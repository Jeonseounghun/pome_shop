from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'shopping'

urlpatterns = [
    path('', index, name='index'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<int:pk>/order_list/', order_list, name='order_list'),
    path('notice/', notice, name='notice'),
    path('notice/<int:pk>/', notice_detail, name='notice_detail'),
    path('show_category/<int:category_id>/', show_category, name='show_category'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
    path('cart_or_buy/<int:pk>/', cart_or_buy, name='cart_or_buy'),
    path('cart/<int:pk>/', cart, name='cart'),
    path('cart/<int:pk>/delete/', delete_cart, name='delete_cart'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='shop/index.html'), name='logout'),
    path('signup/', signup, name='signup'),
]
