from django.urls import path
from RestApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name='hm'),
	path('abt/',views.about,name='ab'),	
	path('cntct/',views.contact,name='ct'),
	path('login/',views.login,name='ln'),
	path('rlist/',views.restlist,name="rstl"),
	path('rstup/<int:m>/',views.rstup,name='rsup'),
	path('dd/<int:s>/',views.rstdl,name='rsdl'),
	path('rstviw/<int:a>/',views.rstvw,name="rsvw"),
	path('litem/',views.litem,name="item1"),
	path('ld/<int:s>/',views.litdl,name='ldel'),
	path('rstviw1/<int:a>/',views.rstvw1,name="rsvw1"),
	path('rstup1/<int:m>/',views.rstup1,name='rsup1'),
	path('rg/',views.usrreg,name="reg"),
	path('login1/',v.LoginView.as_view(template_name="app/login1.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="app/logout.html"),name="lgo"),
]