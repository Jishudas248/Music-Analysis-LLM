# 🎵 Musical LLM – Audio Analysis & Composition Toolkit

**Musical LLM** is a Python-based toolkit for analyzing and composing music using audio processing, machine learning, and symbolic music representation. Designed for musicologists, AI researchers, and composers, this toolkit extracts meaningful musical elements from audio and assists in creative musical tasks.

---

## ✨ Features

* 🎹 **Source Separation** (vocals, drums, instruments) using Spleeter
* 🎼 **Pitch Detection & Key Estimation** (Western and Indian Classical)
* 🪕 **Raag Detection** for Indian classical audio samples
* 🎺 **MIDI Transcription** from instrumental parts
* 🔄 **Chord Progression & Rhythmic Pattern Extraction**
* 📊 **Visualizations** – frequency plots and staff notation

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/musical-llm.git
cd musical-llm
pip install -r requirements.txt
```

Ensure you have [FFmpeg](https://ffmpeg.org/download.html) installed and added to your system path.

---

## ▶️ Usage

```bash
python audio_analysis.py raag_sample.wav
```

Outputs:

* Key note and tempo
* Raag identification (experimental)
* Chord progression
* MIDI file (from instrument stem)
* Staff notation and frequency visualizations

---

## 📁 File Structure

```
musical-llm/
│
├── audio_analysis.py       # Main script
├── requirements.txt        # Dependencies
├── separated_audio/        # Auto-generated stems
├── output/                 # MIDI and visualizations
└── README.md               # You are here!
```

---

## 📚 Dependencies

* librosa
* pretty\_midi
* music21
* spleeter
* gradio
* transformers
* matplotlib
* numpy
* torch
* soundfile

Tested on **Python 3.10+**

---

## 🧠 Future Plans

* Integrate music generation via transformer models
* Real-time audio processing (Web + CLI)
* Raga-based melody generation

---

## 💡 Credits

Developed with ❤️ by \[Your Name].
Inspired by the intersection of classical music and machine learning.

---

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
