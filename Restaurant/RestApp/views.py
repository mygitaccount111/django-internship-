from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.forms import itemform,UsgForm
from RestApp.models import Restaurant
from RestApp.models import itemlist
from django.contrib import messages
from django.contrib.auth.decorators import login_required  

# Create your views here.


def home(r):
	return render(r,'app/home.html')
def about(r):
	w=Restaurant.objects.filter(uid_id=r.user.id)
	return render(r,'app/about.html',{'c':w})
def contact(r):
	return render(r,'app/contact.html')

def login(r):
	return render(r,'app/login.html')

@login_required
def restlist(r):
	y=Restaurant.objects.filter(uid_id=r.user.id)
	if r.method=="POST":
		t=ReForm(r.POST,r.FILES)
		if t.is_valid():
			c=t.save(commit=False)
			c.uid_id=r.user.id
			c.save()
			messages.success(r,"restarent added sucessfully")
			return redirect('/rlist')
	t=ReForm()
	return render(r,'app/restaurantlist.html',{'q':t,'a':y})

def rstup(r,m):
	k=Restaurant.objects.get(id=m)
	if r.method=="POST":
		e=ReForm(r.POST,r.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(r,"{} restarent updated sucessfully".format(k.rname))
			return redirect('/rlist')
	e=ReForm(instance=k)
	return render(r,'app/restupdate.html',{'x':e})

def rstdl(r,s):
	g=Restaurant.objects.get(id=s)
	if r.method=="POST":
		messages.info(r,"{} restarent deleted sucessfully".format(g.rname))
		g.delete()
		return redirect('/rlist')
	return render(r,'app/restdelete.html',{'i':g})

def rstvw(r,a):
	s=Restaurant.objects.get(id=a)
	return render(r,"app/restview.html",{'z':s})


def litem(r):
	y=itemlist.objects.all()
	if r.method=="POST":
		t=itemform(r.POST,r.FILES)
		if t.is_valid():
			t.save()
			return redirect('/litem')
	t=itemform()
	return render(r,'app/listitems.html',{'q':t,'a':y})


def litdl(r,s):
	g=itemlist.objects.get(id=s)
	if r.method=="POST":
		messages.info(r,"{} item deleted sucessfully".format(g.iname))
		g.delete()
		return redirect('/litem')
	return render(r,'app/listdelete.html',{'i':g})


def rstvw1(r,a):
	s=itemlist.objects.get(id=a)
	return render(r,"app/restview1.html",{'z':s})


def rstup1(r,m):
	k=itemlist.objects.get(id=m)
	if r.method=="POST":
		e=itemform(r.POST,r.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(r,"{} item updated sucessfully".format(k.iname))
			return redirect('/litem')
	e=itemform(instance=k)
	return render(r,'app/restupdate1.html',{'x':e})


def usrreg(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login1')
	
	d=UsgForm()
	return render(request,'app/usrregister.html',{'t':d})
