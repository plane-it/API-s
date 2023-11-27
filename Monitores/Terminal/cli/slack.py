import requests
from requests.auth import HTTPBasicAuth
import json
import jira
from datetime import datetime

def montarMensagem(idComponente, tipoComponente, servidor, metricaLimite, unidadeMedida, valorRegistro, urgencia):
    if urgencia.lower() == 'alta':
        emoji = '🔥'
    elif urgencia.lower() == 'média':
        emoji = '⚠️'
    else:
        emoji = 'ℹ️'
        
    mensagem = {
        "text": f"""
            {emoji} ALERTA {emoji}
            O componente com ID: {idComponente}, do tipo: {tipoComponente}, localizado no servidor: {servidor}, registrou um valor de: {valorRegistro} {unidadeMedida}. 
            Isso ultrapassa a métrica limite estabelecida de {metricaLimite} {unidadeMedida}. Portanto, um chamado foi criado com urgência: {urgencia}.
        """
    }
    return mensagem

def enviarMensagem(mensagem):
    chatAlert = "https://hooks.slack.com/services/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"
    postMsg = requests.post(chatAlert, data=json.dumps(mensagem))



