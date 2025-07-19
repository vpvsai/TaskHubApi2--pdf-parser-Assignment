import json
import re
from difflib import SequenceMatcher

def load_chunks(chunk_file):
    with open(chunk_file, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def find_best_match(chunks, question):
    # Try to match section ID directly
    match = re.search(r'\b(\d+(?:\.\d+)*)\b', question)
    if match:
        section_id = match.group(1)
        for chunk in chunks:
            if chunk['section_id'] == section_id:
                return chunk, 1.0  # Perfect match

    # Fallback: fuzzy title match
    best_score = 0
    best_match = None
    for chunk in chunks:
        text = chunk["title"] + " " + chunk.get("full_path", "")
        score = SequenceMatcher(None, question.lower(), text.lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = chunk

    return best_match, best_score

if __name__ == "__main__":
    chunk_file = 'output/usb_pd_chunks.jsonl'
    chunks = load_chunks(chunk_file)

    print("🔍 Ask a question about the USB PD spec (type 'exit' to quit)\n")

    while True:
        question = input("❓ Your Question: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        best_chunk, score = find_best_match(chunks, question)
        print(f"\n📄 Section: {best_chunk['section_id']} {best_chunk['title']} (Score: {score:.2f})\n")
        print("📝 Answer:\n")
        print(best_chunk["text"][:1000])  # show first 1000 characters of section
        print("\n" + "-"*60 + "\n")
