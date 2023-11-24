from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 600)
KV = '''
MDScreen:
    MDBottomNavigation:
        panel_color: "#01A627"
        selected_color_background: "orange"
        text_color_active: "green"

        MDBottomNavigationItem:
            name: "screen 1"
            text: "Каталог"
            icon: "dishes_screen_icon.png"

            FitImage:
                source: "background.png"

            MDTextField:
                size_hint_x: None
                panel_color: "#01A627"
                width: 300
                pos_hint: {"center_x": .5, "center_y": .9}
                fill_color: 0, 0, 0, .4
                hint_text: "Найти..."
                helper_text: "поиск по каталогу блюд"
                helper_text_mode: "on_focus"

                mode: "round"       
                icon_left: "search_icon.png"


        MDBottomNavigationItem:
            name: "screen 2"
            text: "Корзина"
            icon: "basket_screen_icon.png"

            FitImage:
                source: 'background.png'

            MDLabel:
                text: "корзина"
                halign: "center"

        MDBottomNavigationItem:
            name: "screen 3"    
            text: "Профиль"
            icon: "profile_screen_icon.png"
            
            FitImage:
                source: 'background.png'

            MDLabel:
                text: "профиль"
                halign: "center"
'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
