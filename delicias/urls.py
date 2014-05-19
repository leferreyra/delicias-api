from django.conf.urls import patterns, include, url
from viandas import views

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'offers', views.OfferViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)