from django.db import models

class Series(models.Model):
	autor = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	logo = models.CharField(max_length=1000)

	# Defino o que irá retornar quando eu buscar no BD
	def __str__(self):
		return self.name + ' - ' + self.autor


class Episode(models.Model):
	series = models.ForeignKey(Series, on_delete=models.CASCADE)
	logo = models.CharField(max_length=1000)
	title = models.CharField(max_length=100)
	number = models.IntegerField(default=0)
	is_favorite = models.BooleanField(default=False)
	def __str__(self):
		return 'Episode ' + str(self.number) + ' - ' + self.title

class Link(models.Model):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	link = models.CharField(max_length=1000)
	def __str__(self):
		return self.link