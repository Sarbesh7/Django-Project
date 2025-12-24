
from django.contrib import admin
from django.urls import path
from django.urls import include
from app import urls as app_urls
# from app import views as app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', app_views.home, name='home'),
    path('', include(app_urls)),
  
]
