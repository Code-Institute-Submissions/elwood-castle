from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.user_home, name="user_home"),
    path('update/', views.update_user_details, name="update_details"),
    path('order-summary/<order_number>',
         views.order_summary, name="order_summary")
]
