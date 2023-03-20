from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        # Create a vertical box layout
        box = BoxLayout(orientation='vertical')

        # Create the text input for the display
        self.display = TextInput(multiline=False, readonly=True, font_size=50, halign='right', size_hint_y=None, height=100)

        # Add the display to the box layout
        box.add_widget(self.display)

        # Create the grid layout for the buttons
        grid = GridLayout(cols=4, size_hint_y=2)

        # Create the number buttons and add them to the grid
        for i in range(1, 10):
            button = Button(text=str(i))
            button.bind(on_press=self.number_pressed)
            grid.add_widget(button)

        # Add the zero button to the grid
        button = Button(text='0')
        button.bind(on_press=self.number_pressed)
        grid.add_widget(button)

        # Create the operator buttons and add them to the grid
        for operator in ['+', '-', '*', '/']:
            button = Button(text=operator)
            button.bind(on_press=self.operator_pressed)
            grid.add_widget(button)

        # Add the clear button to the grid
        button = Button(text='C')
        button.bind(on_press=self.clear_pressed)
        grid.add_widget(button)


        button = Button(text='=')
        button.bind(on_press=self.equals_pressed)
        grid.add_widget(button)

        # Add the grid to the box layout
        box.add_widget(grid)

        return box

    def number_pressed(self, button):
        if self.display.text == '0':
            self.display.text = ''
        self.display.text += button.text

    def operator_pressed(self, button):
        if self.display.text == '':
            return
        self.operator = button.text
        self.first_number = float(self.display.text)
        self.display.text = ''

    def clear_pressed(self, button):
        self.display.text = '0'

    def equals_pressed(self, button):
        if self.display.text == '':
            return
        second_number = float(self.display.text)
        if self.operator == '+':
            result = self.first_number + second_number
        elif self.operator == '-':
            result = self.first_number - second_number
        elif self.operator == '*':
            result = self.first_number * second_number
        else:
            result = self.first_number / second_number
  
        self.display.text = str(result)

if __name__ == '__main__':
    CalculatorApp().run()
