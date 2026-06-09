"""
Base page

The site-wide HTML skeleton:
- Loads Bootstrap
- Renders base layout components
"""

from django_components import Component, SlotInput, register


@register("base")
class Base(Component):
  template_file = "base.html"
  css_file = "base.css"
  js_file = "base.js"


  class Args():
    title: str = "Events39"

  class Slots():
    content: SlotInput | None = None


  # Additional CSS and JS
  class Media:  # pyright: ignore[reportIncompatibleVariableOverride]
    css = ["https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css"]



  def get_template_data(self, args: Args, kwargs, slots: Slots, context):
    return {
      "title": args.title
    }
