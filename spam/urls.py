from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track_click, name='track_click'),
    path('submit-code/', views.submit_code, name='submit_code'),
    path('submissions/', views.view_submissions, name='view_submissions'),
    path('visits/', views.view_visits, name='view_visits'),
    path('login/', views.login_view, name='login'),

]