from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Restaurant(models.Model):
	rname=models.CharField(max_length=30)
	nitems=models.IntegerField()
	timings=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	rsimg=models.ImageField(upload_to='Restaurantimages/',default='logo.jpg')
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return (self.rname);


class itemlist(models.Model):
	y=[('NV','non-veg'),('VG','veg')]
	p=[('AV','Available'),('NA','Not available'),('s1','Select Availability')]
	iname=models.CharField(max_length=30)
	icategory=models.CharField(choices=y,default="Df",max_length=12)
	iprice=models.IntegerField()
	iimg=models.ImageField(upload_to='Itemimages',default='logo.jpg')
	itavailability=models.CharField(choices=p,default="s1",max_length=20)
	rsid=models.ForeignKey(Restaurant,on_delete=models.CASCADE)