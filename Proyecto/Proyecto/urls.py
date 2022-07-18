
from django.contrib import admin
from django.urls import path, include
from Cafes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cafes/', include('Cafes.urls')),
]
