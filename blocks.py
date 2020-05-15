http_403 = """
[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Your error message contains a `NetApp API failed. Reason - 403:Forbidden` message. This error can be caused by one of the following:\n• The user does not have the correct right (console, http, and ontapi)\n• Http may be disable, on the system run the following to enable it\n• You may have a firewall or Proxy preventing the local host from connecting to the Ontap System"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "If the above didn't help you fix your issue please respond to this thread with the following information:\n• Ansible Version\n• Collection Version \n• Which Module you were trying to run \n• The output of the playbook run with the -vvv option (specificly the stack trace portion)"
			}
		}
	]
"""
console_permission = """
[
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Your error message contains a `<cli-output/><cli-result-value>0</cli-result-value></results>` this message means the user you ran `na_ontap_command` with did not have console permission. Please add console permission to the user and try again"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "If the above didn't help you fix your issue please respond to this thread with the following information:\n• Ansible Version\n• Collection Version \n• Which Module you were trying to run \n• The output of the playbook run with the -vvv option (specificly the stack trace portion)"
			}
		}
	]
"""
unexpected_error = """
[
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "It appear you have hit An Unexpected error, this is almost always because of one of a couple issue. We have steps on how to find and fix each of these issues in the following blog",
				"emoji": true
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://netapp.io/2019/08/05/dealing-with-the-unexpected|Dealing with the Unexpected - thePub>"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://netapp.io/wp-content/uploads/2018/10/ansible-6.jpg",
				"alt_text": "Dealing with the Unexpected"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "If the above didn't help you fix your issue please respond to this thread with the following information:\n• Ansible Version\n• Collection Version \n• Which Module you were trying to run \n• The output of the playbook run with the -vvv option (specificly the stack trace portion)"
			}
		}
	]
"""