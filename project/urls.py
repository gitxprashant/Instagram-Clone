
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('googleRest/', include('googleRest.urls')),
    path('admin/', admin.site.urls),
]
