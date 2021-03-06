from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  item_already_in_cart = False
  if request.user.is_authenticated:
   item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
  return render(request, 'app/productdetail.html',
  {'product':product,
   'item_already_in_cart': item_already_in_cart})

@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

@login_required
def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  # print(cart)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user ==
                  user]
  # print(cart_product)
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount = amount + shipping_amount
   return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
  else:
   return render(request, 'app/emptycart.html')

def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount

    data = {
      'quantity': c.quantity,
      'amount' : amount,
      'totalamount': amount + shipping_amount}
    return JsonResponse(data)


def minus_cart(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity -= 1
  c.save()
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user ==
                  request.user]
  for p in cart_product:
   tempamount = (p.quantity * p.product.discounted_price)
   amount += tempamount
  data = {

   'quantity': c.quantity,
   'amount': amount,
   'totalamount': amount + shipping_amount
  }
  return JsonResponse(data)

def remove_cart(request):
 if request.method == 'GET':
  prod_id = request.GET['prod_id']
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

  c.delete()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount

  data = {
   'amount': amount,
   'totalamount': amount+ shipping_amount}
  return JsonResponse(data)


def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html', {'order_placed':op})


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

class CustomerRegistrationView(View):
 def get(self,request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html',{'form':form})

 def post(self,request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registration Successful')
   form.save()
  return render(request, 'app/customerregistration.html',{'form': form})

@login_required
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user)
 cart_items = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.0
 totalamount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product:
  for p in cart_product:
   tempamount = (p.quantity * p.product.discounted_price)
   amount = tempamount
  totalamount = amount + shipping_amount
 return render(request, 'app/checkout.html', {'add':add, 'totalamount': totalamount, 'cart_items':cart_items})

@login_required
def payment_done(request):
 user = request.user
 custid = request.GET.get('custid')
 customer = Customer.objects.get(id=custid)
 cart = Cart.objects.filter(user=user)
 for c in cart:
  OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
  c.delete()
 return redirect("orders")

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(self, request):
  totalitem = 0
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
  form = CustomerProfileForm()
  return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})

 def post(self, request):
  totalitem = 0
  if request.user.is_authenticated:
   totalitem = len(Cart.objects.filter(user=request.user))
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
   usr = request.user
   name = form.cleaned_data['name']
   locality = form.cleaned_data['locality']
   city = form.cleaned_data['city']
   state = form.cleaned_data['state']
   zipcode = form.cleaned_data['zipcode']
   reg = Customer(user=usr, name=name, locality=locality,
                  city=city, state=state, zipcode=zipcode)
   reg.save()
   messages.success(
    request, 'Congratulations!! Profile Updated Successfully')
  return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'totalitem': totalitem})
