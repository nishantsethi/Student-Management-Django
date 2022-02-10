from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    path('allchildrens', views.viewChildred, name='all-children'),
    path('childFees/<str:pk>/', views.childFees, name='child-fees'),
    path('allFees', views.allFees.as_view(), name='all-fees'),
    path('pendingFees', views.pendingFees, name= 'pending-fees')
]