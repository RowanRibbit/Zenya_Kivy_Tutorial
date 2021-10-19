from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView

from random import randint

# properties allow us to attach widgets to state maintained in our python files - promises a widget that it will have a variable which will be updated in the Python file, which is updated automatically in the Kivy file
# i.e., Name property > Updated to new name. With Kivy, tell the label widget is expecting a string. If the string changes, it updates in the widget itelf.
# Typically attach props as global variables

# import the Window
Window.clearcolor = (1,1,1,1)
Window.size = (300,400)

# ModalView and Popup have the same superclass and share a lot of behaviour
# Want to display this when the timer is up or the player finishes the game
# On exit reset the game
class EndGameScreen(ModalView):
  # dismiss function
  pass


# custom widget for the images
class ImageBox(Widget):
  index = NumericProperty(0)
  image_name = StringProperty('')

  def get_image_path(self, image_name):
    return 'Images/'+image_name+'.png'

class ProgressBar(Widget):
  pass

# gamescreen class, subclass of widget
class GameScreen(Widget):



  # get the item names
  item_names = [
    'bote', 'diamante', 'espada', 'hacha', 'ladrillos', 'manzana', 'pala', 'pasto', 'roca', 'tierra'
  ]
  # numeric property for correct answer index
  correct_answer_index = NumericProperty(0)
  display_image_names = ListProperty(['bote', 'diamante', 'espada', 'hacha'])
  correct_answer_text = StringProperty('bote')
  
  def __init__(self, **kwargs):
    super(GameScreen, self).__init__(**kwargs)
    self.load_new_question()

  # check if a selection is correct based on the index
  def check_if_answer_correct(self, index):
    if index == self.correct_answer_index:
      return True
    return False

  def get_random_image_names(self):
    # get 4 random image names
    # copy the contents of the list with copy()
    temp_items = self.item_names.copy()
    items = []

    for _ in range(4):
      rand_index = randint(0,len(temp_items)-1)
      items.append(temp_items[rand_index])
      del temp_items[rand_index]
    return items

  def load_new_question(self, *args):
    # choose 4 random images
    # randomly choose a correct answer
    # display images and the label with the correct answer
    self.disply_image_names = self.get_random_image_names()
    self.correct_answer_index = randint(0,3)
    self.correct_answer_text = self.display_image_names[self.correct_answer_index]
    
  def make_selection(self, index):
    # get the button index
    if self.check_if_answer_correct(index):
      self.show_answer_popup(True)
    else:
      self.show_answer_popup(False)
  
  def show_answer_popup(self, is_correct):
    content = Image(source='Images/'+self.correct_answer_text+'.png')
    # call function to change the score based on correct
    popup = Popup(
      title = 'Correct' if is_correct else 'Incorrect',
      size_hint=(.5,.4),
      content=content,
      # title centered, coloured black, set bg to white
      title_alight='center',
      title_color=(0,0,0,1),
      background='Images/white.png',
      # when dismiss popup call a function    
    )
    popup.bind(on_dismiss=self.load_new_question)
    # creates a popup but doesnt attach it to anything
    popup.open()

  def show_endgame_popup(self):
    end_game_screen = EndGameScreen(
      size_hint=(.75, .6), 
      auto_dismiss=False)
    end_game_screen.open()

# create a kivy file which is the same as the app name, but all lower case
class LanguageLearnerApp(App):

    def build(self):
      game_screen = GameScreen()
      return game_screen
        
    
if __name__ == '__main__':
    LanguageLearnerApp().run()