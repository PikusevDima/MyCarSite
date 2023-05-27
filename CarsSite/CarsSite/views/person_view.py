from django.shortcuts import render, redirect

from CarsSite.forms import UserName
from CarsSite.models import Person


def edit_user(request, id):
    user = Person.objects.get(id=id)
    if request.method == "POST":
        form = UserName(request.POST)
        if form.is_valid():
            name = form['person_name'].value()
            user.name = name
            try:
                user.save()
                return redirect("/")
            except Exception as e:
                form = UserName(request.POST)
                return render(request, "Person_list.html", {
                    'form': form,
                    'error_message': "такое имя занято"
                })
    else:
        form = UserName(initial={
            "person_name": user.name
        })

        return render(request, "AddUser.html", {'form': form})


def user_list(request):
    out = Person.objects.all()
    users = []

    for user in out:
        users.append((
            user.id,
            user.name
        ))

    return render(request, "Person_List.html", {'users': users})


def delete_user(request, id):
    user = Person.objects.get(id=id)
    user.delete()
    return redirect("/")


def add_user(request):
    if request.method == "POST":
        try:
            form = UserName(request.POST)
            if form.is_valid():
                name = form['person_name'].value()
                user = Person(name=name)
                user.save()
                return redirect("/")
        except Exception as e:
            form = UserName(request.POST)
            return render(request, "AddUser.html", {
                'form': form,
                'error_message': 'такое имя занято'
            })
    else:
        form = UserName()
        return render(request, "Person_list.html", {'form': form})
