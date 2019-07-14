from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from .gps import gps_coord

def main(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()

        ids = list(Address.objects.all().values_list('id', flat=True))
        for id in ids:
            address_obj = Address.objects.get(pk=id)
            if not address_obj.gps:
                loc_dict = gps_coord(address_obj.__str__())
                address_obj.gps = str(loc_dict['lat'])+" "+str(loc_dict['lon'])
                address_obj.fulladdress = loc_dict['fulladdress']
                address_obj.save()
        return redirect('main')
    else:
        form = AddressForm()
        items = Address.objects.all()
        context = {'form':form , 'items':items }
        return render(request, 'webapp/main.html', context)

def delete_address(request, pk):
    if request.method == 'POST':
        address = Address.objects.get(pk=pk)
        address.delete()
    return redirect('main')

# def get_gps(request, pk):
#     if request.method == 'POST':
#         address = Address.objects.get(pk=pk)
#         location = address.__str__()
#         address.gps = gps_coord(location)
#         address.save()
#     return redirect('main')

# def get_all_gps(request):
#     if request.method == 'POST':
#         ids = list(Address.objects.all().values_list('id', flat=True))
#         for id in ids:
#             address_obj = Address.objects.get(pk=id)
#             loc_name = address_obj.__str__()
#             address_obj.gps = gps_coord(loc_name)
#             address_obj.fulladdress = gps_full_address(loc_name)
#             address_obj.save()
#     return redirect('main')
