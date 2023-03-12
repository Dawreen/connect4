# commands.py
from poetry.console import Application

@Application.command("hello")
def hello_command():
    print("Hello, world!")