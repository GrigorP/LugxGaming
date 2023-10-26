from django.forms import ModelForm
from .models import Subscribe, ContactUsF


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsF
        fields = '__all__'



