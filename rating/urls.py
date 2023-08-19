from django.urls import path 

from rating import views

urlpatterns = [
    path('credit_credit_rating',views.credit_rating_view, name='add-rating'),
]
