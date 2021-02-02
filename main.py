from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1000')
import json
from kivymd.app import MDApp
from kivy import properties as KP
from kivy.factory import Factory as F



class TestApp(MDApp):
    rvdata = KP.ListProperty()

    def build(self):
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red" PICK ANOTHER THEME...MAYBE BLUEGRAY
        with open('test_rundown.json') as json_file:
            fresh_data = json.load(json_file)
            self.rvdata = fresh_data




class DrawingWidget(F.RelativeLayout):
    story_id = KP.StringProperty(None, allownone=True)
    line_points = KP.ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(line_points=self.draw_on_canvas)

    def draw_on_canvas(self, _, points):
        with self.canvas:
            F.Color(0, 0, 0, 1)
            F.Line(width=2, points=points)



    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super().on_touch_down(touch)


    def on_touch_move(self, touch):
        if touch.grab_current is self:
            if self.collide_point(*touch.pos):
                self.line_points.extend(self.to_local(*touch.pos))
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):

        if touch.grab_current is self:

            if self.collide_point(*touch.pos):
                self.line_points.extend(self.to_local(*touch.pos))

            if len(self.line_points) <= 2:
                self.line_points = []

            if self.story_id is not None:

                self.line_points = []

            return True
        return super().on_touch_up(touch)



if __name__ == '__main__':
    TestApp().run()
