"""
Nav Bar

The site-wide nav bar:
- Renders the navigation
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

  links = [
    Link("Home", "home"),
    Link("About", "about"),
    Link("Contact", "contact"),
  ]


  def get_template_data(self, args, kwargs, slots, context):
    # `resolver_match` is set by Django once the URL has been resolved, and
    # holds the name of the view currently being rendered (e.g. "home").
    resolver_match = getattr(self.request, "resolver_match", None)
    current_url_name = resolver_match.url_name if resolver_match else None

    return {
      "links": self.links,
      "current_url_name": current_url_name,
    }
