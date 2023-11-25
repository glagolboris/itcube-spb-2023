from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

import random

#В этом приложении будет несколько экранов
#на каждом из экранов будет свой способ позиционирования элементов

#Загружаю разметку
Builder.load_string('''
<Main>:
    BoxLayout:
        padding:10
        orientation:'vertical'
        Button:
            text:'next screen'
            on_press:root.manager.current='second'
        Label:
            text:'This is RelativeLayout'
        ScrollView:
            size_hint_y:None
            height:root.height*0.8
            RelativeLayout:
                id:my_box
                size_hint_y:None
                height:1216

<Second>:
    BoxLayout:
        padding:10
        orientation:'vertical'
        Button:
            text:'next screen'
            on_release:root.manager.current='third'
            size_hint:(1,0.1)
        Label:
            text:'This is BoxLayout'
            size_hint:(1,0.2)
        BoxLayout:
            spacing:10
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'left top'
                Label:
                    text:'right top'
            BoxLayout:
                Label:
                    text:'left bottom'
                Label:
                    text:'right bottom'


<Third>:
    FloatLayout:
        BoxLayout:
            orientation:'vertical'
            size_hint:None,None
            size:(root.my_width-50,root.my_height*0.2)
            pos:(25,root.my_height*0.6)
            Button:
                text:'next screen'
                on_press:root.manager.current='fourth'
            Label:
                text:'This is FloatLayout'
        BoxLayout:
            id:my_box
            size_hint:None,None
            height:50
            width:70
            pos:(root.my_width/3,root.my_height/3)
            canvas.before:
                Color:
                    rgba:(1,1,0,1)
                Rectangle:
                    pos:my_box.pos
                    size:(my_box.width,my_box.height)
        BoxLayout:
            id:my_box1
            size_hint:None,None
            height:100
            width:30
            pos:(120,130)
            canvas.before:
                Color:
                    rgba:(1,0,0,1)
                Rectangle:
                    pos:my_box1.pos
                    size:(my_box1.width,my_box1.height)
        Label:
            text:'I just some label'
            size_hint:None,None
            width:200
            height:50
            pos:(20,70)

<Fourth>:
    GridLayout:
        cols:3
        id:this_layout

''')

class Main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #В этом классе я впервые использую RelativeLayout
        #Есть некоторые нюансы - нужно заранее знать конечный размер лейаута
        #а иногда это не всегда будет получаться
        #я взял грубо 1216 пикселей(вручную посчитал), ведь для ScrollView нужно указывать размер виджета, который в него вложен, иначе он его не будет прокручивать
        #в будущем подумаю, как можно сделать это динамически
        self.flag=True#с помощью этого бросаю виджеты то в левую колонку, то в правую
        posess_y1=1216#максимальная высота левой колонки
        posess_y2=1216#то же, только правой
        for i in range(16):#случайным образом выставляю высоту виджета(кнопки)
            num=random.choice((0,1))
            if num==1:
                my_height=150
            else:
                my_height=100
            if self.flag:#значит кидаем виджет в левую колонку
                posess_y1-=(my_height+2)#нужно помнить, что в kivy рисование происходит с левого нижнего угла, координаты которого 0 и 0
                #значит нужно отступить от верхней границы на выстоту кнопки с отступом в 2 пикселя

                #перед тем как задать позицию и размер виджета нужно дать ему size_hint=(None,None), а потом вручную задать позицию и размер, с необходимыми отступами
                self.ids.my_box.add_widget(Button(text=str(i+1),size_hint=(None,None),height=my_height,width=(Window.width/2)-10,pos=(0,posess_y1)))
                self.flag=False
            else:
                posess_y2-=(my_height+2)
                self.ids.my_box.add_widget(Button(text=str(i+1),size_hint=(None,None),height=my_height,width=(Window.width/2)-10,pos=(Window.width/2,posess_y2)))
                self.flag=True

class Second(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class Third(Screen):
    def __init__(self,**kwargs):
        #эти размеры нужны для того чтобы виджет не выходил за пределы экрана
        #создаю обязательно до super, иначе у меня не работает
        #в разметке всем виджетам задаю size_hint:None,None
        #а потом размещаю как мне нужно с заданными размерами
        self.my_height=Window.height
        self.my_width=Window.width
        super().__init__(**kwargs)


class Fourth(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.list_buttons=[
            '7','8','9',
            '4','5','6',
            '1','2','3',
            'None','0','None',
            ]
        for i in self.list_buttons:
            self.ids.this_layout.add_widget(Button(text=i,on_press=self.pressing))

    def pressing(self,instance):
        print(instance.text)
        self.manager.current='first'


class TestApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Main(name='first'))
        sm.add_widget(Second(name='second'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        return sm


if __name__=="__main__":
    TestApp().run()