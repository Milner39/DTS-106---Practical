"""
Nav Bar

The site-wide nav bar:
- Renders the navigation
- Adapts to whether the user is logged-out, a logged-in member, or staff
"""

from typing import NamedTuple

from django_components import Component, register



@register("nav_bar")
class NavBar(Component):
  template_file = "nav_bar.html"
  css_file = "nav_bar.css"
  js_file = "nav_bar.js"



  class Link(NamedTuple):
    label: str
    url_name: str

  guest_links = [
    Link("Home", "home"),
    Link("About", "about"),
    Link("Contact", "contact"),
  ]
  member_links = [
    Link("Events", "events"),
    Link("My events", "my_events"),
  ]
  staff_links = [
    Link("Dashboard", "admin_events")
  ]


  def get_template_data(self, args, kwargs, slots, context):
    # `resolver_match` is set by Django once the URL has been resolved, and
    # holds the name of the view currently being rendered (e.g. "home").
    resolver_match = getattr(self.request, "resolver_match", None)
    current_url_name = resolver_match.url_name if resolver_match else None

    # `user` is provided by the auth context processor and is available
    # directly in the template.
    # Returning it here causes django-components to error.
    user = self.context_processors_data.get("user")
    is_authenticated = bool(user and user.is_authenticated)
    is_staff = bool(user and user.is_staff)

    links = (
      self.guest_links
      + (self.member_links if is_authenticated else [])
      + (self.staff_links if is_staff else [])
    )

    return {
      "links": links,
      "current_url_name": current_url_name,
      "is_authenticated": is_authenticated,
      "is_staff": is_staff,
    }
