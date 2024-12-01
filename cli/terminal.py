import os
import click
from cli.commands import ls, cd, send

class Terminal:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.commands = {
            'ls' : 'Показать список MP3-файлов в текущей директории',
            'cd': 'Перейти в указанную директорию. Пример: cd <путь>',
            'send': 'Отправить MP3-файл на сервер. Пример: send <имя_файла>',
            'help': 'Показать список доступных команд',
            'exit': 'Выйти из терминала'
        }

    def run(self):
        print(f"Добро пожаловать в BeatsByte!")
        while True:
            command = input(f"{self.current_directory} > ").strip()
            self.execute_command(command)

    def show_help(self, _ctx=None):
        print("Доступные команды:")
        for command, description in self.commands.items():
            print(f"  {command} - {description}")        

    def execute_command(self, command):
        parts = command.split()
        if not parts:
            return

        cmd = parts[0]
        
        if cmd == "exit":
            print("Выход из терминала...")
            exit(0)

        elif cmd == "ls":
            ls(None)

        elif cmd == "cd" and len(parts) > 1:
            cd(None, parts[1])
            self.current_directory = os.getcwd()

        elif cmd == "send" and len(parts) > 1:
            send(None, parts[1])
        elif cmd == "help":
            self.show_help()
        else:
            print(f"Неизвестная команда: {cmd}")
