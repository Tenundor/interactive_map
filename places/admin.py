from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('file', 'get_preview')
    extra = 1

    readonly_fields = ('get_preview',)

    def get_preview(self, instance):
        return format_html('<img src="{url}" style="width:auto; height:200px;"/>', url=instance.file.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
