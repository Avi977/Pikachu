from kivy.app import App
from kivy.core.window  import Window
#setting window interface
Window.size = 400,600
Window.clearcolor = .20, .60, .20, 1
import time

class Pikachu(App):
    '''Layout from pikachu.kv file'''

    def button1clicked(self):
        '''uses the attack that the user gave on pikachu'''
        time.sleep(0.5)#using time delay
        self.root.ids.pikachu.source= "attacked pikachu.jpg"
        self.root.ids.wild_text.text=f'You use  {self.root.ids.attack_name.text}  attack on Pikachu'
        self.root.ids.attack_name.text='' #clearing the text inputbox
    def button2clicked(self):
        '''throws the ball that the user gave on pikachu'''
        time.sleep(0.5)
        self.root.ids.pikachu.source = "pikachu hurt png.png"
        self.root.ids.wild_text.text = f'You throw a {self.root.ids.ball_name.text}  ball on Pikachu'
        self.root.ids.ball_name.text=''
    def button3clicked(self):
        '''user runs away'''
        time.sleep(0.5)
        self.root.ids.pikachu.source = "pikachu laugh.webp"
        self.root.ids.wild_text.text = "You Ran Away"
        self.root.ids.ball_name.text = ''
        self.root.ids.attack_name.text = ''


Pikachu().run()
