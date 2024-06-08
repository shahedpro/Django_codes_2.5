from django.shortcuts import render
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'myapp/form_success.html', {'form': form})
    else:
        form = MyForm()

    return render(request, 'myapp/my_form_template.html', {'form': form})
