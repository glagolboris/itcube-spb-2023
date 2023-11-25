from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 600)
KV = '''
MDScreen:
    FitImage:
        source: "background.png"
        
    MDRaisedButton:
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .8, .2
        md_bg_color: "C5C5C5"
        
        FitImage:
            source: "roll.jpg"
            size_hint: .4, .5
            pos_hint: {"center_x": .1, "center_y": .5}
        
'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
