from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:song_id>/', views.song_view, name='song_view'),
    path('pick/', views.pick, name='pick'),
]
