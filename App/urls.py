from django.urls import path 
from django.conf.urls.static import static
from .views import home,categories,products,contact,products_of_category,promo_order,create_customer,order
from django.conf import settings

urlpatterns = [
    path("",home,name="home"),
    path("categories/",categories,name="categories"),
    path("products/",products,name="products"),
    path("contact/",contact,name="contact"),
    path("order/<int:pk>/",order,name="order"),
    path("promo_order/<int:pk>/",promo_order,name="promo_order"),
    path("products_of_category/<int:pk>/",products_of_category,name="products_of_category"),
    path("create_customer/<int:pk>/",create_customer,name="create_customer")


]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

