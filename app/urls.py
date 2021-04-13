from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(),
         name='product-detail'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),

    path('makeup/', views.makeup, name='makeup'),
    path('makeup/<slug:data>', views.makeup, name='makeupdata'),

    path('skincare', views.skincare, name='skincare'),
    path('skincare/<slug:data>', views.skincare, name='skincaredata'),

    path('accessories', views.accessories, name='accessories'),
    path('accessories/<slug:data>', views.accessories, name='accessoriesdata'),

    path('perfume', views.perfume, name='perfume'),
    path('perfume/<slug:data>', views.perfume, name='perfumedata'),

    path('haircare', views.haircare, name='haircare'),
    path('haircare/<slug:data>', views.haircare, name='haircaredata'),

    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
