from django.urls import path
from . import views
app_name = 'tours'

urlpatterns = [
    path('', views.TourList.as_view(), name='tour_list'),
    path('<int:pk>-<str:slug>/', views.TourDetail.as_view(), name='tour_detail'),
]