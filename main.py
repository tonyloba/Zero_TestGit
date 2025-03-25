# Created In Main Branch:

def import_file(file_path):
    """Импортирует содержимое текстового файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"