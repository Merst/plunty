from django.urls import path
from . import views

urlpatterns = [
    path('', views.AttemptListView.as_view(), name='attempts'),
]
