from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField("Ismi" , max_length = 35)
	email = models.EmailField("Emaili")
	subject = models.CharField("Mavzusi" , max_length = 150)
	message = models.TextField("Habar matni")
	date = models.DateTimeField("Sanasi" , auto_now_add = True)
	
	
	class Meta:
		# database name
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return "Bizga murojat qilgan bor : {0}".format(self.name)

class Article(models.Model):
	name = models.CharField("Nomi" , max_length = 35)
	like = models.PositiveIntegerField("Like", default = 0)
	seen = models.PositiveIntegerField("Seen" , default = 0)
	comment = models.PositiveIntegerField("Comment" , default = 0)
	share = models.PositiveIntegerField("Share" , default = 0)
	added = models.CharField("Qo'shdi" , max_length = 100)
	category = models.CharField("Mavzusi" , max_length = 150)
	text = models.TextField("Moqala matni")
	date = models.DateTimeField("Sanasi" , auto_now_add = True)

	class Meta:
		# database name
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'

	def __str__(self):
		return "Siz shuni qo'shdiz : {0}".format(self.name)
