from django.conf.urls import url #This gives us access to the function url
from . import views              # This explicitly imports views.py in the current folder.
  
urlpatterns = [
    url(r'^$', views.index)     # This line has changed!
]