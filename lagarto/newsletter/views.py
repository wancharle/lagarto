#! -*- coding:utf-8 -*-
from email_com_imagem import enviar_email

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import  simplejson as json

from newsletter.models import Mensagem, Contato
import csv
   
def cancela_newsletter(request,id_msg,id_contato):
    msg = Mensagem.objects.get(id=id_msg)
    msg.cancelamentos+=1
    msg.save()

    contato = Contato.objects.get(id=id_contato)
    contato.ativo =False
    contato.save()

    return HttpResponse("<h1>Seu email foi removido da nossa base de dados com sucesso!</h1>")


def exportar_nao_enviados(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=emails_com_problema.csv'
    msgs = Contato.objects.filter(erro=True)

    writer = csv.writer(response)
    for m in msgs:
        writer.writerow([m.email,])

    return response
 
def exportar_contatos(request,ativo):
    response = HttpResponse(mimetype='text/csv')
    if ativo== "ativos":
        response['Content-Disposition'] = 'attachment; filename=emails_ativos.csv'
        msgs = Contato.objects.filter(ativo=True)
    else:
        response['Content-Disposition'] = 'attachment; filename=nao_querem_receber_emails.csv'
        msgs = Contato.objects.filter(ativo=False)

    writer = csv.writer(response)
    for m in msgs:
        writer.writerow([m.email,])

    return response


def ver_mensagem(request,msg_id):
    m = Mensagem.objects.get(id=msg_id)
    html = m.mensagem
    html = html.replace("cid:image1",m.imagem.url)
    return HttpResponse("""<html><head><title>%s</title><script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-21759410-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script></head><body>%s</body></html>""" % (m.assunto,html),"text/html") 


from django.template import RequestContext

def registrar_email(request):

    if request.method == "POST":
         email = request.POST.get("email","")
         if email:
            c, criado = Contato.objects.get_or_create(email=email.strip())
            c.save()
      
         return render_to_response("newsletter/registre_email.html",{'assinou':True}, RequestContext(request))

    else:
        return render_to_response("newsletter/registre_email.html", RequestContext(request))


from django.core.mail import send_mail
from django.core.validators import validate_email
from lagarto.settings.local import EMAIL_DESTINO
def formreservas(request):
    nome = request.POST.get("nome","")
    jdata={}
    jdata["message"] = "Recebemos sua mensagem, em breve entramos em contato"
   
    try:
        email = request.POST.get("email","-").strip()
        validate_email(email)
    except:
        jdata['erro'] = True
        jdata['message'] = ""
        return HttpResponse(json.dumps(jdata), mimetype="application/json")

    telefone = request.POST.get("telefone","")
    data = request.POST.get("data","")
    suite = request.POST.get("suite","")
    periodo = request.POST.get("periodo","")
    message = "Pedido de reserva feito no site rabodolagarto.com.br:\n Nome: %s\n Telefone: %s \n Email: %s \n Data de nascimento: %s\n Suite: %s \n Periodo: %s \n " % (nome,telefone, email, data, suite, periodo)
    send_mail('[RESERVA]', message, "reservas@rabodolagarto.com.br" ,["reservas@rabodolagarto.com.br"], fail_silently=False)    

    try:
        contato = Contato.objects.get(email=email)
    except:
        contato = Contato(email=email, nome=nome, telefone=telefone, data_nascimento = data)
        contato.save()
    return HttpResponse(json.dumps(jdata), mimetype="application/json")


def formcontato(request):
    nome = request.POST.get("nome","")
    jdata={}
    jdata["message"] = "Recebemos sua mensagem, em breve entramos em contato"
   
    try:
        email = request.POST.get("email","-").strip()
        validate_email(email)
    except:
        jdata['erro'] = True
        jdata['message'] = ""
        return HttpResponse(json.dumps(jdata), mimetype="application/json")

    telefone = request.POST.get("telefone","")
    data = request.POST.get("data","")
    msg = request.POST.get("mensagem","")
    message = "CONTATO \n Nome: %s\n Telefone: %s \n Email: %s \n Data de nascimento: %s\n Mensagem: %s \n " % (nome,telefone, email, data, msg)
    send_mail('[CONTATO]', message, "contato@rabodolagarto.com.br" ,["contato@rabodolagarto.com.br",], fail_silently=False)    

    try:
        contato = Contato.objects.get(email=email)
    except:
        contato = Contato(email=email, nome=nome, telefone=telefone, data_nascimento = data)
        contato.save()
    return HttpResponse(json.dumps(jdata), mimetype="application/json")
