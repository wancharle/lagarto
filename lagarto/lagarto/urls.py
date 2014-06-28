from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', TemplateView.as_view(template_name='lagarto/index.html'), name='home'),
    url(r'^pousada/$', TemplateView.as_view(template_name='lagarto/pousada.html'), name='pousada'),
    url(r'^estrutura/$',TemplateView.as_view(template_name='lagarto/estrutura.html'), name='estrutura'),
    url(r'^suites/$', TemplateView.as_view(template_name='lagarto/suites.html'), name='suites'),
    url(r'^localizacao/$', TemplateView.as_view(template_name='lagarto/localizacao.html'), name='localizacao'),

   (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^newsletter/cancela/(\d+)/(\d+)/$','newsletter.views.cancela_newsletter'),  
    (r'^newsletter/exporta/comerro/$','newsletter.views.exportar_nao_enviados'),
    (r'^newsletter/exporta/contatos/(\w+)/$','newsletter.views.exportar_contatos'),
    (r'^newsletter/view/(\d+)/$','newsletter.views.ver_mensagem'),
    (r'^cron.php$','cron_job.executa_cron'),
    (r'^registre_email/$','newsletter.views.registrar_email'),
    (r'^formreservas/$','newsletter.views.formreservas'),
    (r'^formcontato/$','newsletter.views.formcontato'),
     url(r'^admin/', include(admin.site.urls)),
)

# urls estaticas funcionam apenas no em modo DEBUG
urlpatterns += staticfiles_urlpatterns()

