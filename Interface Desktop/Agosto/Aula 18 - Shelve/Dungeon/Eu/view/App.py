from textual.app import App
from view import TelaInicial, TelaCadastro, TelaJogo
from textual.binding import Binding


class GTA7THEGAME(App):

    SCREENS = {
        "tela_inicial": TelaInicial.TelaInicial,
        "tela_cadastro": TelaCadastro.TelaCadastro,
        "tela_jogo": TelaJogo.TelaJogo
    }

    BINDINGS = {
        Binding("n", "switch_screen('tela_cadastro')", "Tela de Cadastro"),
        Binding("j", "switch_screen('tela_jogo')", "Jogo"),
        Binding("escape", "switch_screen('tela_inicial')", "Tela Inicial")
    }

    TITLE = "GTA7THEGAME"

    def on_mount(self):
        self.push_screen("tela_inicial")
