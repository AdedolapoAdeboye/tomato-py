from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class ScientificCalculator(GridLayout):
    def __init__(self, **kwargs):
        super(ScientificCalculator, self).__init__(**kwargs)
        self.cols = 4
        self.padding = [20, 20, 20, 20]
        self.spacing = [10, 10]

        self.entry = TextInput(multiline=False, readonly=True, font_size=30)
        self.add_widget(self.entry)

        buttons = [
            ('7',), ('8',), ('9',), ('/',),
            ('4',), ('5',), ('6',), ('*',),
            ('1',), ('2',), ('3',), ('-',),
            ('0',), ('.',), ('=', '+'),
            ('√',), ('^',), ('log',), ('sin',),
            ('cos',), ('tan',), ('AC', '')
        ]

        for text in buttons:
            button = Button(text=text[0], font_size=30)
            button.bind(on_press=self.on_button_click)
            self.add_widget(button)

    def on_button_click(self, instance):
        if instance.text == '=':
            try:
                result = eval(self.entry.text)
                self.entry.text = str(result)
            except:
                self.entry.text = "Error"
        elif instance.text == 'AC':
            self.entry.text = ""
        elif instance.text == '√':
            try:
                result = math.sqrt(float(self.entry.text))
                self.entry.text = str(result)
            except:
                self.entry.text = "Error"
        elif instance.text == 'log':
            try:
                result = math.log(float(self.entry.text))
                self.entry.text = str(result)
            except:
                self.entry.text = "Error"
        elif instance.text in ['sin', 'cos', 'tan']:
            try:
                result = getattr(math, instance.text)(float(self.entry.text))
                self.entry.text = str(result)
            except:
                self.entry.text = "Error"
        else:
            self.entry.text += instance.text

class CalculatorApp(App):
    def build(self):
        return ScientificCalculator()

if __name__ == '__main__':
    CalculatorApp().run()
