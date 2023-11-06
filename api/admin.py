from django.contrib import admin
from .models import Software, License, Recipient

admin.site.register(Software)
admin.site.register(License)
admin.site.register(Recipient)
