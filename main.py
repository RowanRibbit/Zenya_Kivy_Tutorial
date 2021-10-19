from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window

# properties allow us to attach widgets to state maintained in our python files - promises a widget that it will have a variable which will be updated in the Python file, which is updated automatically in the Kivy file
# i.e., Name property > Updated to new name. With Kivy, tell the label widget is expecting a string. If the string changes, it updates in the widget itelf.
# Typically attach props as global variables

# import the Window
Window.clearcolor = (1,1,1,1)
Window.size = (300,400)

# custom widget for the images
class ImageBox(Widget):
  pass

class ProgressBar(Widget):
  pass

# gamescreen class, subclass of widget
class GameScreen(Widget):
  # start with images, buttons, default text
  numeric = NumericProperty(0)
  label_text = StringProperty('')
  def __init__(self, **kwargs):
    super(GameScreen, self).__init__(**kwargs)

    self.numeric = 10
    self.label_text = 'Here is a value'
  def on_press(self):
    print('Button Pressed')

# create a kivy file which is the same as the app name, but all lower case
class LanguageLearnerApp(App):

    def build(self):
      game_screen = GameScreen()
      return game_screen
        
    
  

if __name__ == '__main__':
    LanguageLearnerApp().run()