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

def makeup(request, data=None):
 if data == None:
  makeup = Product.objects.filter(category='M')
 elif data== 'Maybelline' or data== 'Elf':
  makeup = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  makeup= Product.objects.filter(category='M').filter(discounted_price__lt=1000)
 elif data == 'above':
  makeup= Product.objects.filter(category='M').filter(discounted_price__gt=1000)



 return render(request, 'app/makeup.html', {'makeup':makeup})

def skincare(request, data=None):
 if data == None:
  skincare = Product.objects.filter(category='S')
 elif data == 'Cetaphil' or data == 'Lotus':
  skincare = Product.objects.filter(category='S').filter(brand=data)
 elif data == 'below':
  skincare = Product.objects.filter(category='S').filter(discounted_price__lt=1000)
 elif data == 'above':
  skincare = Product.objects.filter(category='S').filter(discounted_price__gt=1000)


 return render(request, 'app/skincare.html', {'skincare':skincare})

def accessories(request, data=None):
 if data == None:
  accessories = Product.objects.filter(category='A')
 elif data == 'XoX' or data == 'MasalaBeads':
  accessories = Product.objects.filter(category='A').filter(brand=data)
 elif data == 'below':
  accessories = Product.objects.filter(category='A').filter(discounted_price__lt=1000)
 elif data == 'above':
  accessories = Product.objects.filter(category='A').filter(discounted_price__gt=1000)

 return render(request, 'app/accessories.html', {'accessories':accessories})

def perfume(request, data=None):
 if data == None:
  perfume = Product.objects.filter(category='P')
 elif data == 'VictoriasSecret' or data == 'Wottagirl':
  perfume = Product.objects.filter(category='P').filter(brand=data)
 elif data == 'below':
  perfume = Product.objects.filter(category='P').filter(discounted_price__lt=1000)
 elif data == 'above':
  perfume = Product.objects.filter(category='P').filter(discounted_price__gt=1000)

 return render(request, 'app/perfume.html', {'perfume':perfume})

def haircare(request, data=None):
 if data == None:
  haircare = Product.objects.filter(category='H')
 elif data == 'Tresemme' or data == 'Loreal':
  haircare = Product.objects.filter(category='H').filter(brand=data)
 elif data == 'below':
  haircare = Product.objects.filter(category='H').filter(discounted_price__lt=1000)
 elif data == 'above':
  haircare = Product.objects.filter(category='H').filter(discounted_price__gt=1000)

 return render(request, 'app/haircare.html', {'haircare':haircare})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
