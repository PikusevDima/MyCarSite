from django.shortcuts import render, redirect

from .forms import PersonName
from .models import Person


def edit_product(request, id):
    person = Person.objects.get(id=id)
    if request.method == "POST":
        form = PersonName(request.POST)
        if form.is_valid():
            name = form['product_name'].value()
            person.name = name
            try:
                person.save()
                return redirect("/")
            except Exception as e:
                form = PersonName(request.POST)
                return render(request, "addUser.html", {
                    'form': form,
                    'error_message': "такое имя занято"
                })
    else:
        form = PersonName(initial={
            "product_name": person.name
        })

        return render(request, "addProduct.html", {'form': form})


def product_list(request):
    out = Person.objects.all()
    person = []

    for person in out:
        person.append((
            person.id,
            person.name
        ))

    return render(request, "personList.html", {'people': people})


def delete_person(request, id):
    product = Person.objects.get(id=id)
    product.delete()
    return redirect("/")


def add_person(request):
    if request.method == "POST":
        try:
            form = PersonName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                product = Person(name=name)
                product.save()
                return redirect("/")
        except Exception as e:
            form = PersonName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = PersonName()
        return render(request, "addProduct.html", {'form': form})


def delete_with_submit(request, id):
    product = Person.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect("/")
    else:
        return render(request,
                      "submitAction.html",
                      {
                          'message':
                              f"Вы точно хотите удалить продукт с id {product.id}, name {product.name}"
                      })