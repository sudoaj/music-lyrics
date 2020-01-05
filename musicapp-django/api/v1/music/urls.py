
# from django.conf.urls import urls
from django.conf.urls import url, include
from . import views 
from rest_framework import routers 
# from django.conf import settings
# from django.conf.urls.static import static




router = routers.DefaultRouter()
router.register(r'songs', views.SongView),
router.register(r'artiste', views.ArtisteView),



urlpatterns = [
    url(r'^', include(router.urls)),
]