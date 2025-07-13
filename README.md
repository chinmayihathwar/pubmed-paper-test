 🔹Description
A Python CLI tool to fetch PubMed papers where at least one author is affiliated with a pharmaceutical or biotech company. It uses the PubMed API, filters affiliations, extracts contact information, and outputs clean CSV data.
🔹 Example Usage
poetry run get-papers-list --query "cancer therapy" -f output.csv
🔹 Features
-  Search PubMed articles by keyword (--query)
-  Filters out papers with industry-affiliated authors
-  Extracts corresponding author email addresses
-  Saves results in a clean CSV format
🛠 CLI Options
🔹Option	Description
--query	 Required. Search term (e.g., "cancer")
--file, -f	Optional. Output CSV file name
--debug, -d	Show debug output during fetch and parse
--help	Show CLI help info
  🔹 Project Structure
pubmed-paper-test/
├── cli/
│   └── main.py               # Typer CLI entrypoint
├── get_papers/
│   ├── fetch.py              # PubMed API fetch logic
│   ├── filter.py             # Author filtering and parsing
│   ├── csv_writer.py         # Save results to CSV
├── pyproject.toml            # Poetry project file
└── README.md                 # This file
  🔹 Dependencies
Managed via Poetry:
- typer
- requests

Install with:
poetry install
poetry shell
🔹 Sample Output (output.csv)
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
40645296,"SARS-CoV-2 neutralization and protection...",2025,"Petrovsky Nikolai; Lebedin Yuri","Max Delbrück Center for Molecular Medicine...",lebedin@xema.fi
🔹 Author
Chinmayi Hathwar
GitHub Profile: https://github.com/chinmayihathwar
