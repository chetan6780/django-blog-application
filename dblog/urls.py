from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include("articles.urls")),
    path('', views.homepage),
    path('about/', views.about),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)