from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .forms import AddressForm, FileForm
from .models import Address, Files
from .gps import gps_coord
from .gps import GenerateMap

def main(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        form_f = FileForm(request.POST, request.FILES)
        if request.FILES:             # Проверка есть ли файл на аплоад
            if form_f.is_valid():
                form_f.save()           # Сохраняем файл

                file_path = ''.join(Files.objects.all().order_by('-id').values_list('txtfile')[0]) # Get LATEST file in DB by ID
                with open(file_path) as txt:
                    data = txt.readlines()
                    for address in data:
                        new_address = Address(address=address)  #creating new DB entries, saving
                        new_address.save()
        else:
            if form.is_valid():  # checking for manual form
                form.save()

        counter = 1
        ids = list(Address.objects.all().values_list('id', flat=True)) # get IDs of all saved entries
        for id in ids:
            address_obj = Address.objects.get(pk=id)
            if not address_obj.fulladdress:               # check to get new GPS only for NEW enries
                print(f'getting GPS # {counter}')
                counter += 1

                loc_dict = gps_coord(address_obj.__str__())
                address_obj.latitude = loc_dict['lat']
                address_obj.longitude= loc_dict['lon']
                address_obj.fulladdress = loc_dict['fulladdress']
                address_obj.save()

        return redirect('main')
    else:
        form = AddressForm()
        form_f = FileForm()
        items = Address.objects.all()
        context = {'form':form , 'form_f':form_f, 'items':items }
        return render(request, 'webapp/main.html', context)

def render_map(request):
    map = GenerateMap()
    for obj in Address.objects.all():
        obj_dict = {'fulladdress':obj.fulladdress, 'lat':obj.latitude, 'lon':obj.longitude}
        map.add_point(obj_dict)
    html_file = map.get_html()
    return render(request, html_file)

def delete_address(request, pk):
    if request.method == 'POST':
        address_obj = Address.objects.get(pk=pk)
        address_obj.delete()
    return redirect('main')

def delete_address_all(request):
    ids = list(Address.objects.all().values_list('id', flat=True))
    for id in ids:
        address_obj = Address.objects.get(pk=id)
        address_obj.delete()
    return redirect('main')
