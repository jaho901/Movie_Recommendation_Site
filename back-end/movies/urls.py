from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('recent/', views.movie_list_recent),
    path('<int:movie_id>/', views.movie_detail),
]
