from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class ConvertBox(BoxLayout):
    def handle_conversion(self):
        try:
            miles = float(self.ids.input_miles.text)
            km = miles * 1.60934
            self.ids.output_label.text = f'{km:.5f}'
        except ValueError:
            self.ids.output_label.text = "Invalid input"


class ConvertApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        Builder.load_file("convert_miles_km.kv")  # load style/rules
        return ConvertBox()  # explicitly return the root widget


if __name__ == '__main__':
    ConvertApp().run()
