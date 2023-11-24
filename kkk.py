from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (366, 600)
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
                text: "Профиль"
                halign: "justify"
                pos_hint: {"center_x": .5, "center_y": .9}
                font_size: 24
                
            MDLabel:
                text: "Здравствуйте, name"
                halign: "justify"
                pos_hint: {"center_x": .5, "center_y": .75}
                font_size: 20
            
            MDLabel:
                text: "Здесь Ваш номер телефона"
                halign: "justify"
                pos_hint: {"center_x": .5, "center_y": .7}
                font_size: 18
            
            MDGridLayout:
                rows: 3
                cols: 2
                id: box
                adaptive_height: True
                spacing: 10
                padding: 10
                pos_hint: {"center_x": .5, "center_y": .7}
                MDRaisedButton:
                    text: "Ваша скидка discount%"
                    md_bg_color: "grey"
                    width: 100
                    height: 60
                    
                    
                MDRaisedButton:
                    text: "Ваша скидка discount%"
                    md_bg_color: "grey"
                    width: 100
                    height: 60            
                
                MDRaisedButton:
                    text: "Ваша скидка discount%"
                    md_bg_color: "grey"
                    width: 100
                    height: 60
                    
                MDRaisedButton:
                    text: "Ваша скидка discount%"
                    md_bg_color: "grey"
                    width: 100
                    height: 60        
            
'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
