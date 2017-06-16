"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from snippets import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^slist/', views.home,name="home"),
    url(r'^products/',views.productlist.as_view(),name="item-list"),
    url(r'^product/(?P<pk>[0-9]+)/$',views.productdetail.as_view(),name="item-detail"),
    url(r'^review_submit/',views.review_submit,name="review_sumbit"),
    url(r'^add_product/',views.add_product,name="add_product")
]
