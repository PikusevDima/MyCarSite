from django.shortcuts import render, redirect
from CarsSite.forms import BrandName
from CarsSite.models import Brand


def add_brand(request):
    if request.method == "POST":
        try:
            form = BrandName(request.POST)
            if form.is_valid():
                brand_name = form['brand_name'].value()
                carManufacturerName = form['carManufacturer_Name'].value()
                brand = Brand(name=brand_name, carManufacturer=carManufacturerName)
                brand.save()
                return redirect("/")
        except Exception as e:
            form = BrandName(request.POST)
            return render(request, "addBrand.html", {
                'form': form,
                'error_message': 'такое имя занято'
            })
    else:
        form = BrandName()
        return render(request, "addBrand.html", {'form': form})
