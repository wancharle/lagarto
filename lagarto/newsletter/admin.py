from django.contrib import admin
from django.http import HttpResponseRedirect
from newsletter.models import Campanha, Mensagem, Contato, ContatoTeste

from newsletter.email_com_imagem import enviar_email

class CampanhaAdmin(admin.ModelAdmin):
    actions = ['importar_contatos','exportar_contatos','exportar_contatos_cancelados','exportar_contatos_com_problema']
    list_display = [ 'login','servidor']
    def importar_contatos(self,request,queryset):
        for q in queryset:
            q.importar()
    def exportar_contatos(self,request,queryset):
        return HttpResponseRedirect("/newsletter/exporta/contatos/ativos/")

    def exportar_contatos_cancelados(self,request,queryset):
         return HttpResponseRedirect("/newsletter/exporta/contatos/cancelados/")
    def exportar_contatos_com_problema(self,request, queryset):
         return HttpResponseRedirect("/newsletter/exporta/comerro/")


class MensagemAdmin(admin.ModelAdmin):
    exclude= ('emails_enviados','email_responder_para','cancelamentos','problemas','email_from') 
    actions = ('zerar_emails_enviados','testar_mensagem_com_contatos_de_teste')
    list_display = ('assunto','estado','emails_ja_enviados','emails_com_problema','cancelamentos')
    list_per_page = 20
    def zerar_emails_enviados(self,request,queryset):
        for q in queryset:
            q.emails_enviados.clear()
            q.save()

    def testar_mensagem_com_contatos_de_teste(self,request,queryset):
        contacts = ContatoTeste.objects.all()
        for msg in queryset:
            for c in contacts:
                r=enviar_email(msg, c,msg.campanha.servidor,
                    msg.campanha.login,msg.campanha.senha )

class ContatoAdmin(admin.ModelAdmin):
    list_filter=('ativo','erro')
    list_display=('nome','email','telefone','data_nascimento','ativo','erro')
    search_fields=('email',)

admin.site.register(Campanha,CampanhaAdmin)
admin.site.register(Mensagem,MensagemAdmin)
admin.site.register(Contato,ContatoAdmin)
admin.site.register(ContatoTeste)
