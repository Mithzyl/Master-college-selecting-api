from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from Users.models import User
from Colleges.models import Colleges
from Majors.models import Majors
from Subjects.models import PoliticSubject, ForeignLanguageSubject,\
                                            FirstMajorSubject, SecondMajorSubject


class UserAdmin(BaseUserAdmin):
    ordering = ['mobile']
    list_display = ['mobile', 'name', 'gender', 'email', 'college']
    fieldsets = (
        (None, {'fields': ('mobile', )}),
        (_('Personal Info'), {'fields': ('name', 'gender', 'email', 'college', )}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Colleges)
admin.site.register(Majors)
# admin.site.register(SecondMajorSubject)