from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (395, 600)

KV1 = """
MDScreen:
    FitImage:
        source: "background_decr.png"
    MDLabel:
        text: "smf_name"
        halign: "center"
        font_name: "Roboto-Black"
        font_size: 32
        color: .016, .424, .224
        pos_hint: {"center_x": 0.5, "center_y": 0.9}

"""


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV1)

    # def build_1(self):
    #     return Builder.load_string(KV1)


if __name__ == '__main__':
    app = DemoApp()
    app.run()
