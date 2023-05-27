from django.shortcuts import render, redirect

from ..forms import CarNew
from ..models import Car, Person, Brand


def new_car(request):
    if request.method == "POST":
        try:
            form = CarNew(request.POST)
            if form.is_valid():
                brand = form["brand"].value()
                users = form["users"].value()
                image = form["image"].value()
                cost = form["cost"].value()
                speed = form["speed"].value()
                name = form["name"].value()

                car = Car(image=image, cost=cost, speed=speed,name = name,
                          brand=Brand.objects.get(id=brand))

                car.save()
                for user_id in users:
                    user = Person.objects.get(id=user_id)
                    if user is not None:
                        car.users.add(user)
                        car.users.add(user)

                return redirect("/")
        except Exception as e:
            form = CarNew(request.POST)
            return render(request, "addCar.html", {
                'form': form,
                'error_message': e
            })
    else:
        form = CarNew()
        return render(request, "addCar.html", {'form': form})


def list_car(request):
    out = Car.objects.all()
    car = []

    for car in out:
        users = []
        for user in car.users.all():
            users.append(
                (user.id,
                 user.name)
            )

        car.append((
            car.id,
            car.brand,
            car.image,
            car.cost,
            car.speed,
            users
        ))

    return render(request, "carList.html", {'car': car})
