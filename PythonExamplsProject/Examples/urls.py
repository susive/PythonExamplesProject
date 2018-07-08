from django.conf.urls import url
from . import views
app_name = 'Examples'
urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="all"),
    url(r"^h1/$", views.hello.as_view(), name="h1"),
]
