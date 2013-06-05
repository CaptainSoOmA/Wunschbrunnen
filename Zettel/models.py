from django.db import models

# Create your models here.


class BibInfo(models.Model):

	# infos about Bibliographie
	author    = models.CharField(max_length=60)
	title     = models.CharField(max_length=60)
	journal   = models.CharField(max_length=60)

	page_from 	= models.IntegerField()
	page_to   	= models.IntegerField()

	year      = models.IntegerField()

	


class Zettel(models.Model):
	pub_date 	= models.DateTimeField('date published')

	headline 	= models.CharField(max_length=60)
	text 		= models.TextField()

	bib 		= models.ManyToManyField(BibInfo)

	# --- meta Infos


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    