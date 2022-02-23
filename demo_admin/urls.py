from . import views
from django.urls import path

app_name = 'demo_admin'
urlpatterns = [
    path('',views.signIn, name='signIn'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-item/', views.addItem, name='addItem'),
    path('save-item/', views.saveItem, name='saveItem'),
    path('successful-biddings/', views.viewBiddings, name='viewBiddings'),
    ]