from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'django.views.generic.simple.direct_to_template',{'template':'lagarto/index.html'}, name='home'),

    # url(r'^admin/', include(admin.site.urls)),
)

# urls estaticas funcionam apenas no em modo DEBUG
urlpatterns += staticfiles_urlpatterns()

