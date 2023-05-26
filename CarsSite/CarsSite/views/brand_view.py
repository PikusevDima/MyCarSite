from django.shortcuts import render, redirect
from CarsSite.forms import BrandName, CarManufacturerName
from CarsSite.models import Brand


def add_brand(request):
    if request.method == "POST":
        try:
            form = BrandName(request.POST)
            if form.is_valid():
                name = form['brand_name'].value()
                brand = Brand(name=name)
                brand.save()
                return redirect("/")
            form = BrandName(request.POST)
        except Exception as e:
            form = BrandName(request.POST)
            return render(request, "addBrand.html", {
                'form': form,
                'error_message': 'такое имя занято'
            })
    else:
        form = BrandName()
        return render(request, "addBrand.html", {'form': form})
