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

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


if __name__ == '__main__':
    BoxLayoutDemoApp().run()
