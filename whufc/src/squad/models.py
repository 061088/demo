from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

def download_media_location(instance, filename):

	"""
	Sets the downoad location for files

	Args:
		instance(e.g.ClassTeacherName:mrobson)
		filename(mrobson.jpg)

	Returns:
		instance.slug/filename
		e.g. mrobson/mrobson.jpg
	"""

	return "squad/%s" %(filename)


POSITIONS = (
	('Goalkeeper','Goalkeeper'),
	('Defender','Defender'),
	('Midfielder','Midfielder'),
	('Forward','Forward'),
)

# Create your models here.
class SquadMember(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	image = models.ImageField(blank=True,null=True)
	nationality = models.CharField(max_length=255)
	flag = models.ImageField(blank=True,null=True)
	number = models.PositiveIntegerField()
	position = models.CharField(choices=POSITIONS, max_length=255)
	appearances = models.PositiveIntegerField()
	minutes = models.PositiveIntegerField()
	goals = models.PositiveIntegerField()
	assists = models.PositiveIntegerField()
	yellow_cards = models.PositiveIntegerField()
	red_cards = models.PositiveIntegerField()
	shots_per_game = models.DecimalField(max_digits=5, decimal_places=2)
	key_passes = models.DecimalField(max_digits=5, decimal_places=2)
	rating = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return self.name

	def get_api_url(self, request=None):
		return api_reverse('squad_api:detail', kwargs={'slug':self.slug}, request=request)
