from django.contrib import admin
from .models import Board, Common_Tag, Travel_Tag, Res_tag, Cafe_tag
from accounts.models import User


# Register your models here.
@admin.register(Board)
class BoardModelView(admin.ModelAdmin):
    list_display = (
        "title",
        "writer",
        "tag_common",
        "tag_travel",
        "tag_res",
        "tag_cafe",
    )

    def tag_common(self, obj):
        return ",".join([t.tag_name for t in obj.tag_common.all()])

    def tag_travel(self, obj):
        return ",".join([t.tag_name for t in obj.tag_travel.all()])

    def tag_res(self, obj):
        return ",".join([t.tag_name for t in obj.tag_res.all()])

    def tag_cafe(self, obj):
        return ",".join([t.tag_name for t in obj.tag_cafe.all()])


@admin.register(Common_Tag)
class CommonTagModelView(admin.ModelAdmin):
    list_display = ("tag_common",)


@admin.register(Travel_Tag)
class TravelTagModelView(admin.ModelAdmin):
    list_display = ("tag_travel",)


@admin.register(Res_tag)
class ResTagModelView(admin.ModelAdmin):
    list_display = ("tag_res",)


@admin.register(Cafe_tag)
class CafeTagModelView(admin.ModelAdmin):
    list_display = ("tag_cafe",)


admin.site.register(User)
