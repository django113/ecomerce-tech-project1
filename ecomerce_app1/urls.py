from django.urls import include, path
from rest_framework import routers
from ecomerce_app1.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]