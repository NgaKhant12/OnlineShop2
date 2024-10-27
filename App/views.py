from django.shortcuts import redirect, render
from .models import Category,Products,PromotionProducts,Order,Customer
from .forms import OrderForm,CustomerForm
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Products.objects.all()
    promotion_products = PromotionProducts.objects.all()
    count = products.count()

    context = {"categories":categories,"products":products,"count":count,'promotion_products':promotion_products}
    return render(request,"index.html",context)

def categories(request):
    categories = Category.objects.all()

    context = {"categories":categories}
    return render(request,"categories.html",context)

def products(request):
    products = Products.objects.all()

    context = {"products":products}
    return render(request,"products.html",context)

def contact(request):
    context = {}
    return render(request,"contact.html",context)

def create_customer(request,pk):
    product = Products.objects.get(id=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomerForm()
    context = {"product":product,"form":form}
    return render(request,"customer.html",context)

def products_of_category(request,pk):
    category = Category.objects.get(id= pk)
    products = Products.objects.filter(category=category)
    context = {"category":category,"products":products}
    return render(request,"products_of_category.html",context)


def promo_order(request,pk):
    
    product = PromotionProducts.objects.get(id=pk)


    context = {"product":product}
    return render(request,"order.html",context)

# def order(request,pk):

#     product = Products.objects.get(id=pk)
#     print(product)
#     print(request.method)
#     '''if request.method == 'POST':
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         address = request.POST.get("address")

        

#     else:
#         print(request.method)'''
    
#     if request.method == "POST":
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             customer = form.save()
#             quantity = int(request.POST.get("quantity", 1)) 
#             total_price = quantity * product.price

#             Order.objects.create(
#                 customer = customer,
#                 product = product,
#                 quantity = quantity,
#                 total_price = total_price
#             )
#             return redirect("/")
#     else:
#         form= CustomerForm()   
#     context = {"product":product,"form":form}
#     return render(request,"order.html",context)


def order(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()  # Customer ကို save လုပ်ပြီး customer object ရယူ
            quantity = int(request.POST.get("quantity", 1))  # Quantity ကို POST မှတဆင့်ရယူ
            total_price = product.price * quantity  # စုစုပေါင်းတန်ဖိုး

            # Order ကိုသိမ်းမည်
            Order.objects.create(
                customer=customer,
                product=product,
                quantity=quantity,
                total_price=total_price
            )

            return redirect("/")  # အောင်မြင်ခဲ့လျှင် မူလစာမျက်နှာသို့ ပြန်သွားမည်
    else:
        form = CustomerForm()

    context = {
        "product": product,
        "form": form,
    }
    return render(request, "order.html", context)