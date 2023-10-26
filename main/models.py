from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Category(models.Model):

    name = models.CharField('Category name: ', max_length=255)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Game(models.Model):
    category = models.ManyToManyField(Category)
    img = models.ImageField('Game Image', upload_to='media')
    name = models.CharField('Name of the game', max_length=255)
    price = models.DecimalField('Game Price' , max_digits=5 , decimal_places=2, blank=True)
    discount = models.DecimalField('Price Discount' , max_digits=4 , decimal_places=2, blank = True)
    about = models.TextField('About Game')
    gameID = models.CharField('Game ID' , max_length=15, blank=True)
    genre = models.CharField('Ganre' , max_length=50, blank=True)
    multi_tags = models.CharField('Multy tags' , max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

class TrendingGames(models.Model):

    game = models.ManyToManyField(Game)

    def __str__(self) -> str:
        return self.game.__str__()
    
    class Meta:
        verbose_name = 'TrendingGame'
        verbose_name_plural = 'TrendingGames'

class PopularGames(models.Model):

    popular_game = models.ManyToManyField(Game)

    def __str__(self) -> str:
        return self.popular_game.__str__()
    
    class Meta:
        verbose_name = 'PopularGame'
        verbose_name_plural = 'PopularGames'

class TopCategories(models.Model):

    game = models.ManyToManyField(Game)

    def __str__(self) -> str:
        return self.game.__str__()
    
    class Meta:
        verbose_name = 'TopCategory'
        verbose_name_plural = 'TopCategories'

class Subscribe(models.Model):

    email = models.EmailField("Email", max_length=254)


    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name_plural = 'Subsribe'


class ContactUs(models.Model):
    title = models.CharField('Contact title', max_length=254)
    subtitle = models.CharField('Subtitle', max_length=254)
    text = models.TextField('Contact text')
    address = models.CharField("Address", max_length=50)
    phone = PhoneNumberField()
    email = models.EmailField("Email", max_length=50)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"

class ContactUsF(models.Model):
    name = models.CharField("Name", max_length=50)
    surname = models.CharField("Surname", max_length=50)
    email = models.EmailField("Email", max_length=50)
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ContactUs Form"
        verbose_name_plural = "ContactUs Form"
        