from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('style/', views.result, name='style'),
]

