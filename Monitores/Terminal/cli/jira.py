import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime


def criarChamadoJira(mensagem):
    url = "https://admsptech.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("lucas.garcia@sptech.school", "ATATT3xFfGF01wH3eD_ALyB-rC0ZTwvnaMu1ewXtPmO1ZNsZUcPM5X_QcUcBx8NrhURMqh0H3fl5WduF4BCn1ctaGCYGT7neGQNI337yKbhZzjIkazhYPBxxIeHmaRjTELSl0QhhYbYZxotcUnQcU0dASNFLEEbELYSHGW4LDuqsRFSP7zkSbJw=A2C1523C")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "fields": {
            "summary": "837021 - ALERTA DO SLACK",
            "project": {"key": "ITSAMPLE"},
            'issuetype': {'name': '[System] Problem'},
            "description": mensagem["text"]
        }
    })
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))