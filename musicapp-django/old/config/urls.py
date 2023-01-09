
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # DEFAULT HOMEPAGE
    url(r'^', include_docs_urls(title='API')),

    #ADMIN URL ENDPOINT
    url(r'^admin/', admin.site.urls),

    #API URL ENDPOINT
    
    url(r'^api/', include('api.v1.music.urls')),
    url(r'^api/users', include('api.v1.account.urls')),


    #AUTHENTICATION URL ENDPOINT
    url(r'^auth/', include('django.contrib.auth.urls')),
    

    # DEFAULT PROJECT URL ENDPOIUNT
    url(r'^home/', include('project.homepage.urls')),
    url(r'^about/', include('project.aboutpage.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



