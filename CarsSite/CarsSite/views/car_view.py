from django.shortcuts import render, redirect

from ..forms import CarNew
from ..models import Car, Person, Brand


def new_car(request):
    if request.method == "POST":
        try:
            form = CarNew(request.POST)
            if form.is_valid():
                brand_id = form["users"].value()
                users = form["users"].value()

                car = Car(brand=Brand.objects.get(id=brand_id))

                car.save()
                for user_id in users:
                    user = Person.objects.get(id=user_id)
                    if user is not None:
                        car.users.add(user)

                return redirect("/car")
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
            car.customer,
            users
        ))

    return render(request, "carList.html", {'car': car})