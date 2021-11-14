from django.urls import path
from . import views

app_name = 'trials'

urlpatterns = [
    path('', views.index, name='index'),    
    path('user_login', views.user_login, name='user_login'),
    path("<str:trialName>", views.get_trial, name="trialName"),        
    path('register/', views.register, name='register'),
    path('addTrial/', views.addtrial, name='addtrial'),    
    path('logout/', views.user_logout, name='logout'),
    # path('ajax/load_cancers/', views.load_cancer_type, name='ajax_load_cancer_type'),        
]