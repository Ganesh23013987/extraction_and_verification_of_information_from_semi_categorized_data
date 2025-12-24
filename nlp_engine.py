import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(blocks):
    entities = {
        "PERSON": set(),
        "ORG": set(),
        "DATE": set(),
        "GPE": set()
    }

    for block in blocks:
        doc = nlp(block)
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].add(ent.text)

    return entities
