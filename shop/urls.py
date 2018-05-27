from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ProductView.as_view(), name='product'),
    url(r'^form/', views.form, name='form'),
    ]