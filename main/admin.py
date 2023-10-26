from django.contrib import admin
from .models import *

@admin.register(Game)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'price' , 'discount')
    list_display_links = ('id' , 'name' , 'price' , 'discount')
    search_fields = ('id' , 'name' , 'price' , 'discount' , 'gameID' , 'multi_tags' , 'genre' ,'about' )

admin.site.register(Category)
admin.site.register(Subscribe)
admin.site.register(TrendingGames)
admin.site.register(PopularGames)
admin.site.register(TopCategories)

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('id' , 'address' , 'phone' , 'email')
    list_display_links = ('id' , 'address' , 'phone' , 'email')
    search_fields = ('id' , 'address' , 'phone' , 'email' , 'text' , 'title' , 'subtitle')


@admin.register(ContactUsF)
class ContactUsFModelAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'surname' , 'email' , 'subject')
    list_display_links = ('id' , 'name' , 'surname' , 'email' , 'subject')
    search_fields = ('id' , 'name' , 'surname' , 'email' , 'subject' , 'message')

