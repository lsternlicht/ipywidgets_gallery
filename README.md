# IPyWidgets Gallery

IPyWidgets Gallery is a library of interactive widgets for Jupyter notebooks.
It provides a collection of classes that can be used to create widgets with
custom output and global variable assignments.

## Installation

You can install IPyWidgets Gallery using pip:
    
```bash
    pip install ipywidgets-gallery
```

IPyWidgets Gallery depends on the ipywidgets package, which must also be
installed:
    
    
```bash
    pip install ipywidgets
```
    

## Usage

To use IPyWidgets Gallery in your Jupyter notebooks, you can import the classes
you need and create instances of them. For example, to create a dropdown
widget that displays the selected option and sets a global variable, you can
use the `DropdownWithOutput` class:

    
![image](https://user-images.githubusercontent.com/128432/230676626-ed9ea717-31aa-4135-ac11-29d0d7ace85a.png)
    
```python
    from ipywidgets_gallery import DropdownWithOutput
    options = ['option 1', 'option 2', 'option 3']
    dropdown = ipywidgets_gallery.DropdownWithOutput(options, default='option 1')
    dropdown.value      # 'option 1'
```

This will display a dropdown widget with the specified label and options, and
an output widget that displays the specified message (formatted with the
selected option) when an option is selected. The global variable named
`my_global_var` will be set to the selected option when an option is selected.

IPyWidgets Gallery provides a variety of other classes for creating widgets
with different types of output and global variable assignments. 



## Available widgets

* `CheckboxWithOutput`
* `ColorPickerWithOutput`
* `DatePickerWithOutput`
* `DropdownWithOutput`
* `FilePickerWithOutput`
* `IntSliderWithOutput`
* `RadioButtonsWithOutput`
* `RangeSliderWithOutput`
* `SelectMultipleWithOutput`
* `TextAreaWithOutput`
* `ToggleButtonWithOutput`
* `ToggleButtonGroupWithOutput`


## License

IPyWidgets Gallery is released under the MIT License. See the
[LICENSE](LICENSE) file for details.
