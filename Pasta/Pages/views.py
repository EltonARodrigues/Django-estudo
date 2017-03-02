from django.shortcuts import render


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        dados_form = form.data
        user = authenticate(
            username=dados_form['username'].lower(),
            password=dados_form['password']
        )
        if user is not None:
            login_page(request, user)
            return redirect('index')
return render(request, 'login.html')
