import csv

def save_to_csv(papers: list[dict], filename: str):
    if not papers:
        return

    headers = list(papers[0].keys())
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(papers)