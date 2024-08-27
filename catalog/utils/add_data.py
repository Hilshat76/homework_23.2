import json
import os


def add_to_json_file(name: str, phone: str, message: str):
    '''
    Функция для добавления данных в JSON файл
    '''

    file_name = 'data.json'

    # Определяем путь к директории data
    data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    # Указываем путь к файлу vacancy.json
    file_path = os.path.join(data_directory, file_name)

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        # Если файл не существует, создаем новый с пустым списком
        data = []
    else:
        # Если файл существует, загружаем его содержимое
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)

    # Добавляем новые данные в список
    id = len(data) + 1
    data.append({
        'id': id,
        'name': name,
        'phone': phone,
        'message': message
    })

    # Сохраняем обновленный список обратно в файл
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Данные успешно добавлены в файл {file_name}.")
