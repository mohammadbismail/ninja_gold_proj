from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("find_gold_farm/", views.find_gold_farm),
    path("find_gold_cave/", views.find_gold_cave),
    path("find_gold_house/", views.find_gold_house),
    path("find-gold-quest/", views.find_gold_quest),
]
