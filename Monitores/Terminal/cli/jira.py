import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime


def criarChamadoJira(mensagem):
    url = "https://admsptech.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("lucas.garcia@sptech.school", "ATATT3xFfGF0SjntMy8T-HXEd-Lee1t5KOfJtoNbGR_Oo199zzm7QbD_UfaWi8omIqSvmwp-7tvd3bBZbR5-FBX10AGxWF-C4UZZl-iohI6Vh2tbt-j_pDkJ4B5eHSAtMCnS66dRon_XzKrH9Olck6Bga2ZTSBsltiiTTDSr-mK68n_pH_mU7AM=04669E6D")
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