from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("certifications/", views.certifications, name="certifications"),
    path("projects/", views.projects_index, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
]
