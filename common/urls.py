from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('',views.index, name="index"),
    path('login/', views.signIn, name='signIn'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bid-now/<item_id>', views.bidNow, name='bidNow'),
    path('save-bid/', views.saveBid, name='saveBid'),
]