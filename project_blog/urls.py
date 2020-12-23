from django.contrib import admin

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

    path("", views.project_index, name="project_index"),

    path("<int:pk>/", views.project_detail, name="project_detail"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)