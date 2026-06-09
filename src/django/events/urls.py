from django.urls import path

from . import views

urlpatterns = [
  # Public
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("contact/", views.contact, name="contact"),
  path("signup/", views.signup, name="signup"),

  # Events (members only)
  path("events/", views.events_list, name="events"),
  path("events/create/", views.event_create, name="event_create"),
  path("events/<int:pk>/", views.event_detail, name="event_detail"),
  path("events/<int:pk>/edit/", views.event_edit, name="event_edit"),
  path("events/<int:pk>/delete/", views.event_delete, name="event_delete"),
  path("my-events/", views.my_events, name="my_events"),

  # Admin dashboard (staff only)
  path("admin-events/", views.admin_events, name="admin_events"),
]
