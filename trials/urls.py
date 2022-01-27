from django.urls import path
from . import views

app_name = 'trials'

urlpatterns = [
    path('', views.index, name='index'),    
    path('user_login', views.user_login, name='user_login'),
    path('csv_upload', views.csv_upload, name='csv_upload'),
    path("update/<str:id>", views.trial_update, name="update/id"),
    path("<str:id>", views.get_trial, name="id"),        
    path('register/', views.register, name='register'),
    path('addTrial/', views.addtrial, name='addtrial'),    
    path('logout/', views.user_logout, name='logout'),
    path('ajax/load_cancers/', views.load_cancer_type, name='ajax_load_cancer_type'),
    path('cancerTypes/', views.cancerTypesListView.as_view(), name='cancerTypes'),
    path('cancerTypes/<str:id>', views.cancerTypesDetailView.as_view(), name='cancerTypes/id'),
    path('newTypes/', views.cancerTypesCreateView.as_view(), name='newType'),            
]