import sys
import os
import requests
from pydub import AudioSegment
from pydub.playback import play

API_URL = "http://localhost:8080/v1/compress-audio"

def printHelp():
    print("Использование bb <команда> [аргументы]\n")
    print("Команды:")
    print("  compress <имя_файла> <уровень>  Сжать указанный mp3 аудиофайл с заданным уровнем сжатия (0, 1, 2)")
    print("  play <имя_файла>               Воспроизвести mp3 аудиофайл")
    sys.exit()

def compressAudio(filename, level):
    if not os.path.exists(filename):
        print(f"Ошибка: файл {filename} не найден.")
        return

    if not filename.endswith('.mp3'):
        print("Ошибка: только файлы с расширением .mp3 поддерживаются.")
        return

    if level not in ['0', '1', '2']:
        print("Ошибка: уровень сжатия должен быть 0, 1 или 2.")
        return

    print(f"Отправка файла {filename} с уровнем сжатия {level}...")

    with open(filename, 'rb') as file:
        files = {'file': (filename, file, 'audio/mpeg')}
        data = {'compress_degree': level}  # Уровень сжатия передаётся в запросе

        try:
            response = requests.post(API_URL, files=files, data=data)

            if response.status_code == 200:
                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}_compressed.mp3"
                with open(new_filename, 'wb') as compressed_file:
                    compressed_file.write(response.content)
                print(f"Файл успешно сжат и сохранён как '{new_filename}'")
            else:
                print(f"Ошибка при отправке файла: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

def playAudio(audiofile):
    try:
        print(f"Воспроизведение файла: {audiofile}")
        audio = AudioSegment.from_file(audiofile, format="mp3")
        play(audio)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{audiofile}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при воспроизведении: {e}")

def main():
    if len(sys.argv) < 2:
        printHelp()
              
    if sys.argv[1] in ["help", "--help"]:
        printHelp()
    
    command = sys.argv[1]

    match command:
        case 'compress':
            if len(sys.argv) < 4:
                print("Ошибка: недостаточно аргументов для команды 'compress'.")
                printHelp()
            filename = sys.argv[2]
            level = sys.argv[3]
            compressAudio(filename, level)
        case 'play':
            if len(sys.argv) < 3:
                print("Ошибка: недостаточно аргументов для команды 'play'.")
                printHelp()
            filename = sys.argv[2]
            playAudio(filename)
        case _:
            print(f"Ошибка: неизвестная команда '{command}'.")
            printHelp()

if __name__ == "__main__":
    main()
