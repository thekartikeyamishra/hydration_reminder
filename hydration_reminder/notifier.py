from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup

def show_reminder(message):
    popup = Popup(title='Hydration Reminder',
                  content=Label(text=message),
                  size_hint=(None, None), size=(300, 150))
    popup.open()
