from django.conf.urls import url
from . import views
app_name = 'Examples'
urlpatterns = [
    url(r"^$", views.HomePage.as_view(), name="all"),
    url(r"^h1/$", views.hello.as_view(), name="h1"),
    url(r"^sumofNumbers/$", views.sumodNum.as_view(), name="sum"),
    url(r"^even/$", views.Even.as_view(), name="even"),
    url(r"^useofpython/$", views.UseofPython.as_view(), name='use'),
    url(r"^cando/$", views.PythonCanDo.as_view(), name='do'),
    url(r"why/$", views.WhyPython.as_view(),name='why'),
    url(r"^variable/$", views.Variablediclration.as_view(), name='var'),
    url(r"^DataTypes/$", views.DataTypes.as_view(), name='dt'),
    url(r"DataTypes/bool/$", views.Bool.as_view(), name='bool'),
    url(r"DataTypes/Numbers/$", views.Numbers.as_view(), name='numbers'),
    url(r"DataTypes/list/$", views.Lists.as_view(), name='list'),
    url(r"DataTypes/tuple/$", views.Tuples.as_view(), name='tuple'),
    url(r"DataTypes/set/$", views.Sets.as_view(), name='set'),
    url(r"DataTypes/dictionary/$", views.Dictionarys.as_view(), name='dict'),
    url(r"DataTypes/strings/$", views.Strings.as_view(), name='strings'),
    url(r"^conversions/$", views.Conversions.as_view(), name='conversions'),
    url(r"^Cstatements/$", views.Conditionalstatements.as_view(), name='cst'),
]
