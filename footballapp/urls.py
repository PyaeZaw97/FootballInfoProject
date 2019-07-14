from django.urls import path
from footballapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('player/', views.PlayerList.as_view()),
    path('player/<int:pk>/', views.PlayerDetail.as_view()),
    path('team/', views.TeamList.as_view()),
    path('team/<int:pk>/', views.TeamDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)