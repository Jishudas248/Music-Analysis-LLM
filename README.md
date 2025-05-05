# 🎶 Musical LLM – AI-Powered Raag and Audio Analysis Toolkit

**A Multimodal Music Analysis Toolkit for Indian Classical and Western Music Traditions using AI**

---

## 🧠 Overview

**Musical LLM** is an AI-powered music analysis toolkit designed to bridge the gap between computational musicology and Indian/Western classical music traditions. It focuses on analyzing `.wav`, `.mp3`, and MIDI files to extract musical insights including:

* Raag identification (Hindustani Classical)
* Chord progression detection (Western theory)
* Key, tempo, scale, and rhythmic analysis
* MIDI generation and music staff notation
* Instrument separation and symbolic music output

This project aims to serve musicians, composers, educators, and AI researchers who are looking to fuse traditional musical analysis with modern AI techniques.

---

## 🎯 Key Features

### 🔀 Audio Source Separation

* Uses **Spleeter** to isolate vocals, drums, and instrumental tracks.
* Focuses particularly on the **instrument track** to extract more accurate melodic information for MIDI generation.

### 🎼 Symbolic Music Generation

* Generates **MIDI files** using `pretty_midi`
* Converts analyzed features into **Western staff notation** using `music21`

### 🎵 Indian Classical Analysis

* **Detects the root note (Sa)** and estimates the **scale/raag**
* Compares melodic structure against known **Hindustani Raags** to predict the most likely Raag
* Identifies **rhythmic cycles** (Taal/Tala) based on tempo and beat patterns

### 🎹 Western Classical Analysis

* Detects **key signature**, **chord progressions**, and **harmonic structure**
* Estimates **time signature** and rhythm patterns

### 🧑‍🎤 User Interaction

* **Gradio interface** provides a clean, browser-based UI for users to upload files and view results
* Displays waveforms, MIDI previews, and sheet music interactively

---

## 🧰 Technology Stack & Dependencies

* **Python 3.10+**
* [`librosa`](https://librosa.org/) – audio feature extraction
* [`Spleeter`](https://github.com/deezer/spleeter) – source separation
* [`music21`](https://web.mit.edu/music21/) – music theory and notation
* [`pretty_midi`](https://github.com/craffel/pretty-midi) – MIDI file manipulation
* [`gradio`](https://gradio.app/) – browser-based UI
* **FFmpeg** – required backend for audio I/O
* **TensorFlow / PyTorch** – (for Spleeter and potential deep models)

---

## 🚀 Future Directions

This toolkit is designed as a foundation and will continue evolving into a multimodal, multilingual music analysis platform. Planned enhancements include:

### 🖼️ Sheet Music (Image) Support

* Integrate **Optical Music Recognition (OMR)** using models like:

  * [`naver-clova-ix/donut-base-finetuned-omr`](https://huggingface.co/naver-clova-ix/donut-base-finetuned-omr)
  * Audiveris (open-source OMR)

### 🗣️ Text & Voice Notes as Input

* Use **Whisper** to transcribe voice memos or sung examples
* Feed transcribed text into an **LLM** (e.g., Mistral, LLaMA) for explanation, discussion, or generation of musical instructions

### 🎺 Carnatic Classical Expansion

* Add support for **Carnatic Ragas**, **Gamaka analysis**, and **Tala system** recognition
* Use **custom-trained models** or rule-based logic for more accurate Carnatic analysis

### 💬 LLM Integration

* Use `transformers` to power a music theory assistant that can explain results, generate new compositions, or translate theory across music systems

---

## 📂 Project Structure

```
musical-llm/
├── audio_analysis.py         # Main entry point
├── separated_audio/          # Output from Spleeter
├── midi_output/              # Generated MIDI files
├── notation_output/          # Sheet music files
├── models/                   # Future ML model files
└── gradio_ui.py              # UI app
```

---

## 📌 Use Cases

* 🎓 **Music Students** – Analyze ragas, notations, and rhythms from recordings
* 🎧 **AI & ML Researchers** – Study audio/music processing with deep learning
* 🧑‍🎻 **Fusion Composers** – Convert raags into MIDI for orchestration
* 🪪 **Educators** – Use staff notation + audio separation in classrooms
* 🎤 **Performers** – Visualize and practice from their own recordings

---

## 🛠️ Installation & Usage

### 🔧 Prerequisites

Make sure you have:

* Python 3.10+
* `ffmpeg` installed and added to your system `PATH`

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install librosa music21 pretty_midi spleeter gradio transformers
```

### ▶️ Run the Application

```bash
python gradio_ui.py
```

Then open your browser to view the interface and upload your audio files.

---

## 🌐 Related Resources

* [Raag Recognition Papers](https://arxiv.org/abs/1703.08115)
* [Carnatic Music Analysis Tools](https://compmusic.upf.edu/)
* [OMR for Indian Music](https://audiveris.github.io/)
* [Hugging Face Music Models](https://huggingface.co/models?pipeline_tag=audio)

---

## 🤝 Contributing

Contributions, feature suggestions, and dataset links are welcome! Please open an issue or pull request with details.

---

## 📜 License

This project is under no license but have a Keen Ideology to use for all.

---
