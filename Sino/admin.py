from django.contrib import admin
from .models import customer,Product,Order,Category,Status



admin.site.register(customer )
admin.site.register(Category )
admin.site.register(Status )
admin.site.register(Order )
admin.site.register(Product )

admin.site.index_title = 'BADASS'


