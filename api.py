from requests.auth import HTTPBasicAuth
import requests
from use_json import *
from tkinter import messagebox

class JiraAPI:
    def __init__(self):
        self.use = creds
        self.jira_domain = f"{self.use['base_url']}"
        self.auth = HTTPBasicAuth(f"{self.use['email']}", f"{self.use['token']}")

    def search_jira_issues(self, issue_key):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}"
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(jira_api_url, headers=headers, auth=self.auth)

        if response.status_code == 200:
            issue = response.json()
            return f"{issue['key']}: {issue['fields']['summary']}"
        else:
            raise Exception(f"Failed to fetch issue: {response.status_code} - {response.text}")
    
    def search_jql_query(self, jql_entry):
        jira_api_url = f"{self.jira_domain}/rest/api/2/search"

        jql_query = jql_entry.get("1.0", "end-1c").strip()

        headers = {
            "Accept": "application/json"
        }

        response = requests.get(jira_api_url, headers=headers, auth=self.auth, params={'jql': jql_query})

        if response.status_code == 200:
            issues = response.json().get('issues', [])
            if issues:
                result = "\n".join([f"{issue['key']}: {issue['fields']['summary']}" for issue in issues])
                messagebox.showinfo("Search Results", result)
            else:
                messagebox.showinfo("Search Results", "No issues found.")
        else:
            messagebox.showerror("Error", f"Failed to fetch issues: {response.status_code} - {response.text}")


    def log_time_on_issue(self, issue_key, time_spent, comment):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}/worklog"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "timeSpent": time_spent,
            "comment": comment
        }

        response = requests.post(jira_api_url, headers=headers, auth=self.auth, json=data)

        if response.status_code != 201:
            raise Exception(f"Failed to log time: {response.status_code} - {response.text}")

    def create_jira_issue(self, summary, description, issue_type, project_key):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue"
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

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

        response = requests.post(jira_api_url, headers=headers, auth=self.auth, json=data)

        if response.status_code == 201:
            return response.json().get('key')
        else:
            raise Exception(f"Failed to create issue: {response.status_code} - {response.text}")
        
    def add_comment(self, issue_key, comment_text):
        jira_api_url = f"{self.jira_domain}/rest/api/2/issue/{issue_key}/comment"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "body": comment_text
        }
        
        response = requests.post(jira_api_url, headers=headers, auth=self.auth, json=data)
        print(f'Response: {response.json()}')
        return response.status_code == 201
