import json
import os
from difflib import SequenceMatcher

def load_jsonl(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def match_toc_to_chunks(toc_entries, chunks):
    matched = []
    missing = []
    extra = []

    chunk_ids = {c['section_id']: c for c in chunks}
    toc_ids = {t['section_id']: t for t in toc_entries}

    for toc_id, toc_entry in toc_ids.items():
        if toc_id in chunk_ids:
            matched.append(toc_id)
        else:
            # Try fuzzy match fallback
            possible = [c['section_id'] for c in chunks if SequenceMatcher(None, toc_id, c['section_id']).ratio() > 0.9]
            if possible:
                matched.append(possible[0])  # best guess
            else:
                missing.append(toc_id)

    for chunk_id in chunk_ids:
        if chunk_id not in toc_ids:
            extra.append(chunk_id)

    return matched, missing, extra

if __name__ == "__main__":
    toc_file = os.path.join("output", "usb_pd_spec.jsonl")
    chunk_file = os.path.join("output", "usb_pd_chunks.jsonl")

    toc_entries = load_jsonl(toc_file)
    chunks = load_jsonl(chunk_file)

    matched, missing, extra = match_toc_to_chunks(toc_entries, chunks)

    print(f"✅ Matched: {len(matched)} sections")
    print(f"❌ Missing from chunks: {len(missing)}")
    print(f"➕ Extra sections in chunks: {len(extra)}")

    if missing:
        print("\n🚫 Missing sections from ToC:")
        for mid in missing:
            print(f" - {mid}")
