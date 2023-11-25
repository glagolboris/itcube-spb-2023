from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 230)
KV = '''
MDScreen:
    FitImage:
        source: "background.png"
        
    MDLabel:
        text: "Авторизация"
        font_name: "Roboto"
        font_size: "30sp"
        color: .8, .8, .8, 1
        pos_hint: {"center_x": .5, "center_y": .8}
        halign: "center"
        
    MDTextField:
        pos_hint: {"center_x": .5, "center_y": .65}
        panel_color: "#01A627"
        fill_color: 0, 0, 0, .4
        size_hint: .7, .1
        hint_text: "Логин"
        halign: "center"
        mode: "round"
        
    MDTextField:
        pos_hint: {"center_x": .5, "center_y": .5}
        panel_color: "#01A627"
        fill_color: 0, 0, 0, .4
        size_hint: .7, .1
        hint_text: "Пароль"
        halign: "center"
        mode: "round"
        
    MDRaisedButton:
        md_bg_color: "C5C5C5"
        pos_hint: {"center_x": .5, "center_y": .35}
        size_hint: .3, .1
        elevation: 0
        text: "Войти"
        text_color: "046A38"
'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()


