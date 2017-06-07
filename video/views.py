from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Series
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = "video/index.html"
	context_object_name = 'all_series'

	def get_queryset(self):
		return Series.objects.all()

class DetailView(generic.DetailView):
	model = Series
	template_name = "video/detail.html"

class SeriesCreate(CreateView):
	model = Series
	fields = ['autor', 'name', 'genre', 'logo']

class SeriesUpdate(UpdateView):
	model = Series
	fields = ['autor', 'name', 'genre', 'logo']

class SeriesDelete(DeleteView):
	model = Series
	sucess_url = reverse_lazy()

class UserFormView(View):
	form_class = UserForm
	template_name = "video/registration_form.html"

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()