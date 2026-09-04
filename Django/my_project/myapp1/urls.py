from django.urls import path, re_path
from myapp1 import views
urlpatterns = [
    path("", views.home, name = "home"),
    path("about", views.about, name = "about"),
    path("shareid/<int:id>/<str:name>",views.shareid, name="shareid"),
    re_path(r'^year/(?P<year>[0-9]{4})/$', views.year),
    path("key_word_args/<int:id>/<str:name>", views.key_word_args, name="key_word_args")
]