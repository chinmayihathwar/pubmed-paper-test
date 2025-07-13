import requests

def fetch_pubmed_results(query: str, max_results: int = 20) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    ids = response.json()["esearchresult"]["idlist"]

    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    details_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    detail_response = requests.get(details_url, params=details_params)
    detail_response.raise_for_status()
    return detail_response.text