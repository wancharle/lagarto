from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/index.html'}, name='home'),
    url(r'^pousada/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/pousada.html'}, name='pousada'),
    url(r'^estrutura/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/estrutura.html'}, name='estrutura'),
    url(r'^suites/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/suites.html'}, name='suites'),
    url(r'^localizacao/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/localizacao.html'}, name='localizacao'),

    (r'^newsletter/cancela/(\d+)/(\d+)/$','newsletter.views.cancela_newsletter'),  
    (r'^newsletter/exporta/comerro/$','newsletter.views.exportar_nao_enviados'),
    (r'^newsletter/exporta/contatos/(\w+)/$','newsletter.views.exportar_contatos'),
    (r'^newsletter/view/(\d+)/$','newsletter.views.ver_mensagem'),
    (r'^registre_email/$','newsletter.views.registrar_email'),
    (r'^formreservas/$','newsletter.views.formreservas'),
    (r'^formcontato/$','newsletter.views.formcontato'),
     url(r'^admin/', include(admin.site.urls)),
)

# urls estaticas funcionam apenas no em modo DEBUG
urlpatterns += staticfiles_urlpatterns()

