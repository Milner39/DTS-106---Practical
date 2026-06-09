"""
Form Fields

Renders a whole Django form:
- Non-field (form-level) errors
- Each visible field via the `form_field` atom
- Hidden fields
- The surrounding <form>, csrf token and submit buttons stay in the page template.
"""

from typing import NamedTuple

from django.forms import BaseForm
from django_components import Component, register



@register("form_fields")
class FormFields(Component):
  template_file = "form_fields.html"


  class Kwargs(NamedTuple):
    form: BaseForm


  def get_template_data(self, args, kwargs: Kwargs, slots, context):
    return {
      "form": kwargs.form,
    }
