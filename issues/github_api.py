import os
import requests


GITHUB_API = "https://api.github.com"


def github_headers():

    return {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


# ==========================================================
# CREATE GITHUB ISSUE
# ==========================================================

def create_github_issue(
    title,
    body,
    assignees=None,
    labels=None
):

    owner = os.getenv("GITHUB_OWNER")
    repo = os.getenv("GITHUB_REPO")

    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues"


    # ==================================================
    # ISSUE DATA
    # ==================================================

    data = {
        "title": title,
        "body": body,
    }


    # ==================================================
    # MULTIPLE ASSIGNEES
    # ==================================================

    if assignees:

        data["assignees"] = assignees


    # ==================================================
    # MULTIPLE LABELS
    # ==================================================

    if labels:

        data["labels"] = labels


    # ==================================================
    # CREATE ISSUE
    # ==================================================

    response = requests.post(
        url,
        headers=github_headers(),
        json=data
    )


    # ==================================================
    # ERROR
    # ==================================================

    if response.status_code != 201:

        raise Exception(
            f"GitHub Error: {response.status_code} - {response.text}"
        )


    # ==================================================
    # RETURN CREATED ISSUE
    # ==================================================

    return response.json()


# ==========================================================
# GET GITHUB ASSIGNEES
# ==========================================================

def get_github_assignees():

    owner = os.getenv("GITHUB_OWNER")
    repo = os.getenv("GITHUB_REPO")

    url = f"{GITHUB_API}/repos/{owner}/{repo}/assignees"


    response = requests.get(
        url,
        headers=github_headers()
    )


    if response.status_code != 200:

        raise Exception(
            f"GitHub Error: {response.status_code} - {response.text}"
        )


    return response.json()