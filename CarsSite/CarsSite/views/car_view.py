from django.shortcuts import render, redirect

from CarsSite.models import Car



def add_car(request):
    if request.method == "POST":
        try:
            form = CarName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                product = Person(name=name)
                product.save()
                return redirect("/")
        except Exception as e:
            form = UserName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = UserName()
        return render(request, "addProduct.html", {'form': form})
