from django.shortcuts import render
from formApp.forms import NewUser
# Create your views here.

def form_view(request):
    form = forms.formApp()
    print("Before POST Method")
    if request.method == "POST":
        print("POST")
        form = forms.formApp(request.POST)
        if form.is_valid():
            print("Validation Success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request,'formApp/MyForm.html',{'formdata':form})

def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request,'formApp/user.html',{'formdata':form})
