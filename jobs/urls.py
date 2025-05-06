from django.urls import path
from . import views

urlpatterns = [
    path('job_form/', views.job_application, name='job_application'),  # URL for job application form
    path('job_success/', views.job_success_view, name='job_success'),  # URL for job success page
    path('', views.home, name='home'),  # URL for home page (index.html)
    path('menu/', views.menu, name='menu'),  # URL for menu page (menu.html)
    path('music/', views.music, name='music'),  # URL for music page (music.html)
]
