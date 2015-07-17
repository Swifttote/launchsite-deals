from django.conf.urls import patterns,url
from signup import views
urlpatterns = [
	url(r'^$',views.index, name = "index"),
	url(r'^index/',views.index, name = "index"),
	
]