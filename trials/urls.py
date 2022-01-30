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
    path('cancerTypes/<int:pk>', views.cancerTypesDetailView.as_view(), name="cancerTypesDetails"),
    path('cancerTypes/update/<int:pk>', views.cancerTypesUpdateView.as_view(), name="cancerTypesUpdate"),
    path('cancerTypes/delete/<int:pk>', views.cancerTypesDeleteView.as_view(), name="cancerTypesDelete"),
    path('newTypes/', views.cancerTypesCreateView.as_view(), name='newType'),
    path('triallead/', views.trial_leadListView.as_view(), name='trial_lead'),
    path('triallead/<int:pk>', views.trial_leadDetailView.as_view(), name="trial_leadDetails"),
    path('triallead/update/<int:pk>', views.trial_leadUpdateView.as_view(), name="trial_leadUpdate"),
    path('triallead/delete/<int:pk>', views.trial_leadDeleteView.as_view(), name="trial_leadDelete"),
    path('newlead/', views.trial_leadCreateView.as_view(), name='newlead'),             
]