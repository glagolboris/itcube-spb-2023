from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (395, 600)
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
                font_size: 40
                font_name: "Roboto-Black"
                color: 1,1,1,1
                
            MDLabel:
                text: "Здравствуйте, name"
                font_name: "Roboto-Black"            
                halign: "justify"
                pos_hint: {"center_x": .5, "center_y": .8}
                font_size: 20
                color: 1,1,1,1 
            
            MDLabel:
                text: "      +7 (***) ***-**-**"
                font_name: "Roboto-Black"                
                halign: "justify"
                pos_hint: {"center_x": .5, "center_y": .7}
                font_size: 18
                color: 1,1,1,1
                            
            MDRaisedButton:
                text: "Ваша скидка discount%"
                font_name: "Roboto-Black"                
                md_bg_color: .868, .868, .868, .8
                size_hint_x: .25
                size_hint_y: .1
                pos_hint: {"center_x": .28, "center_y": .6}                    
                    
            MDRaisedButton:
                text: "История заказов"
                font_name: "Roboto-Black"                                  
                md_bg_color: .868, .868, .868, .8
                size_hint_x: .38
                size_hint_y: .1
                pos_hint: {"center_x": .76, "center_y": .6}        
            
            MDRaisedButton:
                text: "Банковские карты"
                font_name: "Roboto-Black"                
                md_bg_color: .868, .868, .868, .8
                pos_hint: {"center_x": .5, "center_y": .45}  
                size_hint_x: 0.9
                size_hint_y: 0.1
                
            MDRaisedButton:
                text: "Настройки"
                font_name: "Roboto-Black"                
                md_bg_color: 217, 217, 217, .6
                size_hint_x: 0.9    
                size_hint_y: 0.1
                pos_hint: {"center_x": .5, "center_y": .3}

            MDRaisedButton:
                text: "Выйти"
                font_name: "Roboto-Black"                
                md_bg_color: 1, 0, 0, 1
                size_hint_y: 0.1
                size_hint_x: 0.4
                pos_hint: {"center_x": .25, "center_y": .1}                   
'''

KV1 = """
MDScreen:
    MDLabel:
        text: "smf_name"
        halighn: "center"
        text_color: .016, .424, .224
        
"""

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


    # def build_1(self):
    #     return Builder.load_string(KV1)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
