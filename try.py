from requests.auth import HTTPBasicAuth
import requests
from use_json import *
from tkinter import messagebox

class JiraAPI:
    def __init__(self):
        self.use = creds
        self.jira_domain = f"{self.use['base_url']}"
        self.auth = HTTPBasicAuth(f"{self.use['email']}", f"{self.use['token']}")
        self.headers = { "Accept": "application/json" }

    def search_jira(self, jql_query):
        jira_api_url = f"{self.jira_domain}/rest/api/2/search"
        
        print(f'Query: {jql_query}')
        
        params = {
            'jql': jql_query,
            'maxResults': 10
        }
        response = requests.get(jira_api_url, headers=self.headers, auth=self.auth, params=params)  # Use params instead of json
        print(f'Response: {response.json()}')  # Changed to print full response for debugging

        if response.status_code == 200:
            issues = response.json().get('issues', [])
            if issues:
                print([f"{issue['key']}: {issue['fields']['summary']}" for issue in issues])
            else:
                print(["No issues found."])
        else:
            raise Exception(f"Failed to fetch issues: {response.status_code} - {response.text}")


jira = JiraAPI()
jira.search_jira('project = PRD')