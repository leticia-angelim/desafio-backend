from django.shortcuts import render, redirect
from django.db.models import Sum

from .utils.get_stores_names import get_stores_names
from .utils.convert_file import convert_file
from .forms import UploadFileForm
from .models import Cnab


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            convert_file(request)

            return redirect("list/")
    else:
        form = UploadFileForm()
    return render(request, "cnab/upload.html", {"form": form})


def list_stores(request):
    if request.method == "GET":
        stores = Cnab.objects.all()

        stores_list = []

        stores_names = get_stores_names(stores)

        for name in stores_names:
            store = Cnab.objects.filter(store_name=name)[0]
            value = Cnab.objects.filter(store_name=name).aggregate(total=Sum("value"))

            store.total = value["total"] / 100

            stores_list.append(store)

        return render(request, "cnab/list.html", {"stores_list": stores_list})
