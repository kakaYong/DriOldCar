from django.contrib import admin
from SmallVideo.models import Video, Avideo, LiveVideo

# Register your models here.

class AvideAdmin(admin.ModelAdmin):
    list_display = ('name', 'actor_name', 'country', 'media_file')
    list_per_page = 12


admin.site.register(Video)
admin.site.register(Avideo, AvideAdmin)
admin.site.register(LiveVideo)
