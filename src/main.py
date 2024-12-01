import sys
import os
import requests

API_URL = "http://localhost:8080/v1/compress-audio"

def printHelp():
    print("Использование bb <команда> [аргументы]\n")
    print("Команды:")
    print("  compress <имя_файла>        Сжать указанный mp3 аудиофайл")
    sys.exit()

def compressAudio(filename):
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
                base_name, _ = os.path.splitext(filename) 
                new_filename = f"{base_name}_compressed.mp3"
                with open(new_filename, 'wb') as compressed_file:
                    compressed_file.write(response.content)
                print(f"Файл успешно сжат и сохранён как '{new_filename}'")
            else:
                print(f"Ошибка при отправке файла: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к серверу: {e}")

def main():
    if len(sys.argv) < 2:
        printHelp()
              
    if sys.argv[1] in ["help", "--help"]:
        printHelp()
    
    if len(sys.argv) < 3:
         printHelp()

    command, arg = sys.argv[1], sys.argv[2]

    match command:
         case 'compress':
              compressAudio(arg)


if __name__ == "__main__":
    main()
