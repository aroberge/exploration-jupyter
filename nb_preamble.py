"""Some useful stuff for jupyter notebooks"""

# Using common abbreviations

import matplotlib.pyplot as plt # noqa
import numpy as np  # noqa
import ipywidgets as widgets

from IPython.display import display, HTML

# The following ads a button to hide or display code, which is in an
# html div with class input

javascript_functions = {False: "hide()", True: "show()"}
toggle_code_label = {False: "Montrer le code", True: "Cacher le code"}


def toggle_code(state):
    """Toggles the JavaScript show()/hide() function on the div.input element."""
    output_string = '<script>$("div.input").{}</script>'  # noqa
    output_args = (javascript_functions[state],)
    output = output_string.format(*output_args)
    display(HTML(output))


def toggle_code_action(value):
    """Calls the toggle_code function and updates the button description."""
    state = value.new
    toggle_code(state)
    value.owner.description = toggle_code_label[state]


state = True
toggle_code(state)
show_code_btn = widgets.ToggleButton(state, description=toggle_code_label[state])
show_code_btn.observe(toggle_code_action, "value")
