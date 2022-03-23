# pyqt-description-tooltip
PyQt QToolTip that user can add description and so on.

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-description-tooltip.git --upgrade```

## Usage
You can get the qt tooltip text using static method below.
```python
DescriptionToolTipGetter.getToolTip(title: str = '', shortcut: str = '', description: str = '', 
shortcut_color: str = '#AAA', description_color: str = '#AAA')
```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from pyqt_description_tooltip import DescriptionToolTipGetter
from pyqt_style_setter import StyleSetter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('ToolTip Button')

        btn.setToolTip(DescriptionToolTipGetter.getToolTip(title='ToolTip Title', shortcut='Ctrl+T',
                                                description='ToolTip Description.',))
        self.setCentralWidget(btn)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = MainWindow()
    StyleSetter.setWindowStyle(example)
    example.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/159687417-3a6adfe8-4f52-4b2e-ad13-4dac51f3d17c.png)


