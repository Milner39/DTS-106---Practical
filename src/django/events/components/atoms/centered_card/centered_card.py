"""
Centered Card

A horizontally-centered card:
- Wraps content (forms, confirmation dialogs) in its `content` slot
"""

from typing import NamedTuple

from django_components import Component, SlotInput, register



@register("centered_card")
class CenteredCard(Component):
  template_file = "centered_card.html"


  class Kwargs(NamedTuple):
    max_width: str = "420px"
    body_class: str = ""

  class Slots(NamedTuple):
    content: SlotInput | None = None


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "max_width": kwargs.max_width,
      "body_class": kwargs.body_class,
    }
