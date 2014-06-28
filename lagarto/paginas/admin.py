from django.contrib import admin
from image_cropping import ImageCroppingMixin
from easy_thumbnails.files import get_thumbnailer
from paginas.models import Slider 

class SliderAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display = ('url','ordem','legenda','legenda_em_ingles','imagem')

    def imagem(self,obj):
        thumbnail_url = get_thumbnailer(obj.foto).get_thumbnail({
            'size': (250, 100),
            'box': obj.cropping,
            'crop': True,
            'detail': True,
        }).url

        return u"<img src='%s'>" % thumbnail_url
    imagem.allow_tags=True
    imagem.short_description= "foto"


admin.site.register(Slider, SliderAdmin)
