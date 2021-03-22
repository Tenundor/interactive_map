from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:place_id>/', views.place_api, name='place_api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

