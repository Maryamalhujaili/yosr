from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('grade/<int:pk>/', views.grade_detail, name='grade'),
    path('search/', views.search, name='search'),
    path('subject/<int:pk>/', views.subject_detail, name='subject'),
]