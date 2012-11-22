# -*- coding: utf-8 -*-
from django.db import models


class Campanha(models.Model):
    servidor = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    arquivo_dados = models.FileField(upload_to="dados/",null=True,blank=True)

    def __unicode__(self):
	return u"%s"% self.servidor
    
    def importar(self):
        f = open(self.arquivo_dados.path)
        texto = f.read()
        f.close()
        for email in texto.split("\n"):
            c, criado = Contato.objects.get_or_create(email=email.strip())
            c.save()
        
class ContatoTeste(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    ativo = models.BooleanField(default=True)
    erro = models.BooleanField(default=False)
    def __unicode__(self):
        return u"%s" % self.email
    
    class Meta:
        verbose_name_plural= "Contatos de teste"
        verbose_name = "Contato de teste"

class Contato(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    nome =  models.CharField(max_length=200,null=True, blank= True)
    data_nascimento =  models.CharField(max_length=30,null=True, blank= True)
    telefone =  models.CharField(max_length=30,null=True, blank= True)

    ativo = models.BooleanField(default=True)
    erro = models.BooleanField(default=False,verbose_name=u"possui erro?") 

    def __unicode__(self):
        return u"%s"% self.email

estados = (
	('0','esperando para enviar'),
	('1','enviando'),
	('2','envio completo'),
)

class Mensagem(models.Model):
    campanha = models.ForeignKey(Campanha)
    email_from = models.CharField(max_length=200,default=u"'MAX DA MATA' <vereador@maxdamata.com.br>")
    email_responder_para = models.EmailField(max_length=200,default=u"bancodedados@maxdamata.com.br")
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    mensagem_texto_alternativo= models.TextField()
    imagem = models.ImageField(upload_to="propaganda/")    
    emails_enviados = models.ManyToManyField(Contato,verbose_name=u"destinatários") 
    estado = models.CharField(max_length=2,choices=estados,default='0') # trava de seguranca
    cancelamentos = models.IntegerField(default=0)
    problemas = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" % self.assunto

    def emails_ja_enviados(self):
        return u"%d" % self.emails_enviados.count()
    
    def assinaturas_canceladas(self): 
        n = Contato.objects.filter(ativo=False).count()
        if n > 0:
            return u"<a href='/newsletter/exporta/contatos/cancelados/'>%d cancelamentos</a>" % n
        else:
            return u"nenhuma"
    assinaturas_canceladas.allow_tags = True 

    def emails_com_problema(self):
        n= Contato.objects.filter(erro=True).count()
        if n>0:
            return u"<a href='/newsletter/exporta/comerro/'>%d emails</a>" % n
        else:
            return u"nenhum"
    emails_com_problema.allow_tags = True
    
 
