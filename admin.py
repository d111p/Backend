from django.contrib import admin
from django.contrib import admin
from .models import Reservation, Signup, billingInfo,profile,Rooms_info,Hotels,customer, customer_details, customer_info, rooms, service_info, services,billingInfo, Reservation, service_info, services, rooms
# adminUser,customeruser,User
# Register your models here.
admin.site.register(Signup)
admin.site.register(profile)
admin.site.register(Rooms_info)
admin.site.register(Hotels)
admin.site.register(customer_details)
admin.site.register(customer_info)
admin.site.register(customer)
admin.site.register(Reservation)
admin.site.register(billingInfo)
admin.site.register(service_info)
admin.site.register(services)
admin.site.register(rooms)
# admin.site.register(adminUser)
# admin.site.register(customeruser)
# admin.site.register(User)
