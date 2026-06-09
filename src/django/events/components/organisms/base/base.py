"""
Base page

The site-wide HTML skeleton:
- Loads Bootstrap
- Renders base layout components
"""

from typing import NamedTuple

from django_components import Component, SlotInput, register



@register("base")
class Base(Component):
  template_file = "base.html"
  css_file = "base.css"
  js_file = "base.js"


  class Kwargs(NamedTuple):
    title: str = "CannyByte"

  class Slots(NamedTuple):
    content: SlotInput | None = None


  # Additional CSS and JS
  class Media:  # pyright: ignore[reportIncompatibleVariableOverride]
    css = [
      "https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css",
      "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
    ]
    js = [
      "https://cdn.jsdelivr.net/npm/bootstrap@5/dist/js/bootstrap.bundle.min.js",
    ]



  def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context):
    return {
      "title": kwargs.title
    }
