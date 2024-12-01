import click
from cli.terminal import Terminal

@click.command()
def start_terminal():
    """Запуск интерактивного CLI терминала."""
    terminal = Terminal()
    terminal.run()

if __name__ == "__main__":
    start_terminal()
