from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

app_name="recommendation"

# router = DefaultRouter()
# router.register('', views.MovieListViewSet)

urlpatterns = [
    # path('recommend_by_day_of_week/', views.MovieRecommendByDayViewSet.as_view({'get': 'list'})),
]