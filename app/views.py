from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self,request):
  beautyproducts = Product.objects.filter(category='B')
  skincare = Product.objects.filter(category='S')
  accessories = Product.objects.filter(category='A')
  perfumes = Product.objects.filter(category='P')
  haircare = Product.objects.filter(category='H')
  return render(request, 'app/home.html',
                   {'beautyproducts':beautyproducts, 'skincare':skincare, 'accessories':accessories,
                    'perfumes':perfumes, 'haircare':haircare})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',
  {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def makeup(request):
 return render(request, 'app/makeup.html')

def skincare(request):
 return render(request, 'app/skincare.html')

def accessories(request):
 return render(request, 'app/accessories.html')

def perfume(request):
 return render(request, 'app/perfume.html')

def haircare(request):
 return render(request, 'app/haircare.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
