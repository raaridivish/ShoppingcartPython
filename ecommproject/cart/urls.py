from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/', views.addCart, name="addCart"),
    path('', views.cartDetail, name="cartDetail"),
    path('remove/<int:product_id>/', views.removeCart, name='removeCart'),
    path('delete/<int:product_id>/', views.delCart, name='delCart'),
]
