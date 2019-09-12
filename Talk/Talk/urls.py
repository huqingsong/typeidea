"""Talk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.urls import path

import xadmin

from Talk.settings.base import DEBUG

#这里使用xadmin替代admin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]

#这里使用的是
if DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns