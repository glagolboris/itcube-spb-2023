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
                pos_hint: {"center_x": .45, "center_y": .93}
                fill_color: 0, 0, 0, .4
                hint_text: "Найти..."
                helper_text: "поиск по каталогу блюд"
                helper_text_mode: "on_focus"
                mode: "round"
                
            MDScrollView:
                size_hint: 1, .8
                md_bg_color: 1, 1, 1, .3
                
                MDBoxLayout:
                    id: box
                    orientation: "vertical"
                    spacing: 15
                    padding: 15
                    
                    MDRaisedButton:
                        md_bg_color: .9, 1, .9, 1
                        elevation: 0
                        size_hint_y:None
                        height: 180
                        size_hint_x:None
                        width: 350
                        pos_hint: {"center_x": .5, "center_y": .9}
                        
                    MDRaisedButton:
                        md_bg_color: .9, 1, .9, 1
                        elevation: 0
                        size_hint_y:None
                        height: 180
                        size_hint_x:None
                        width: 350
                        pos_hint: {"center_x": .5, "center_y": .9}
                        
                               
                    
        MDBottomNavigationItem:
            name: "screen 2"
            text: "Корзина"
            icon: "basket_screen_icon.png"
            
            FitImage:
                source: 'background.png'
                
            MDLabel:
                text: "Корзина"
                font_name: "Roboto"
                font_size: "35sp"
                color: 1, 1, 1, 1
                pos_hint: {"center_x": .4, "center_y": .93}
                halign: "center"
                
            MDLabel:
                text: "В корзине пусто :("
                font_name: "pp_font.ttf"
                font_size: "20sp"
                color: 1, 1, 1, 1
                pos_hint: {"center_x": .55, "center_y": .6}
                halign: "justify"
                
            MDLabel:
                text: "добавьте позиции из меню"
                font_name: "pp_font.ttf"
                font_size: "20sp"
                color: 1, 1, 1, 1
                pos_hint: {"center_x": .55, "center_y": .55}
                halign: "justify"
                
        MDBottomNavigationItem:
            name: "screen 3"
            text: "Профиль"
            icon: "profile_screen_icon.png"
            
            FitImage:
                source: 'background.png'
            
            MDLabel:
                text: "Профиль"
                font_name: "pp_font.ttf"
                font_size: "35sp"
                color: 1, 1, 1, 1
                pos_hint: {"center_x": .57, "center_y": .9}
                halign: "justify"
                
            MDLabel:
                text: "Здравствуйте, name"
                font_name: "pp_font.ttf"
                font_size: "25sp"
                color: 1, 1, 1, 1
                pos_hint: {"center_x": .57, "center_y": .84}
                halign: "justify" 
            
            MDLabel:
                text: "phone_number"
                font_name: "pp_font.ttf"
                font_size: "20sp"
                color: .8, .8, .8, 1
                pos_hint: {"center_x": .57, "center_y": .79}
                halign: "justify"
                
            MDCard:
                md_bg_color: "C5C5C5"
                pos_hint: {"center_x": .25, "center_y": .65}
                size_hint: .4, .1
                elevation: 0
                
                MDLabel:
                    text: "Ваша скидка"
                    font_name: "Roboto"
                    font_size: "15sp"
                    color: "046A38"
                    
            MDRaisedButton:
                md_bg_color: "C5C5C5"
                pos_hint: {"center_x": .7, "center_y": .65}
                size_hint: .4, .1
                elevation: 0
                text: "История заказов"
                text_color: "046A38"
                
            MDRaisedButton:
                md_bg_color: "C5C5C5"
                pos_hint: {"center_x": .48, "center_y": .52}
                size_hint: .85, .1
                elevation: 0
                text: "Банковские карты"
                text_color: "046A38"
                
            MDRaisedButton:
                md_bg_color: "C5C5C5"
                pos_hint: {"center_x": .48, "center_y": .4}
                size_hint: .85, .1
                elevation: 0
                text: "Настройки"
                text_color: "046A38"
            
            MDRaisedButton:
                md_bg_color: "FF0000"
                pos_hint: {"center_x": .48, "center_y": .2}
                size_hint: .85, .1
                elevation: 0
                text: "Выйти"
                text_color: "046A38"
            
'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()


