from django.urls import path, include
from author.views import AuthorViewSet
from rest_framework import routers

app_name = "author"

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
