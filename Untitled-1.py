import json
import requests
webhook2 = 'https://hooks.slack.com/services/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'
data = {
    "text" : "There is an attack from IP: 172.26.68.125"
}
requests.post(webhook2,json.dumps(data))
