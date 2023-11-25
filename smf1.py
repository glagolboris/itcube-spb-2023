from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 600)
KV = '''
MDScreen:
    FitImage:
        source: "background.png"
        
    MDCard:
        md_bg_color: 1, 1, 1, .6
        size_hint: 1, .95
        elevation: 0
        
    MDLabel:
        text: "dish_name"
        font_name: "Roboto"
        font_size: "30sp"
        color: "046A38"
        pos_hint: {"center_x": .5, "center_y": .85}
        halign: "center"
        
    MDRaisedButton:
        md_bg_color: "01A627"
        pos_hint: {"center_x": .5, "center_y": .25}
        size_hint: .4, .07
        elevation: 0
        text: "price"
        text_color: "046A38"
        
    FitImage:
        source: "roll.jpg"
        pos_hint: {"center_x": .5, "center_y": .85}
        size_hint: .4, .4
'''

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
