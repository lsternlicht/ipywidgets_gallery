# IPyWidget Gallery

IPyWidget Gallery is a library of interactive widgets for Jupyter notebooks.
It provides a collection of classes that can be used to create widgets with
custom output and global variable assignments.

## Installation

You can install IPyWidget Gallery using pip:
    
```bash
    pip install ipywidget-gallery
```

IPyWidget Gallery depends on the ipywidgets package, which must also be
installed:
    
    
```bash
    pip install ipywidgets
```
    

## Usage

To use IPyWidget Gallery in your Jupyter notebooks, you can import the classes
you need and create instances of them. For example, to create a dropdown
widget that displays the selected option and sets a global variable, you can
use the `DropdownWithOutput` class:

    
```python
    pip install ipywidgets
    from ipywidget_gallery import DropdownWithOutput
    
    my_dropdown = DropdownWithOutput('Select an option:', ['Option 1', 'Option 2', 'Option 3'], 'You selected {}!', 'my_global_var')
```

This will display a dropdown widget with the specified label and options, and
an output widget that displays the specified message (formatted with the
selected option) when an option is selected. The global variable named
`my_global_var` will be set to the selected option when an option is selected.

IPyWidget Gallery provides a variety of other classes for creating widgets
with different types of output and global variable assignments. 

<!-- See the  [documentation](https://github.com/lsternlicht/IPyWidgetGallery/tree/main/docs)
for more information.-->

## License

IPyWidget Gallery is released under the MIT License. See the
[LICENSE](LICENSE) file for details.