from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .forms import SubscribeForm, ContactUsForm
from django.core.mail import EmailMessage
from LugxGaming.settings import EMAIL_HOST_USER
from .models import *

class HomeListView(generic.ListView):
    template_name = 'index.html'

    @staticmethod
    def __extact_all_data():

        games = Game.objects.all()
        trending_games = TrendingGames.objects.get().game.all()

        for game in trending_games:
            game.discount_price = round(game.price * (1 - game.discount / 100) , 2)

        popular_games = PopularGames.objects.get().popular_game.all()
        top_categories = TopCategories.objects.get().game.all()


        context = {
           'navbar': 'Home',
           'games':games,
           'trending_games':trending_games,
           'popular_games':popular_games,
           'top_categories': top_categories,
        }
        print('_________________________________________________')
        print(top_categories[0])
        print(top_categories[0].name)
        print(top_categories[0].price)
        print(top_categories[0].category.name)



        print('_________________________________________________')

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        context = self.__extact_all_data()
        
        return render(request, self.template_name, context)


    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        form  = SubscribeForm(request.POST)

        if form.is_valid():
            subject = f"Thanks For Subscribtion"

            body = 'Nice Web page'
            try:
                email = EmailMessage(
                subject = subject,
                body = body,
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')],
                )
                email.send()
            except Exception:
                pass
            form.save()
        else:
            form = SubscribeForm()


        context = self.__extact_all_data()

        context.update({'form':form})

        
        return render(request, self.template_name , context)


class ShopListView(generic.ListView):
    template_name = 'shop.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        games = Game.objects.all()
        category = Category.objects.all()
        for game in games:
            game.discount_price = round(game.price * (1 - game.discount / 100) , 2)
            game.main_category = game.category.all()[0]

        context = {
           'navbar': 'Shop',
            'games':games,
            "category":category,
        }
        
        return render(request, self.template_name , context)



class ContactListView(generic.ListView):
    template_name = 'contact.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        contactus = ContactUs.objects.get()

        context = {
            'contactus': contactus,
            'navbar': 'Contact Us' ,
            
        }
        
        return render(request, self.template_name , context)
    
    def post(self, request):

        contactus = ContactUs.objects.get()
        contactusform = ContactUsForm(request.POST)

        if contactusform.is_valid():
            contactusform.save()
        else:
            contactusform = ContactUsForm()

        context = {
            'contactusform': contactusform,
            'contactus': contactus,
            'navbar': 'Contact Us' ,
            
        }
        
        return render(request, self.template_name , context)



class ProductDetailView(generic.DetailView):
    template_name = 'product-details.html'


    def get(self, request: HttpRequest , id ,  *args: Any, **kwargs: Any) -> HttpResponse:
        
        game = Game.objects.get(pk=id)
        game.discount_price = round(game.price * (1 - game.discount / 100) , 2)
        context = {
           'navbar': 'Product Details' ,
           "game":game,
            
        }
        
        return render(request, self.template_name , context)