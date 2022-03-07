from re import search
from django.contrib import admin
from production.models import Pallet, Box

class Pallets(admin.ModelAdmin):
    list_display = ('Palletqty','line','operator','data_production','shift_closed')
    list_display_link = ('line',)
    search_field = ('Palletqty',)
    list_per_page = (20)

admin.site.register(Pallet, Pallets)

class Boxs(admin.ModelAdmin):
    list_display = ('Box_tqty','Box_line','Box_operator','Box_data_production','Box_shift_closed','Box_Product')
    list_display_link = ('Box_tqty',)
    search_field = ('Box_Product',)

admin.site.register(Box, Boxs)
