import re
from rapidfuzz import fuzz
from utils import normalize

def confidence_name(name, text):
    return fuzz.partial_ratio(normalize(name), normalize(text))

def extract_dates(text):
    return re.findall(r'\b\d{2}[\/\-.]\d{2}[\/\-.]\d{4}\b', text)

def extract_certificate_numbers(text):
    return re.findall(r'\b\d{8}\b', text)

def verify(form_data, extracted_entities, full_text=""):
    issues = []
    confidence = {}

    # ---------- NAME ----------
    name = form_data.get("name", "")
    name_candidates = list(extracted_entities.get("PERSON", [])) + [full_text]


    name_scores = [
        confidence_name(name, c) for c in name_candidates
    ] if name else [0]

    name_conf = max(name_scores)
    confidence["Name"] = name_conf

    if name_conf < 80:
        issues.append("Candidate name mismatch or low confidence")

    # ---------- DOB ----------
    dob = form_data.get("dob", "")
    extracted_dobs = extract_dates(full_text)
    dob_conf = 100 if dob in extracted_dobs else 0
    confidence["Date of Birth"] = dob_conf

    if dob and dob_conf == 0:
        issues.append("Date of birth mismatch or not found")

    # ---------- CERTIFICATE ----------
    cert = form_data.get("certificate_no", "")
    extracted_certs = extract_certificate_numbers(full_text)
    cert_conf = 100 if cert in extracted_certs else 0
    confidence["Certificate Number"] = cert_conf

    if cert and cert_conf == 0:
        issues.append("Certificate number mismatch or not found")

    return issues, confidence
