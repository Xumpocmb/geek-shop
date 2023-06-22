from django.contrib import admin
from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    # readonly_fields = ('image')
    # ordering = ('name')
    search_fields = ('name',)


# для того чтобы в админке пользователя сразу отображалась его корзина
class BasketInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    # количество пустых полей корзины
    # extra = 0
