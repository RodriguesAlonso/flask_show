import click
from flask_show.ext.db import db
from flask_show.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
         """Este comando inicializa o db"""
         click.echo("banco de dados criado")
         db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adicionar novo usuario"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f'Usuario {email} criado com sucesso!')

    @app.cli.command()
    def listar_pedidos():
         """Este comando inicializa o db"""
         click.echo("lista de pedidos")
    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuarios")