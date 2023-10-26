from django.urls import path
from .views import (
    HomeListView , ShopListView,
    ProductDetailView , ContactListView,
)



urlpatterns = [
    path('' , HomeListView.as_view() , name='home'),
    path('product/shop/' , ShopListView.as_view() , name='shop'),
    path('contact/' , ContactListView.as_view() , name='contact'),
    path('shop/detail/<int:id>' , ProductDetailView.as_view() , name='proddetail')
]
