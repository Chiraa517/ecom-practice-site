from django.contrib import admin
from .models import Contry, City, Area, Customer, Category, Product, Order, OrderStatus, Cart
# Register your models here.
admin.site.register(Contry)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Cart)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

    class Media:
        js = ("https://cdn.tiny.cloud/1/pvc4ir3y3m926ajbtvymmuia4120k3zo0k19dalsyuv591c3/tinymce/6/tinymce.min.js",
              "js/tinymce.js", )


admin.site.register(Product, ProductAdmin)