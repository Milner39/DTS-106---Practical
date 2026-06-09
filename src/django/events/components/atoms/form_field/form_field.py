"""
Form Field

Renders a single bound Django form field:
- Label
- Django widget
- Help text
- Validation errors
"""

from typing import NamedTuple

from django.forms import BoundField
from django_components import Component, register



@register("form_field")
class FormField(Component):
  template_file = "form_field.html"


  class Kwargs(NamedTuple):
    field: BoundField


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "field": kwargs.field,
    }
