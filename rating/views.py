from django.shortcuts import render, redirect
from .forms import CreditRatingForm

def create_credit_rating(request):
    if request.method == 'POST':
        form = CreditRatingForm(request.POST)
        if form.is_valid():
            credit_rating = form.save(commit=False)
            # You can customize the logic for setting the maker and checker here.
            # For example, you can set them based on user roles.
            credit_rating.maker = request.user
            credit_rating.checker = None  # Initially, there's no checker
            credit_rating.save()
            return redirect('credit_rating_list')  # Replace with your URL
    else:
        form = CreditRatingForm()

    context = {'form': form}
    return render(request, 'rating/create_credit_rating.html', context)
