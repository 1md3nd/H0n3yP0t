import logging

import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class SlackWebhookBot:
    def __init__(self, webhook_url: str, timeout: int = 15):
        """Class to send messages to a provided Slack webhook URL.

        You can read more about Slack's Incoming Webhooks here:
            https://api.slack.com/messaging/webhooks
        
        Args:
            webhook_url: The webhook URL to send a message to.  Typically
                formatted like "https://hooks.slack.com/services/...".
        
        Kwargs:
            timeout: Number of seconds before the request will timeout.
                This is used to prevent a hang and is set to a default
                value of 15 seconds.
        """
        self.webhook_url = webhook_url
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
        }
    

    def send(self, message: str) -> bool:
        """Sends a message to the webhook URL.

        Per the Slack Incoming Webhook example.  The body of the request
        (for plain text) should be formatted as follows:
            `{"text": "Hello, Wrld!"}`

        Args:
            message: Plain text string to send to Slack.

        Returns:
            A boolean representing if the request was successful.
        """
        success = False
        payload = {
            'text': message,
        }
        try:
            r = requests.post(
                self.webhook_url,
                headers=self.headers,
                json=payload,
                timeout=self.timeout
            )
        except requests.Timeout:
            logger.error('Timeout occurred when trying to send message to Slack.')
        except requests.RequestException as e:
            logger.error(f'Error occurred when communicating with Slack: {e}.')
        else:
            success = True
            logger.info('Successfully sent message to Slack.')

        return success
