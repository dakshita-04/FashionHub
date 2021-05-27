from django.urls import path
from Management.views import *

urlpatterns = [
    path('About/', About, name='about'),
    path('Contact/', Contact, name='contact')
    
]
