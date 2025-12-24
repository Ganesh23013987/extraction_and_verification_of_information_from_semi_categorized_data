# Intelligent Document Verification System (IDP)

An **AI-assisted Intelligent Document Processing (IDP)** system that automatically extracts and verifies information from semi-structured documents such as certificates and biodata submissions, with **human-in-the-loop review** for reliability.

This project is built using **only open-source tools**, requires **no paid APIs**, and supports **GPU acceleration** for fast processing.

---

## 📌 Problem Statement

In online application systems, candidates submit biodata along with supporting documents such as:
- Educational certificates
- Date of Birth proof
- Certificate / Registration numbers

Verification of these documents is traditionally **manual**, time-consuming, and error-prone.

This system automates the **extraction and verification** of information using OCR and NLP techniques, while safely escalating uncertain cases for **manual review**.

---

## 🎯 Key Features

- 📄 OCR using **EasyOCR** (CPU / GPU supported)
- 🖼️ Grayscale preprocessing for improved OCR accuracy
- 🧠 NLP-based entity extraction
- 🔍 Verification of:
  - Candidate Name (fuzzy, case-insensitive)
  - Date of Birth
  - 8-digit Certificate Number
- 📊 Confidence score for each field
- 🧑‍⚖️ Human-in-the-loop review workflow
- ⚡ Fast processing (≤ 3 seconds per document)
- 🎨 Modern Streamlit web interface
- 💻 100% open-source, no paid services

---

## 🧠 System Architecture


Document Upload
↓
Preprocessing (Grayscale + Intensity)
↓
OCR (EasyOCR)
↓
Text Structuring
↓
Entity Extraction (spaCy)
↓
Verification & Confidence Scoring
↓
Auto-Approval OR Human Review


---

## 🖥️ Technology Stack

| Component | Technology |
|--------|-----------|
| OCR | EasyOCR |
| Image Processing | OpenCV |
| NLP | spaCy |
| Verification | RapidFuzz |
| UI | Streamlit |
| Language | Python |
| Acceleration | GPU (CUDA via PyTorch) |

---

## 📁 Project Structure

intelligent-document-verification/
│
├── app.py # Streamlit frontend
├── ocr_engine.py # OCR logic (CPU/GPU)
├── preprocess.py # Image preprocessing
├── structure.py # Text structuring
├── nlp_engine.py # Entity extraction
├── verify.py # Verification + confidence
├── utils.py # Text normalization
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── sample_docs/
└── sample_certificate.jpg


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/intelligent-document-verification.git
cd intelligent-document-verification
```
### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
### ⚡ GPU Acceleration (Optional but Recommended)
If you have an NVIDIA GPU:
```bash
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
Verify GPU availability:
```bash
import torch
print(torch.cuda.is_available())
```

### ▶️ Running the Application
```bash
streamlit run app.py
```
Open in browser:

```bash
http://localhost:8501
```
---
### 🧪 How the System Works

1.Upload a document

2.OCR runs automatically

3.Extracted text and image are displayed

4.User enters Name, DOB, and Certificate Number

5.Verification runs on button click

6.System either:

  .✅ Auto-verifies, or

  .⚠️ Escalates to human review

### 📊 Accuracy & Performance

<img width="699" height="268" alt="image" src="https://github.com/user-attachments/assets/97d88e5e-a330-4948-8014-c6024aaa957e" />

---
### 🧑‍⚖️ Human-in-the-Loop Design

Instead of rejecting applications on uncertainty, the system flags low-confidence cases and requests manual verification. This improves reliability and aligns with real-world government and enterprise workflows.

---

## Future Enhancements

- Region-based OCR
- PDF document support
- Table extraction for marksheets
- Dashboard and analytics
- Audit logs and reports
- Model fine-tuning with feedback

---

## License

MIT License

---

## Author

Developed as part of an Intelligent Document Processing (IDP) project using open-source AI tools.

