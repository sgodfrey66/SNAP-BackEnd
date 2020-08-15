from django.contrib import admin
from .models import SecurityGroup,SecurityGroupUserAgency


admin.site.register(SecurityGroup)
admin.site.register(SecurityGroupUserAgency)
