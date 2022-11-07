from django.urls import path
from MiApp.views import showFamily

urlpatterns = [
    path('', showFamily)
]