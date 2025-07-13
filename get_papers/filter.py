import re
from xml.etree import ElementTree as ET

def is_company_affiliation(text: str) -> bool:
    companies_keywords = ["pharma", "biotech", "inc", "llc", "gmbh", "corp"]
    return any(word.lower() in text.lower() for word in companies_keywords)

def extract_info(xml_data: str) -> list[dict]:
    root = ET.fromstring(xml_data)
    results = []
    for article in root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "Publication Date": article.findtext(".//PubDate/Year"),
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": ""
        }

        for author in article.findall(".//Author"):
            aff = author.findtext("AffiliationInfo/Affiliation", default="")
            name = author.findtext("LastName", "") + " " + author.findtext("ForeName", "")
            email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", aff)

            if is_company_affiliation(aff):
                paper["Company Affiliation(s)"].append(aff)
            elif "univ" not in aff.lower() and "institute" not in aff.lower():
                paper["Non-academic Author(s)"].append(name)

            if email:
                paper["Corresponding Author Email"] = email[0]
        
        if paper["Company Affiliation(s)"]:
            results.append(paper)
    return results