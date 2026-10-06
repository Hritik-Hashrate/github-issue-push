from django.shortcuts import render
from django.contrib import messages

from .github_api import create_github_issue, get_github_assignees


def create_issue(request):

    try:
        assignees = get_github_assignees()

    except Exception as e:
        assignees = []
        messages.error(request, str(e))


    if request.method == "POST":

        title = request.POST.get("title")
        priority = request.POST.get("priority")
        description = request.POST.get("description")

        selected_assignees = request.POST.getlist("assignees")
        labels = request.POST.getlist("labels")


        issue_body = f"""
## Priority

{priority}

## Description

{description}
"""


        try:

            issue = create_github_issue(
                title=title,
                body=issue_body,
                assignees=selected_assignees,
                labels=labels
            )

            messages.success(
                request,
                f"GitHub Issue #{issue['number']} created successfully!"
            )

            return render(
                request,
                "issues/create_issue.html",
                {
                    "issue_url": issue["html_url"],
                    "assignees": assignees,
                }
            )

        except Exception as e:

            messages.error(request, str(e))


    return render(
        request,
        "issues/create_issue.html",
        {
            "assignees": assignees,
        }
    )