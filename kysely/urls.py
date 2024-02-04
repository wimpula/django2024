from django.urls import path

from . import views


urlpatterns = [
    # ex: /kyselyt/
    path("", views.index, name="index"),
    
    # ex: /kyselyt/5/
    path("<int:question_id>/", views.yksityiskohdat, name="yksityiskohdat"),
    # ex: /kyselyt/5/results/
    path("<int:question_id>/tulokset/", views.tulokset, name="tulokset"),
    # ex: /kyselyt/5/vote/
    path("<int:question_id>/äänestä/", views.äänestä, name="äänestä"),
]
