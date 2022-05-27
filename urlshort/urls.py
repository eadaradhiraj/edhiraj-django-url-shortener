from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path('urls/', views.Urls.as_view()),
    path("urls/red/<str:slug>", views.urlRedirect, name="redirect")
]
