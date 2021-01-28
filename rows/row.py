from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy import  properties as KP
from kivy.graphics import Color, Line


class Row(RecycleDataViewBehavior, BoxLayout):
    # Copy description from Slicker
    index = KP.NumericProperty()
    title = KP.StringProperty()
    camera = KP.StringProperty()
    story_id = KP.StringProperty()
    backtime = KP.StringProperty()

    def refresh_view_attrs(self, view, index, data):
        self.index = index

        super().refresh_view_attrs(view, index, data)

    def on_parent(self, instance, parent):
        if parent:
            pass
            # self.ids.title_lbl.text = self.title
            # self.ids.camera_lbl.text = self.camera
            # self.ids.drawingwidget.story_id = self.story_id
            # self.ids.backtime_lbl.text = self.backtime


class DrawingRepository:
    drawings = {}


    @staticmethod
    def add_drawing(story_id, points):
        drngs = DrawingRepository.drawings

        if story_id is not None:
            drngs[story_id] = points


    @staticmethod
    def get_drawing(story_id, default=None):
        return DrawingRepository.drawings.get(story_id, default)

    @staticmethod
    def has_drawing(story_id):
        return story_id in DrawingRepository.drawings




class DrawingWidget(RelativeLayout):
    story_id = KP.StringProperty(None, allownone=True)
    line_points = KP.ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(line_points=self.draw_on_canvas)

    def draw_on_canvas(self, _, points):
        with self.canvas:
            Color(1, 0, 0, 1)
            Line(width=2, points=points)



    def on_story_id(self, _, story_id):
        drawings = DrawingRepository.get_drawing(story_id)

        if drawings is not None:
            with self.canvas:
                Line(points=drawings)
        else:
            self.line_points = []
            self.canvas.clear()

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
        dp = DrawingRepository
        if touch.grab_current is self:

            if self.collide_point(*touch.pos):
                self.line_points.extend(self.to_local(*touch.pos))

            if len(self.line_points) <= 2:
                self.line_points = []

            if self.story_id is not None:
                dp.add_drawing(self.story_id, self.line_points[:])
                self.line_points = []

            return True
        return super().on_touch_up(touch)
