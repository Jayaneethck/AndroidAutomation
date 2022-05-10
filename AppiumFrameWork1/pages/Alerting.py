# https://hooks.slack.com/services/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
import json

import requests as requests
from aiohttp import request


class slackalerts():
    """def slackalert(request, result):
        driver = request
        webhook_url = 'https://hooks.slack.com/services/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'
        slack_data = {'text': result}

        response = driver.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

        return
    """



    def slackalert(self,result):
        webhook_url = 'https://hooks.slack.com/services/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'
        slack_data = {'text':result}

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

        return
