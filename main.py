from kivymd.app import MDApp
from kivy.clock import Clock
from functools import partial
import os

from os.path import dirname, join


class TestApp(MDApp):
    dir_get_counter = 0

    kivy_dir = os.getcwd()

    def build(self):
        print('build')
        self.kivy_dir = os.getcwd() if len(os.listdir(getattr(self, 'user_data_dir'))) == 0 else self.user_data_dir

    def dir_get(self, *args):
        '''Provides a way for the .kv to load files.'''
        path_list = [self.kivy_dir]
        for arg in args:
            path_list.append(arg)
        self.dir_get_counter += 1
        return os.path.join(*path_list)


if __name__ == '__main__':
    TestApp().run()
