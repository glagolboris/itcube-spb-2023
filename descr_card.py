from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (395, 600)

KV1 = """
MDScreen:
    FitImage:
        source: "background.png"
    MDLabel:
        text: "smf_name"
        halign: "center"
        font_name: "Roboto-Black"
        font_size: 32
        color: 1, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
    
    MDRaisedButton:
        text: "img"
        font_name: "Roboto-Black"                
        md_bg_color: .868, .868, .868, .8
        size_hint_x: .6
        size_hint_y: .4
        pos_hint: {"center_x": .5, "center_y": .6} 
        
    MDLabel:
        text: "Состав"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .35}
        font_size: 22
        font_name: "Roboto-Black"
        color: 1,1,1,1
    
    MDLabel:
        text: "Свекла, морковь, мясо: говядина"
        padding: 10
        halign: "justify"
        pos_hint: {"center_x": .5, "center_y": .28}
        font_size: 20
        font_name: "Roboto-Black"
        color: 1,1,1,1
    MDLabel:
        text: "Калории, ккл:"
        halign: "justify"
        padding: 5
        hint_size_x: .8
        hint_size_y: .1
        pos_hint: {"center_x": .53, "center_y": .2}
        font_size: 22
        font_name: "Roboto-Black"
        color: "#084C2B"
        
    MDLabel:
        text: "знач_ккл"
        halign: "justify"
        pos_hint: {"center_x": .9, "center_y": .2}
        font_size: 22
        font_name: "Roboto-Black"
        color: "#084C2B"
        
    MDLabel:
        text: "Есть в наличии"
        halign: "justify"
        pos_hint: {"center_x": 1.26, "center_y": .28}
        font_size: 16
        font_name: "Roboto-Black"
        color: "#084C2B"
        
    MDLabel:
        text: "Осталось мало"
        halign: "justify"
        pos_hint: {"center_x": 1.26, "center_y": .25}
        font_size: 16
        font_name: "Roboto-Black"
        color: "#FF6347"
        
    MDLabel:
        text: "Нет в наличии"
        halign: "justify"
        pos_hint: {"center_x": 1.26, "center_y": .22}
        font_size: 16
        font_name: "Roboto-Black"
        color: "#800000" 
        
    MDFillRoundFlatButton:
        text: "Добавить в корзину (цена - x руб.)"  
        font_name: "Roboto-Black"                
        md_bg_color: "#01A627"
        size_hint_x: .3
        size_hint_y: .1
        pos_hint: {"center_x": .5, "center_y": .1} 
    
    MDFloatingActionButton:
        pos_hint: {"center_x": .1, "center_y": .92}
        icon: "strelka.jpg"
        md_bg_color: 1, 1, 1
    
"""


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV1)

    # def build_1(self):
    #     return Builder.load_string(KV1)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
