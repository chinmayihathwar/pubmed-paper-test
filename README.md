# Get PubMed Papers

## Description
Fetch PubMed papers with at least one author affiliated with a pharmaceutical/biotech company.

## Usage

```bash
poetry run get-papers-list --query "cancer therapy" -f output.csv
```

## Flags
- `--help`: Show help
- `--debug`: Debug output
- `--file`: Output file

## Dependencies
- `requests`
- `typer`
- Managed via Poetry

## Project Structure
- `get_papers/`: Core logic
- `cli/`: CLI script