from django.urls import path,include
from .views import *
app_name = "home"

urlpatterns = [
    path('', home, name='home'), # home = function name
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('blogHome', blogHome, name='blogHome'),
    path('blogSingle', blogSingle, name='blogSingle'),
]