"""
Nav Bar

The site-wide nav bar:
- Renders the navigation
"""

from django_components import Component, register



@register("nav_bar")
class NavBar(Component):
  template_file = "nav_bar.html"
  css_file = "nav_bar.css"
  js_file = "nav_bar.js"
