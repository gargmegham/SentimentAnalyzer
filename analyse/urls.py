from django.urls import path,include
from analyse import views

urlpatterns = [
    path('',views.analyse,name='analyse'),
]
