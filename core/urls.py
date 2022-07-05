from django.urls import path
from . import views

urlpatterns = [
    path('testing/<int:id>/<str:name>', views.testing),
    path('', views.home),
    path('another', views.Another.as_view())
]
