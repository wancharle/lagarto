#!/usr/bin/env python
from lagarto.settings import local as settings


def get_log():
    import glob
    import logging
    import logging.handlers

    LOG_FILENAME = settings.LOG_FILENAME #'/home/rabodolagarto/logs/crom_jog.log'

    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('Crom_job')
    my_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(
               LOG_FILENAME, maxBytes=200000, backupCount=5)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler.setFormatter(formatter)

    my_logger.addHandler(handler)

    return my_logger 


printlog = get_log()

from newsletter.email_com_imagem import enviar_email
from newsletter.models import Mensagem, Contato
from django.http import HttpResponse 

def envia_mensagem():
    msgs = Mensagem.objects.filter(estado='1')
    lista=""
    for msg in msgs:
        contatos = Contato.objects.filter(ativo=True,erro=False).exclude(id__in=msg.emails_enviados.all().values("id"))[:5]
        for c in contatos:
            lista +=str(c.email)+"<br> "
            r=enviar_email(msg, c,msg.campanha.servidor,
                    msg.campanha.login,msg.campanha.senha )
            msg.emails_enviados.add(c)

            if (r!=None):
                c.erro=True
                c.save()

        if len(contatos)==0:
            msg.estado='2' # envio completo
        msg.save()
    return "Abaixo segue os emails que foram enviados no ultimo minuto:\n{ %s }" % str(lista)

   
def executa_cron(request):
    r= envia_mensagem() 
    printlog.debug(r)
    return HttpResponse(r,mimetype="text/plain")
