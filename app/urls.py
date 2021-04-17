from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(),
         name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart,name='showcart'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
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

    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',
                                                        authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                  form_class=MyPasswordChangeForm,
                                                                  success_url='/passwordchangedone/'),
         name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeView.
         as_view(template_name='app/passwordchangedone.html'),
         name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                    form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('checkout/', views.checkout, name='checkout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
