import requests
from bs4 import BeautifulSoup
import csv

token = "YOUR TOKEN GOES HERE"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def github_search(q, l):
    """
    Function to gather 50 links to pull requests matching the query and labels

    Parameters
    ----------
    q - (str) query
    l - (str) label

    Returns
    -------
    links - (list) URLs to GitHub pull requests
    """
    query = f'https://api.github.com/search/issues?q={q}+label:{l}+is:issue&per_page=50'
    pull_requests = requests.get(query, headers=HEADERS).json()["items"]

    links = [["link"]]
    for pr in pull_requests:
        links.append([pr["html_url"]])

    return links

if __name__ == "__main__":
    # getting the links for the specified search request
    links = github_search('"accessibility" OR "a11y"', '"good first issue"')

    # outputting the links into a one column CSV file
    with open("links.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(links)
