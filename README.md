<h1>Jira Logger App</h1>
I created a simple lighweight and user-friendly Jira Logger App designed to interact using JIRA API.
<br>
<h2>FEATURES</h2>
<p><b>• JQL Search:</b> Enter JQL queries to search for issues in JIRA.</p>
<p><b>• Log Time:</b> Log time spent on existing issues, including comments for better tracking.</p>
<p><b>• Create Tickets:</b> Easily create new JIRA tickets with project keys, issue types, summaries, and descriptions.</p>

<h2>Tools</h2>
<p><b>• Python:</b> The core programming language for building the application.</p>
<p><b>• Tkinter:</b> Used for creating the GUI.</p>
<p><b>• JIRA API:</b> Interaction with JIRA's API for fetching and managing issues.</p>

<h2>Installation</h2>
<p>To run the application, ensure you have Python installed on your computer. Then, follow these steps:</p>
• First, create a json file named <em>"creds.json"</em> on the root folder where you need to put three data:
<pre><code id=code-block>
  <i>//creds.json</i>
  {
  "base_url": "your-jira-base-url",
  "token": "your-jira-token",
  "email: "your-work-email"
  }
</code></pre>
<br>
• Second, Clone the repository:
<pre><code id=code-block>
  git clone https://github.com/Code-Me-N0t/Jira-Logger-App.git
  cd JiraLoggerApp
</code></pre>
<br>
• Third, install the required package/s:
<pre><code>
  <i>//bash:</i>
  pip install -r requirements.txt
</code></pre>
<br>
• Fourth, run the application:
<pre><code>
  <i>//bash:</i>
  python timelogger_fe.py
</code></pre>
<br>
<i>* You can also run the executable file created in the <b>dist</b> folder</i>


<pre><code id=code-block>try</code></pre>
