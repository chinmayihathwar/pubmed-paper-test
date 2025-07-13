import typer
from get_papers.fetch import fetch_pubmed_results
from get_papers.filter import extract_info
from get_papers.csv_writer import save_to_csv

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "-f", "--file"),
    debug: bool = typer.Option(False, "-d", "--debug")
):
    if debug:
        typer.echo(f"Fetching papers for query: {query}")

    xml_data = fetch_pubmed_results(query)
    papers = extract_info(xml_data)

    if file:
        save_to_csv(papers, file)
        typer.echo(f"Saved to {file}")
    else:
        for paper in papers:
            typer.echo(paper)

if __name__ == "__main__":
    app()