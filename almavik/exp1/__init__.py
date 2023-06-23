import os

# Получение списка файлов .jpeg в папке exp1
image_files = [filename for filename in os.listdir(os.path.dirname(__file__)) if filename.endswith('.jpeg')]

# Импорт файлов .jpeg в модуль
for filename in image_files:
    name = os.path.splitext(filename)[0]
    globals()[name] = os.path.join(os.path.dirname(__file__), filename)
