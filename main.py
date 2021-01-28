from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1000')
import json
from kivymd.app import MDApp
from kivy import properties as KP
from rows.row import Row, DrawingRepository #### DO NOT DELETE!!! ######
from kivymd.uix.screen import MDScreen

# TODO: POSSIBILITES FOR REDUCED SPEED:
# KIVYMD



class TestApp(MDApp):
    rvdata = KP.ListProperty()

    def build(self):
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red" PICK ANOTHER THEME...MAYBE BLUEGRAY
        with open('test_rundown.json') as json_file:
            fresh_data = json.load(json_file)
            self.rvdata = fresh_data


class LoginScreen(MDScreen):
    username = 'joe'
    password = 'aaa'

    def login(self, login_text, password_text):
        if login_text == self.username and password_text == self.password:
            self.parent.current = 'menu'

        else:
            self.parent.current = 'menu'


if __name__ == '__main__':
    TestApp().run()
