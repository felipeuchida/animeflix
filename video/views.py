from django.views import generic
from .models import Series

class IndexView(generic.ListView):
	template_name = "video/index.html"
	context_object_name = 'all_series'

	def get_queryset(self):
		return Series.objects.all()

class DetailView(generic.DetailView):
	model = Series
	template_name = "video/detail.html"
