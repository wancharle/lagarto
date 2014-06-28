#! -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from paginas.models import Slider

class CapaView(TemplateView):
	template_name='lagarto/index.html'	

	def get_context_data(self, **context):
		context['sliders'] = Slider.objects.all() 
		return context
