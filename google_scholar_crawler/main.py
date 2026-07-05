import scholarly
import json
import sys
import os

author_id = os.environ.get("GOOGLE_SCHOLAR_ID", "Gs22F0UAAAAJ")

author = scholarly.search_author_id(author_id)
author = scholarly.fill(author, sections=["basics", "indices", "publications"])

publications = {}
for pub in author.get("publications", []):
    pub_filled = scholarly.fill(pub)
    pub_id = pub_filled.get("author_pub_id", "")
    publications[pub_id] = {
        "num_citations": pub_filled.get("num_citations", 0),
        "title": pub_filled["bib"].get("title", ""),
    }

total_citations = author.get("citedby", 0)
h_index = author.get("hindex", 0)
i10_index = author.get("i10index", 0)

gs_data = {
    "citedby": total_citations,
    "hindex": h_index,
    "i10index": i10_index,
    "publications": publications,
}

os.makedirs("google-scholar-stats", exist_ok=True)

with open("google-scholar-stats/gs_data.json", "w") as f:
    json.dump(gs_data, f, ensure_ascii=False, indent=2)

shieldsio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(total_citations),
    "color": "9cf",
}

with open("google-scholar-stats/gs_data_shieldsio.json", "w") as f:
    json.dump(shieldsio_data, f, ensure_ascii=False, indent=2)

print(f"Total citations: {total_citations}")
print(f"H-index: {h_index}")
print(f"Publications crawled: {len(publications)}")
