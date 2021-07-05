#from django.forms import ModelForm
from RestApp.models import Restaurant
from RestApp.models import itemlist
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReForm(forms.ModelForm):
	class Meta:
		model=Restaurant
		fields=['rname','nitems','timings','rsimg','address']
		widgets={
		"rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items Available in Restaurant",
			}),
		'timings':forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Timings",
			"type":"time"
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":5,
			}),
		}

class itemform(forms.ModelForm):
	class Meta:
		model=itemlist
		fields=['rsid','iname','icategory','iprice','itavailability','iimg']
		widgets={
		"rsid":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Select Restarent",
			}),
		"iname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter item name",
			}),
		"icategory":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Item",
			}),
		"iprice":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter price",
			}),
		"itavailability":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		

		
		}


class UsgForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2",
		"placeholder":"Enter Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2",
		"placeholder":"Confirm Password",
		}))
	
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter UserName",
			}),
		}
