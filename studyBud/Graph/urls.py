from django.urls import path
from . import views
from .views import getStudent, printProfile

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", printProfile),
    path('<int:id>/', getStudent)
]
