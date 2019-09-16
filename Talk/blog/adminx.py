import xadmin
from xadmin.filters import RelatedFieldListFilter, manager
from xadmin.layout import Row, Fieldset, Container

from django.urls import reverse
from django.utils.html import format_html

from Talk.base_admin import BaseOwnerAdmin
from .models import Post, Category, Tag
from .adminforms import PostAdminForm

class PostInline:
    form_layout = (
        Container(
            Row('title', 'desc')
        )
    )
    extra = 1 #控制额外多几个
    model = Post

@xadmin.sites.register(Category)
class Category(BaseOwnerAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

class CategoryOwnerFilter(RelatedFieldListFilter):
    """ 自定义过滤器只展示当前用户的分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, admin_view, field_path):
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')

manager.register(CategoryOwnerFilter, take_priority=True)

@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]
    date_hierarchy = 'created_time'
    search_fields = ['title', 'category__name']

    # 开启顶部的编辑按钮
    save_on_top = True

    #动作的相关配置
    actions_on_top = True
    actions_on_bottom = True

    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
            'status'
        )
    )

    # 设置字段横向或纵向展示
    filter_horizontal = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id, ))
        )

    operator.short_description = '操作'