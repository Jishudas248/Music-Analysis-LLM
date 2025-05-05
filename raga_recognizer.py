"""
Raga Recognition from MP4 Audio
Author: Ashutosh Das
Date: 2025-05-05

Dependencies:
- librosa
- numpy
- moviepy
- tensorflow
- pydub

Install requirements:
pip install librosa numpy moviepy tensorflow pydub
"""

import os
import numpy as np
import librosa
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# =========================
# 1. Audio Extraction
# =========================
def extract_audio_from_mp4(mp4_path, output_wav="temp_audio.wav"):
    """
    Extracts audio from an MP4 file and saves it as a WAV file.
    """
    print(f"Extracting audio from {mp4_path}...")
    video = VideoFileClip(mp4_path)
    video.audio.write_audiofile(output_wav, logger=None)
    return output_wav

# =========================
# 2. Audio Preprocessing
# =========================
def preprocess_audio(file_path, output_path="processed.wav", target_sr=22050):
    """
    Converts audio to mono 22050Hz WAV format.
    """
    print(f"Preprocessing audio {file_path}...")
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1).set_frame_rate(target_sr)
    audio.export(output_path, format="wav")
    return output_path

# =========================
# 3. Feature Extraction
# =========================
def extract_features(audio_path):
    """
    Extracts chroma, MFCC, and delta MFCC features from audio.
    """
    print(f"Extracting features from {audio_path}...")
    y, sr = librosa.load(audio_path, sr=None)
    # Chroma
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    # Tonic normalization (simple roll to max energy)
    chroma = np.roll(chroma, -np.argmax(chroma.mean(axis=1)), axis=0)
    # MFCC and delta
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    delta_mfcc = librosa.feature.delta(mfcc)
    # Combine features
    features = np.vstack([chroma, mfcc, delta_mfcc])
    # Pad/truncate to fixed length for model input (example: 400 frames)
    max_len = 400
    if features.shape[1] < max_len:
        pad_width = max_len - features.shape[1]
        features = np.pad(features, ((0,0),(0,pad_width)), mode='constant')
    else:
        features = features[:, :max_len]
    return features.T  # shape: (frames, features)

# =========================
# 4. Dummy Model Prediction
# =========================
def dummy_predict_raga(audio_features):
    """
    Dummy model: randomly selects a raga.
    Replace this with your trained model for real predictions.
    """
    raga_classes = [
        "Bhairav", "Yaman", "Malkauns", "Bageshree", "Shankarabharanam", 
        "Kafi", "Asavari", "Bhairavi", "Todi", "Purvi", "Marwa", "Khamaj"
    ]
    # Dummy: random prediction
    idx = np.random.randint(len(raga_classes))
    return raga_classes[idx]

# # Uncomment and use this function if you have a trained model
# import tensorflow as tf
# def predict_raga(audio_features, model_path="raga_cnn_model.h5"):
#     model = tf.keras.models.load_model(model_path)
#     features = np.expand_dims(audio_features, axis=0)
#     prediction = model.predict(features)
#     raga_classes = [ ... ]  # your raga label list
#     return raga_classes[np.argmax(prediction)]

# =========================
# 5. Main Pipeline
# =========================
def recognize_raga_from_mp4(mp4_file):
    # Step 1: Extract audio
    wav_file = extract_audio_from_mp4(mp4_file)
    # Step 2: Preprocess audio
    processed_wav = preprocess_audio(wav_file)
    # Step 3: Extract features
    features = extract_features(processed_wav)
    # Step 4: Predict raga
    raga = dummy_predict_raga(features)
    # Clean up temp files
    os.remove(wav_file)
    os.remove(processed_wav)
    return raga

# =========================
# 6. Example Usage
# =========================
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python raga_recognizer.py <input_video.mp4>")
        sys.exit(1)
    mp4_path = sys.argv[1]
    print("Starting raga recognition pipeline...")
    raga = recognize_raga_from_mp4(mp4_path)
    print(f"\nPredicted Raga: {raga}")
