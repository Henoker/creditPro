from django.shortcuts import render, redirect
from .forms import CreditRatingForm

def credit_rating_view(request):
    if request.method == 'POST':
        form = CreditRatingForm(request.POST)
        if form.is_valid():
            # Process the form data, save it to the database, etc.
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = CreditRatingForm()

    return render(request, 'rating/credit_credit_rating.html', {'form': form})