import firebase_admin
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from firebase_admin import credentials
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from firebase_admin import db
from kivy.app import App


cred = credentials.Certificate('C:/Users/Home/Desktop/telalogin21-firebase-adminsdk-k33mc-5f8b5ebc52.json') 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://telalogin21-default-rtdb.firebaseio.com/'  
})


class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=[50, 20], spacing=10)
        Window.size = (400, 696)
        Window.clearcolor = (0.15, 0.15, 0.15, 1)

        layout.add_widget(Image(source='img/img_icon.png'))
        layout.add_widget(Label(text='CADASTRO', font_size=24, color=(1, 1, 1, 1)))

        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.senha_input = TextInput(hint_text='Senha', password=True, multiline=False)
        layout.add_widget(self.email_input)
        layout.add_widget(self.senha_input)

        self.error_label = Label(text='', color=(1, 0, 0, 1), font_size=14)
        layout.add_widget(self.error_label)

        buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        signup_button = Button(text='Cadastre-se', color=(0, 0, 0, 1), size_hint=(1, None), size=(450, 50),
                              background_color=(100, 100, 100, 1))
        signup_button.bind(on_press=self.cadastrar)
        login_button = Button(text='Login', color=(0, 0, 0, 1), size_hint=(1, None), size=(450, 50),
                               background_color=(100, 100, 100, 1))
        login_button.bind(on_press=self.ir_para_tela_login)
        buttons_layout.add_widget(signup_button)
        buttons_layout.add_widget(login_button)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)
         
    def cadastrar(self, instance):
        email = self.email_input.text
        senha = self.senha_input.text
        if email and senha:
            ref = db.reference('LOGIN')
            ref.push({
                'Email': email,
                'Senha': senha
            })
            print('Usuário cadastrado com sucesso!')
    def ir_para_tela_login(self, *args): 
        self.manager.current = "LOGIN"

class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=[50, 20], spacing=10)
        Window.clearcolor = (0, 0, 0, 1)

        layout.add_widget(Image(source="img/img_icon.png"))
        layout.add_widget(Label(text='LOGIN', color=(1, 1, 1, 1), font_size=24, bold=True))

        self.email_input = TextInput(hint_text='Login', multiline=False)
        self.senha_input = TextInput(hint_text='Senha', password=True, multiline=False)
        layout.add_widget(self.email_input)
        layout.add_widget(self.senha_input)

        self.error_label = Label(text='', color=(1, 0, 0, 1), font_size=14)
        layout.add_widget(self.error_label)

        buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        login_button = Button(text='Login', color=(0, 0, 0, 1), size_hint=(1, None), size=(450, 50),
                              background_color=(100, 100, 100, 1))
        login_button.bind(on_press=self.login)
        signup_button = Button(text='Cadastre-se', color=(0, 0, 0, 1), size_hint=(1, None), size=(450, 50),
                               background_color=(100, 100, 100, 1))
        signup_button.bind(on_press=self.cadastrar)
        buttons_layout.add_widget(login_button)
        buttons_layout.add_widget(signup_button)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def login(self, instance):
        email = self.email_input.text
        senha = self.senha_input.text
        ref = db.reference('LOGIN')
        users = ref.get()

        for user in users.values():
            if user['Email'] == email and user['Senha'] == senha:
                print("Login feito com sucesso")
                return
        print("Login não encontrado")

    def cadastrar(self, instance):
        self.manager.current = 'CADASTRO'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='LOGIN'))
        sm.add_widget(TelaCadastro(name='CADASTRO'))
        return sm

if __name__ == '__main__':
    MyApp().run()
