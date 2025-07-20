from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(BoxLayout):
    pass

class BoxLayoutDemoApp(App):
    def build(self):
        self.title = "Box Layout Demo"
        Builder.load_file("box_layout.kv")
        return BoxLayoutDemo()  # <--- instantiate the widget

if __name__ == '__main__':
    BoxLayoutDemoApp().run()
