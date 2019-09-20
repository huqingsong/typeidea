from rest_framework import viewsets
from pprint import pprint

from .models import Post, Category
from .serializer import (
    PostSerializer, PostDetaiSerializer,
    CategorySerializer, CategoryDetailSerializer
)

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """ 提供文章接口 """
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetaiSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    # def list(self, request, *args, **kwargs):
    #     for query in self.queryset:
    #         pprint(query)
    #     return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
