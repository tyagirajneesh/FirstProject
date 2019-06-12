jira_server = 'http://10.89.4.22:8080'
jira_user = 'vinay_singh'
jira_pass = 'satgurudev@05'
jira_transition = 'Done'  # Transition to close issue. Read more https://jira.readthedocs.io/en/master/examples.html#transitions
jira_project = 'ZAB'  # Your project key, for example "ZBX"
jira_issue_type = 'Incident'  # Your issue type in Jira project(Error, Bug, Epic ...)

zbx_prefix = "zbx"  # variable for separating text from script info
zbx_tmp_dir = "/tmp/" + zbx_prefix  # directory for saving caches, cookies, etc.
zbx_server = "http://10.200.208.24/zabbix"  # zabbix server full url
zbx_api_user = "admin"
zbx_api_pass = "zabbix"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore
check
proxy_to_zbx = None
proxy_to_tg = None
new_line=None

# proxy_to_zbx = "proxy.local:3128"
# proxy_to_tg = "proxy.local:3128"
