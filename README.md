# 🎭 Deep Face Full Analyzer & Liveness Checker

An interactive AI-powered web application that performs comprehensive facial analysis in real-time. Built using **Streamlit** and the **DeepFace** library, this tool is designed for educational purposes to demonstrate how Deep Learning models interpret human attributes and verify identity.

---

## 🚀 Project Overview

**Deep Face Analyzer** allows users to extract deep insights from facial data across three different input modes. It doesn't just recognize a face; it understands the attributes and checks for authenticity.

### 🌟 Key Features
*   **Emotion Detection:** Instantly identifies feelings (Happy, Sad, Angry, Surprise, Neutral, etc.).
*   **Demographic Analysis:** Provides estimates for **Age**, **Gender**, and **Dominant Race**.
*   **Liveness Detection (Anti-Spoofing):** A security layer that distinguishes between a real person and a digital spoof (like a photo or a screen).
*   **Interactive Input:** 
    *   📷 **Image Upload:** Detailed analysis for static photos.
    *   📹 **Video Upload:** High-power processing for video files.
    *   🎥 **Live Webcam:** Real-time attribute tracking and visual overlays.

---

## 🧠 The Models Behind the App

To ensure high accuracy, this project utilizes specialized models for different tasks:
*   **Face Detection:** Uses the **OpenCV** or **RetinaFace** backend to find faces in a frame.
*   **Feature Extraction:** Leverages **VGG-Face** and **FaceNet** architectures to convert facial features into numerical embeddings.
*   **Liveness:** Employs specialized **Anti-Spoofing** weights to detect screen glare or flat photo edges.

---

## 🛠️ Tech Stack
*   **Language:** Python
*   **Web Framework:** Streamlit
*   **AI Library:** DeepFace
*   **Computer Vision:** OpenCV & Pillow
*   **Backend:** TensorFlow / Keras

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/pythonophile/Deepface-Analyzer.git](https://github.com/pythonophile/Deepface-Analyzer.git)
cd Deepface-Analyzer
