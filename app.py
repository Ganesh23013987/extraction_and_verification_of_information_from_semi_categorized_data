import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import streamlit as st
import re
from ocr_engine import extract_text
from structure import structure_text
from nlp_engine import extract_entities
from verify import verify
from PIL import Image

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Intelligent Document Verification",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# CSS (unchanged)
# -------------------------------------------------
st.markdown("""
<style>
body { background-color: #0e1117; color: #e5e7eb; }
.main { background-color: #0e1117; }
.card {
    background:#161b22; padding:1.5rem; border-radius:14px;
    box-shadow:0 8px 24px rgba(0,0,0,0.4); margin-bottom:1.5rem;
}
.section-title { font-size:20px; font-weight:600; color:#f1f5f9; }
.badge-success { background:#064e3b; color:#a7f3d0; padding:6px 14px; border-radius:20px; }
.badge-warning { background:#78350f; color:#fde68a; padding:6px 14px; border-radius:20px; }
</style>
""", unsafe_allow_html=True)

st.markdown("## 📄 Intelligent Document Verification System")

# -------------------------------------------------
# SESSION INIT
# -------------------------------------------------
if "ocr_done" not in st.session_state:
    st.session_state.ocr_done = False

if "entities" not in st.session_state:
    st.session_state.entities = {}

if "raw_text" not in st.session_state:
    st.session_state.raw_text = ""

# -------------------------------------------------
# LAYOUT
# -------------------------------------------------
left, right = st.columns([1, 1])

# -------------------------------------------------
# LEFT PANEL — ALWAYS VISIBLE
# -------------------------------------------------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📤 Upload & Applicant Details</div>', unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload Document", type=["png", "jpg", "jpeg"])

    name = st.text_input("Candidate Name")
    dob = st.text_input("Date of Birth (DD/MM/YYYY)")
    cert = st.text_input("Certificate Number (8 digits)")

    valid_inputs = (
        name.strip() and
        re.fullmatch(r"\d{2}/\d{2}/\d{4}", dob) and
        re.fullmatch(r"\d{8}", cert)
    )

    check_clicked = st.button("🔍 Check", disabled=not valid_inputs)

    if not valid_inputs:
        st.info("Enter valid Name, DOB and 8-digit Certificate Number")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# OCR — RUNS AFTER UPLOAD (INPUTS STILL VISIBLE)
# -------------------------------------------------
if uploaded and not st.session_state.ocr_done:
    with open("temp.png", "wb") as f:
        f.write(uploaded.getbuffer())

    with st.spinner("Running OCR..."):
        raw = extract_text("temp.png")
        structured = structure_text(raw)
        entities = extract_entities(structured)

    st.session_state.raw_text = raw
    st.session_state.entities = entities
    st.session_state.ocr_done = True

# -------------------------------------------------
# RIGHT PANEL — ORDERED OUTPUT
# -------------------------------------------------
with right:

    # 1️⃣ VERIFICATION RESULT
    if check_clicked and st.session_state.ocr_done:
        issues, confidence = verify(
            {"name": name, "dob": dob, "certificate_no": cert},
            st.session_state.entities,
            st.session_state.raw_text
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🔍 Verification Result</div>', unsafe_allow_html=True)

        if issues:
            st.markdown('<span class="badge-warning">Human-in-the-loop review required</span>', unsafe_allow_html=True)
            for i in issues:
                st.write(f"• {i}")
        else:
            st.markdown('<span class="badge-success">Document verified successfully</span>', unsafe_allow_html=True)

        st.markdown("**Confidence Scores**")
        for k, v in confidence.items():
            st.write(f"{k}: {v}%")
            st.progress(v / 100)

        st.markdown('</div>', unsafe_allow_html=True)

    # 2️⃣ PREPROCESSED IMAGE
    if st.session_state.ocr_done:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🖼 OCR Input (Preprocessed Image)</div>', unsafe_allow_html=True)
        st.image(Image.open("preprocessed.png"), width=700)
        st.markdown('</div>', unsafe_allow_html=True)

    # 3️⃣ EXTRACTED INFORMATION
    if st.session_state.ocr_done:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📑 Extracted Information</div>', unsafe_allow_html=True)
        st.json({k: list(v) for k, v in st.session_state.entities.items()})
        st.markdown('</div>', unsafe_allow_html=True)
