from django.shortcuts import render, get_object_or_404
from .models import Series

def index(request):
	all_series = Series.objects.all()
	return render(request, 'video/index.html', {'all_series': all_series})

def detail(request, series_id):
	series = get_object_or_404(Series, pk=series_id)
	return render(request, 'video/detail.html', {'series': series})

def favorite(request, series_id):
	series = get_object_or_404(Series, pk=series_id)
	try:
		selected_episode = series.episode_set.get(pk = request.POST['episode'])
	except (KeyError, Episode.DoesNotExist):
		return render(request, 'video/detail.html', {
			'series': series,
			'error_message': "You didn't select a valid episode",
			})
	else:
		selected_episode.is_favorite = True
		selected_episode.save()
		return render(request, 'video/detail.html', {'series': series})