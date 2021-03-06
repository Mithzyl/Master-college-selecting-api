from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.utils.translation import gettext as _
from Users.models import User
from Colleges.models import Colleges
from Majors.models import Majors
from Favorites.models import FavoriteColleges, FavoriteMajors
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


# class MajorsAdmin(GroupAdmin):
#     ordering = ['name']
#     list_display = ['classes', 'code', 'name']
#
#     filter_horizontal = None


admin.site.register(User, UserAdmin)
admin.site.register(Colleges)
admin.site.register(Majors)
admin.site.register(FavoriteColleges)
admin.site.register(FavoriteMajors)
# admin.site.register(SecondMajorSubject)