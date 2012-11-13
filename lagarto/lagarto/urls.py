from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/index.html'}, name='home'),
    url(r'^pousada/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/pousada.html'}, name='pousada'),
    url(r'^estrutura/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/estrutura.html'}, name='estrutura'),
    url(r'^suites/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/suites.html'}, name='suites'),
    url(r'^localizacao/$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/localizacao.html'}, name='localizacao'),

    # url(r'^admin/', include(admin.site.urls)),
)

# urls estaticas funcionam apenas no em modo DEBUG
urlpatterns += staticfiles_urlpatterns()

