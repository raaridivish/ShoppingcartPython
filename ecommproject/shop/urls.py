from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.allPrdctCtgry, name="allPrdctCtgry"),
    path('<slug:c_slug>/', views.allPrdctCtgry, name="products_by_category"),
    path('<slug:c_slug>/<slug:p_slug>/', views.prodDetail, name="prodCtgryDetail"),
]
