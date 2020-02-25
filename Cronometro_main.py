"""

    Projeto: Cronometro com kivy
    Por: Marcilio

"""
# Importa o kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.uix.label import Label


# Classe CronoWidget
class CronoWidget(BoxLayout):

    # Cria uma variavel Numerica em kv lang
    cronoValue = NumericProperty()
    # Cria uma variavel String em kv lang
    cronoValueText = StringProperty()
    # Cria uma variavel Booleana em kv lang
    habilitarContagem = BooleanProperty

    # Função que da update na tela
    def update(self, *args):
        self.cronoValueText = str(round(self.cronoValue, 1))
        if self.habilitarContagem:
            self.cronoValue += 0.1

    # Função que ao pressionar "zerar" zera a contagem
    def zerar(self):
        print("'Zerar' pressionado!")
        if not self.habilitarContagem:
            self.cronoValue = 0

    # Função que ao pressionar "iniciar" inicia contagem
    def iniciar(self):
        print("'Iniciar' pressionado!")
        self.habilitarContagem = True

    # Função que ao pressionar "parar" para contagem
    def parar(self):
        print("'Parar' pressionado!")
        self.habilitarContagem = False

    # Função que ao pressionar "reiniciar" reinicia a contagem
    def reiniciar(self):
        print("'Reiniciar' pressionado")
        if not self.habilitarContagem:
            self.habilitarContagem = True


# Classe CronoApp é a classe main do kivy
class CronoApp(App):

    # Builda o app e seta o cronometro para atualizar a cada 0.1s
    def build(self):
        cronos = CronoWidget()
        cronos.cronoValue = 0
        cronos.habilitarContagem = False
        Clock.schedule_interval(cronos.update, 0.1)
        return cronos


# Inicializa o app buildado
CronoApp().run()
