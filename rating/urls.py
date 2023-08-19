from django.urls import path 

from rating import views

urlpatterns = [
    path('create_credit_rating',views.create_credit_rating, name='add-rating'),
]
