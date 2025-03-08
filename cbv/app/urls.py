from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('cbv_register', cbv_register.as_view(), name='cbv_register' )
]
