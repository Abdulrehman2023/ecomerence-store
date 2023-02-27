from django.urls import path 
from store import views


urlpatterns = [
    path('',views.store , name= "store"),
    
    path('checkout/', views.checkout.as_view(), name="checkout"),
    
    path('specs/', views.specs, name="specs"),  
    path('product_upload/', views.product_upload, name="product_upload"),
    path('home_view/', views.home_view, name="home_view"),
    
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('stock/', views.stock, name="stock"),
    path('stock/', views.stock, name="stock"),
    path('Contact_us/', views.Contact_us.as_view(), name = 'Contact_us'),
    path('cart/', views.cart.as_view(), name="cart"),
    path("AddToCart/<int:pk>/", views.AddToCart.as_view(), name="AddToCart"),

    
    




]
