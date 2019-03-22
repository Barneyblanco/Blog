from django.db import models
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	image = models.FileField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def get_absolute_url(self):
		return reverse('forum:detail', kwargs={'pk': self.pk})


	def __str__(self):
		return self.title

	