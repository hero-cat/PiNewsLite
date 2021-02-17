from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1000')
from kivymd.app import MDApp

class TestApp(MDApp):
    pass


TestApp().run()
