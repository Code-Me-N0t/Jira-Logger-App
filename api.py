from requests.auth import HTTPBasicAuth
import requests
from use_json import *
from tkinter import messagebox
import webbrowser

class JiraAPI:
    def __init__(self):
        self.use = creds
        self.jira_domain = f"{self.use['base_url']}"
        self.auth = HTTPBasicAuth(f"{self.use['email']}", f"{self.use['token']}")
        self.headers = { "Accept": "application/json" }

    def search_jira(self, jql_query):
        jira_api_url = f"{self.jira_domain}/rest/api/2/search"
        
        params = { 'jql': jql_query }
        response = requests.get(jira_api_url, headers=self.headers, auth=self.auth, params=params)

        if response.status_code == 200:
            issues = response.json().get('issues', [])
            if issues:
                return [f"{issue['key']}: {issue['fields']['summary']}" for issue in issues]
            else:
                return ["No issues found."]
        else:
            raise Exception(f"Failed to fetch issues: {response.status_code} - {response.text}")
        
    def redirect_to_jira_issue(self, selected_issue):
        issue_key = selected_issue.split(":")[0]  # Assuming the format is 'KEY: Summary'
        issue_url = f"{self.use['base_url']}/browse/{issue_key}"  # Construct the URL
        webbrowser.open(issue_url)


    def search_jira_issues(self, issue_key):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}"

        response = requests.get(jira_api_url, headers=self.headers, auth=self.auth)

        if response.status_code == 200:
            issue = response.json()
            return f"{issue['key']}: {issue['fields']['summary']}"
        else:
            raise Exception(f"Failed to fetch issue: {response.status_code} - {response.text}")

    def log_time(self, issue_key, time_spent, comment, time_started):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}/worklog"

        data = {
            "timeSpent": time_spent,
            "comment": comment,
            "started": time_started
        }

        response = requests.post(jira_api_url, headers=self.headers, auth=self.auth, json=data)

        if response.status_code != 201:
            raise Exception(f"Failed to log time: {response.status_code} - {response.text}")

    def create_jira_issue(self, summary, description, issue_type, project_key):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue"

        data = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": issue_type
                }
            }
        }

        response = requests.post(jira_api_url, headers=self.headers, auth=self.auth, json=data)

        if response.status_code == 201:
            return response.json().get('key')
        else:
            raise Exception(f"Failed to create issue: {response.status_code} - {response.text}")
        
    def add_comment(self, issue_key, comment_text):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}/comment"

        data = {
            "body": comment_text
        }

        response = requests.post(jira_api_url, headers=self.headers, auth=self.auth, json=data)
        return response.status_code == 201
