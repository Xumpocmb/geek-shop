from django.contrib import admin
from users.models import User
from products.admin import BasketInline

# для того чтобы в админке пользователя сразу отображалась его корзина
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketInline,)
