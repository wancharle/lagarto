# -*- coding: utf-8 -*-
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

def limpa(email):
	return email.replace("\r","")

def enviar_email(msg,destino,servidor,login,senha):
    msgRoot = MIMEMultipart('related')
    msgRoot.set_charset("utf-8")
    msgRoot['Subject'] = msg.assunto #'Meu desejo de Boas Festas'
    msgRoot['From'] =  msg.email_from
    msgRoot['To'] = limpa(destino.email)
    msgRoot['List-Unsubscribe']= msg.email_responder_para
    msgRoot['Precedence'] = 'bulk'
    msgRoot['Reply-To'] = msg.email_responder_para 
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgAlternative.set_charset("utf-8")

    msgText = MIMEText(msg.mensagem_texto_alternativo.encode("utf-8"),_charset="utf-8")
    msgAlternative.attach(msgText)
    remove_span = u"""<p style="text-align:center;font-family:Verdana;font-size:9pt;color:#a2a2a2;">Caso não esteja visualizando corretamente este e mail, 
<a  href="http://rabodolagarto.com.br/newsletter/view/%d/">acesse aqui</a></p><br>
<br>%s <p style="text-align:center;font-size:9pt;font-family:Verdana;color:#a2a2a2;">Caso não queira mais receber informações da pousada 
<a href="http://rabodolagarto.com.br/newsletter/cancela/%d/%d/">clique aqui</a> 
ou responda este email com assunto REMOVER.<br>
Agradecemos sua atenção durante este período.</p>
""" % (msg.id,msg.mensagem,msg.id,destino.id)
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(remove_span.encode("utf-8"),'html',_charset="utf-8")
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(msg.imagem.path)
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP()
    smtp.connect(servidor)
    smtp.starttls()
    smtp.login(login,senha)
    try:
    	smtp.sendmail(msg.email_from, [limpa(destino.email),], msgRoot.as_string())
    except Exception, err:
        return err
    smtp.quit()
    return None

