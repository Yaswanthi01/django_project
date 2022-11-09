from django.urls import include, path

from rest_framework import routers

from myapp.views import AssetViewSet
from . import views

# router = routers.DefaultRouter()
# router.register(r'Asset', AssetViewSet)


urlpatterns = [
    path('Asset/',     AssetViewSet.as_view()),
    path('Asset/<int:object_id>', AssetViewSet.as_view()),
    path('home/',views.homepage)
	

]