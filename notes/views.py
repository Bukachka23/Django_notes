from django.shortcuts import render, get_object_or_404

from .models import Category, Note

# Define the home view
def home(request):
    return render(request, 'index.html',
    # Pass all Category objects to the template
    {
        'categories': Category.objects.all()
    })

# Define the detail view for a specific category
def category_detail(request, category_id):
    # Get the Category object with the given id, or raise a 404 error
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'detail.html', {
        'category': category
    })