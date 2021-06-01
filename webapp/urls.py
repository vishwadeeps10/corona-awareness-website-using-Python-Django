from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('vaccination', views.webpage1, name='webpage1'),
    path('dos&donts', views.webpage2, name='webpage2'),
    path('FAQs', views.webpage3, name='webpage3'),
    path('Error', views.webpage4, name='webpage4'),
    
]