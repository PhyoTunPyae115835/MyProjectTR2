from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class RootWidget(BoxLayout):
    pass


class DynamicLabelApp(App):
    def build(self):
        self.title = "Dynamic Labels Example"
        Builder.load_file("dynamic_labels.kv")
        root = RootWidget()

        names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in names:
            label = Label(text=name)
            root.ids.entries_box.add_widget(label)

        return root


if __name__ == "__main__":
    DynamicLabelApp().run()
