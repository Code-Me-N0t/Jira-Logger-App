<h1>Jira Logger App</h1>
I created a simple lighweight and user-friendly Jira Logger App designed to interact using JIRA API.
<br>
<h2>FEATURES</h2>
<h5>• JQL Search:</h5>&nbsp Enter JQL queries to search for issues in JIRA.
<h5>• Log Time:</h5>&nbsp Log time spent on existing issues, including comments for better tracking.
<h5>• Create Tickets:</h5>&nbsp Easily create new JIRA tickets with project keys, issue types, summaries, and descriptions.
<br>
<h2>Tools</h2>
<h5>• Python:</h5> The core programming language for building the application.
<h5>• Tkinter:</h5> Used for creating the GUI.
<h5>• JIRA API:</h5> Interaction with JIRA's API for fetching and managing issues.
<br>
<h2>Installation</h2>
<p>To run the application, ensure you have Python installed on your computer. Then, follow these steps:</p>
• First, create a json file named <em>"creds.json"</em> where you need to put three data:
<pre><code id=code-block>
  //creds.json<br>
  {
  "base_url": "your-jira-base-url",
  "token": "your-jira-token",
  "email: "your-work-email"
</code></pre>


<pre><code id=code-block>try</code></pre>
