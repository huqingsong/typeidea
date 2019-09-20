#这里使用xadmin替代admin
import xadmin
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework import renderers

from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps import views as sitemap_views

from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView,
    Handler404, Handler50x
)
from comment.views import CommentView, VerifyCaptcha
from config.views import ListView
from blog.sitemap import PostSitemap
from blog.rss import LastPostFeed
from blog.apis import PostViewSet, CategoryViewSet

sitemaps = {
    'posts': PostSitemap
}

handler404 = Handler404.as_view()
# handler500 = Handler50x.as_view()

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    path('admin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^links/$', ListView.as_view(), name='links'),
    url(r'^sitemap\.xml', cache_page(60 * 20, key_prefix='sitemap_cache_')(sitemap_views.sitemap), {'sitemaps': sitemaps}),
    url(r'^rss|feed', LastPostFeed(), name='rss'),

    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^verify_captcha/', VerifyCaptcha.as_view(), name='verify_captcha'),
    url(r'^api/', include(router.urls)),
    # url(r'^api/(?P<post_id>\d+)/post/$', api_post_detail, name='api_post_detail'),
    url(r'^api/docs/', include_docs_urls(title='blog apis')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#这里使用的是
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
