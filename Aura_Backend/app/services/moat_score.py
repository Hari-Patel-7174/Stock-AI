from transformers import pipeline

# Load zero-shot classification for dynamic label scoring
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_moat(description: str):
    labels = ["Wide Moat", "Narrow Moat", "No Moat"]
    result = classifier(description, candidate_labels=labels)
    top_label = result['labels'][0]
    return top_label, result['scores'][0]

def analyze_cg(description: str):
    labels = ["Excellent Governance", "Good Governance", "Weak Governance"]
    result = classifier(description, candidate_labels=labels)
    top_label = result['labels'][0]
    return top_label, result['scores'][0]

# Example usage
if __name__ == "__main__":
    text_moat = "The company has a dominant telecom market share and operates retail leadership"
    text_cg = "Transparent disclosures, regular board updates, but complex holding structure"

    moat, moat_score = analyze_moat(text_moat)
    cg, cg_score = analyze_cg(text_cg)

    print("Moat:", moat, round(moat_score, 2))
    print("Governance:", cg, round(cg_score, 2))
