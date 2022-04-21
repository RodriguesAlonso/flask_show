"""Extensão Flask"""

def init_app(app): #Inicialização de extensões
    @app.route('/')
    def index():
        return "Hello World"