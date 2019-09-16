import xadmin
from xadmin.views import CommAdminView, BaseAdminView

from django.conf import settings

from .models import Link, SideBar
from Talk.base_admin import BaseOwnerAdmin

# Register your models here.
@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    #list_display控制展示的时候页面的显示
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    #fileds字段控制展示的时候的显示
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        return super(LinkAdmin, self).save_model(request, obj, form, change)

@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        return super(SideBarAdmin, self).save_model(request, obj, form, change)

#注册全局样式
@xadmin.sites.register(CommAdminView)
class GlobalSetting:
    site_title = settings.XADMIN_TITLE
    site_footer = settings.XADMIN_FOOTER_TITLE

#注册主题样式
@xadmin.sites.register(BaseAdminView)
class BaseSetting:
    enable_themes = True
    use_bootswatch = True