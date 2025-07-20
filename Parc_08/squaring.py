from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class SquareRootBox(BoxLayout):
    def handle_square(self):
        try:
            number = float(self.ids.input_number.text)
            result = number ** 2
            self.ids.output_label.text = str(result)
        except ValueError:
            self.ids.output_label.text = 'Invalid input'

class SquareApp(App):
    def build(self):
        self.title = "Square Number"
        return Builder.load_file("squaring.kv")

if __name__ == '__main__':
    SquareApp().run()
