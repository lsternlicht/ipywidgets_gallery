# test_ipywidgets_gallery.py

from ipywidget_gallery import (
    CheckboxWithOutput,
    ColorPickerWithOutput,
    DatePickerWithOutput,
    DropdownWithOutput,
    FilePickerWithOutput,
    IntSliderWithOutput,
    RadioButtonsWithOutput,
    RangeSliderWithOutput,
    SelectMultipleWithOutput,
    TextAreaWithOutput,
    ToggleButtonGroupWithOutput,
    ToggleButtonWithOutput,
)
import ipywidgets as widgets


def test_checkbox_output():
    checkbox = CheckboxWithOutput("Label", "Checkbox is {}", "checkbox_value")
    assert isinstance(checkbox.checkbox, widgets.Checkbox)


def test_colorpicker_output():
    colorpicker = ColorPickerWithOutput("Label", "Color is {}", "color_value")
    assert isinstance(colorpicker.color_picker, widgets.ColorPicker)


def test_datepicker_output():
    datepicker = DatePickerWithOutput("Label", "Date is {}", "date_value")
    assert isinstance(datepicker.date_picker, widgets.DatePicker)
