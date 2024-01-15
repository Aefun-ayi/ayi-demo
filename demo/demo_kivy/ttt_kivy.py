# 导入app类
from kivy.app import App
# 导入布局类
from kivy.uix.boxlayout import BoxLayout

# 导入控件
from kivy.uix.button import Button

import plyer




class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 指定属性
        bt = Button(text='Button 01')
        uid = plyer.uniqueid.id
        bb = Button(text=f'{uid}')
        # 添加到布局中
        self.add_widget(bt)
        self.add_widget(bb)


class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()



if __name__ == '__main__':
    BoxApp().run()