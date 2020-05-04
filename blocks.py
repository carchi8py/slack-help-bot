http_403 = """
[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Your error message contains a `NetApp API failed. Reason - 403:Forbidden` message. This error can be caused by one of the following\n•The user does not have the correct right (console, http, and ontapi)\n•Http may be disable, on the system run the following to enable it\n•You may have a firewall or Proxy preventing the local host from connecting to the Ontap System"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "If none of the above helped solve your issues please fill out a bug report "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Create new Bug Report",
					"emoji": true
				},
				"value": "bug_report"
			}
		}
	]
"""