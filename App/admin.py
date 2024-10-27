from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(PromotionProducts)
admin.site.register(Customer)
admin.site.register(Order)



