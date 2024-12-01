import os
import requests
import click

API_URL = "http://example.com/api/compress"

def ls(ctx):
    files = [f for f in os.listdir() if f.endswith('.mp3')]
    if files:
        print("MP3 файлы в текущей директории:")
        for file in files:
            print(file)
    else:
        print("Нет MP3 файлов в текущей директории.")


def cd(ctx, path):
    try:
        os.chdir(path)
        
    except FileNotFoundError:
        print(f"Ошибка: директория {path} не найдена.")


def send(ctx, filename):
    if not os.path.exists(filename):
        print(f"Ошибка: файл {filename} не найден.")
        return

    if not filename.endswith('.mp3'):
        print("Ошибка: только файлы с расширением .mp3 поддерживаются.")
        return

    print(f"Отправка файла {filename}...") 

    with open(filename, 'rb') as file:
        files = {'file': (filename, file, 'audio/mpeg')}
        try:
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                with open(f"compressed_{filename}", 'wb') as compressed_file:
                    compressed_file.write(response.content)
                print(f"Файл успешно сжат и сохранён как 'compressed_{filename}'")
            else:
                print(f"Ошибка при отправке файла: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")            



