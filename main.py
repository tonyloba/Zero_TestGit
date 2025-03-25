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

# Created In Dev Branch:

def export_file(file_path, content):
    """Экспортирует строку в текстовый файл."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return "Файл успешно сохранён."
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Created In Dev 2 Branch:

def count_lines_in_file(file_path):
    """Подсчитывает количество строк в текстовом файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"