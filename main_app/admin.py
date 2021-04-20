from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class My_Recent_Works_Admin(SummernoteModelAdmin):
    summernote_fields = ('project_description',)


admin.site.register(models.Home_dev_information),
admin.site.register(models.About_dev_information),
admin.site.register(models.What_I_do_dev_information),
admin.site.register(models.My_Skills_dev_information),
admin.site.register(models.My_Languages_dev_information),
admin.site.register(models.Social_links_dev_information),
admin.site.register(models.Experience_and_starting_dev_information),
admin.site.register(models.My_Recent_Works_dev_information, My_Recent_Works_Admin)


