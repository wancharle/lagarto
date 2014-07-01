#! -*- coding: utf-8 -*-
from django.db import models

from image_cropping import ImageRatioField

class Slider(models.Model):
    foto = models.ImageField(upload_to=u"slide/", help_text=u"imagens com proporção 5x2. Exemplo: 1440px X 564px")
    cropping = ImageRatioField('foto', '1440x564')

    legenda = models.CharField(max_length=100)
    legenda_em_ingles = models.CharField(max_length=100,verbose_name=u"legenda em inglês")

    url = models.CharField(max_length=100, db_index=True,null=True,blank=False)
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ('ordem',)

    def get_link_attrs(self):
        if self.url.startswith("http"):
            return u" target=\'_blank' href='%s' " % self.url
        else:
            return u" href='%s' " % self.url

    def __unicode__(self):
        return u"%s" % self.url
