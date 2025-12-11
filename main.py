from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)

        self.label = Label(
            text='Привет из Windows 7 🖖',
            font_size=32,
            color=(0.3, 0.7, 1, 1),
            halign='center',
            valign='middle'
        )
        self.label.bind(size=self._update_text_size)

        button = Button(
            text='Нажми меня!',
            font_size=24,
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.on_button_click)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def _update_text_size(self, instance, value):
        self.label.text_size = instance.size

    def on_button_click(self, instance):
        self.label.text = 'APK собран через GitHub 🎉'


MyApp().run()
