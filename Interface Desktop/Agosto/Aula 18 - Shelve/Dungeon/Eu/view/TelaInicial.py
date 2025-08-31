from textual.widgets import Header, Footer, Static
from textual.screen import Screen
from textual.containers import VerticalGroup


class TelaInicial(Screen):

    CSS_PATH = "css/TelaInicial.tcss"

    titulo = '''
   /$$$$$$  /$$$$$$$$ /$$$$$$        /$$$$$$$$                                  
 /$$__  $$|__  $$__//$$__  $$      |_____ $$/                                  
| $$  \__/   | $$  | $$  \ $$           /$$/                                   
| $$ /$$$$   | $$  | $$$$$$$$          /$$/                                    
| $$|_  $$   | $$  | $$__  $$         /$$/                                     
| $$  \ $$   | $$  | $$  | $$        /$$/                                      
|  $$$$$$/   | $$  | $$  | $$       /$$/                                       
 \______/    |__/  |__/  |__/      |__/                                        
                                                                               
                                                                               
                                                                               
 /$$$$$$$$ /$$   /$$ /$$$$$$$$        /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$
|__  $$__/| $$  | $$| $$_____/       /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/
   | $$   | $$  | $$| $$            | $$  \__/| $$  \ $$| $$$$  /$$$$| $$      
   | $$   | $$$$$$$$| $$$$$         | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$   
   | $$   | $$__  $$| $$__/         | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/   
   | $$   | $$  | $$| $$            | $$  \ $$| $$  | $$| $$\  $ | $$| $$      
   | $$   | $$  | $$| $$$$$$$$      |  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$
   |__/   |__/  |__/|________/       \______/ |__/  |__/|__/     |__/|________/
                                                                               
                                                                               
                                                                               '''

    def compose(self):
        yield Header()
        with VerticalGroup():
            yield Static(self.titulo)
            yield Static("O Melhor GTA todos")
        yield Footer()

    def on_mount(self):
        self.sub_title = "Tela Inicial"
