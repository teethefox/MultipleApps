from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.blogs_app.urls')),    
    url(r'^blogs/', include('apps.blogs_app.urls')),
    url(r'^surveys/', include('apps.surveys_app.urls')),
    url(r'^users/', include('apps.users_app.urls'))
]
