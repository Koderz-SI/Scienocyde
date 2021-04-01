from django.urls import path
from core.views import (
    about,
    projects,
    contact,
    host,
    add_host,
    host_dashboard,
    detail,
    applyto,
    participant,
    add_participant,
    project_details,
    project_view,
    add_contact,
    delete_host,
)

urlpatterns = [
    path("about/", about, name="about"),
    path("projects/", projects, name="projects"),
    path("contact/", contact, name="contact"),
    path("host/", host, name="host"),
    path("host/add_host/", add_host, name="add_host"),
    path("host_dashboard/<str:username>/", host_dashboard, name="host_dashboard"),
    path("host_dashboard/<str:username>/delete_host/", delete_host, name="delete_host"),
    path("detail/", detail, name="detail"),
    path("applyto/<int:host_id>/", applyto, name="applyto"),
    path(
        "participant/<int:host_id>/",
        participant,
        name="participant",
    ),
    path(
        "participant/add_participant/<int:host_id>/",
        add_participant,
        name="add_participant",
    ),
    path(
        "project_details/<int:project_id>",
        project_details,
        name="project_details",
    ),
    path(
        "project_view/<int:project_id>",
        project_view,
        name="project_view",
    ),
    path(
        "contact/add_contact/",
        add_contact,
        name="add_contact",
    ),
]
