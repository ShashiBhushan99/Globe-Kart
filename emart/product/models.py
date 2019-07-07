from django.db import models
from django.utils import timezone
# Create your models here.
class product(models.Model):
	ProductName = models.CharField(max_length=100)
	BrandName = models.CharField(max_length=100)
	ModelNo = models.CharField(max_length=100)
	description = models.TextField()
	Quantity = models.CharField(max_length=100)
	Type = models.CharField(max_length=100)
	ItemWeight = models.IntegerField(max_length=100)
	Size = models.CharField(max_length=100)
	Wattage = models.CharField(max_length=100)
	ProductColor = models.CharField(max_length=100)
	StandardPrice = models.CharField(max_length=100)
	GST = models.CharField(max_length=100)
	Total = models.CharField(max_length=100)
	ProductImage = models.ImageField(upload_to='images',null=True)
	
	def __str__(self):
		return str(self.ProductImage)
	