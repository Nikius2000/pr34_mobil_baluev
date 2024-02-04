from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class RainbowApp(App):
    colors = {
        'Красный': '#ff0000',
        'Оранжевый': '#ff8800',
        'Желтый': '#ffff00',
        'Зеленый': '#00ff00',
        'Голубой': '#00ffff',
        'Синий': '#0000ff',
        'Фиолетовый': '#ff00ff'
    }

    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.color_label = Label(text='Выберите цвет', font_size=40, size_hint=(1, 0.3))
        layout.add_widget(self.color_label)
        
        for color_name, color_code in self.colors.items():
            button = Button(text=color_name, background_normal='', background_color=self.hex_to_rgb(color_code))
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)
        
        return layout

    def on_button_press(self, instance):
        color_name = instance.text
        color_code = self.colors[color_name]
        self.color_label.text = color_name
        self.color_label.color = self.hex_to_rgb(color_code)

    def hex_to_rgb(self, hex_code):
        hex_code = hex_code.lstrip('#')
        return [int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2, 4)] + [1]

if __name__ == '__main__':
    RainbowApp().run()