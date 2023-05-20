from django.shortcuts import render, redirect

from CarsSite.forms import UserName
from CarsSite.models import Person


def edit_user(request, id):
    person = Person.id.get(id=id)
    if request.method == "POST":
        form = UserName(request.POST)
        if form.is_valid():
            name = form['product_name'].value()
            person.name = name
            try:
                person.save()
                return redirect("/")
            except Exception as e:
                form = UserName(request.POST)
                return render(request, "AddUser.html", {
                    'form': form,
                    'error_message': "такое имя занято"
                })
    else:
        form = UserName(initial={
            "user_name": person.name
        })

        return render(request, "addUser.html", {'form': form})


def user_list(request):
    out = Person.objects.all()
    person = []

    for person in out:
        person.append((
            person.id,
            person.name
        ))

    return render(request, "Person_List.html", {'users': person})


def delete_person(request, id):
    product = Person.id.get(id=id)
    product.delete()
    return redirect("/")


def add_user(request):
    if request.method == "POST":
        try:
            form = UserName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                Person = Person(name=name)
                Person.save()
                return redirect("/")
        except Exception as e:
            form = UserName(request.POST)
            return render(request, "AddUser.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = UserName()
        return render(request, "AddUser.html", {'form': form})
