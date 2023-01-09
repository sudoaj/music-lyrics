
# from django.conf.urls import urls
from django.urls import include, re_path
from . import views 
from rest_framework import routers 
# from django.conf import settings
# from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'songs', views.SongView),
router.register(r'artiste', views.ArtisteView),



urlpatterns = [
    re_path(r'^', include(router.urls)),
]