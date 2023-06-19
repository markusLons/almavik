import os
import shutil
import subprocess

# Папка, содержащая код проекта
project_folder = os.path.dirname(os.path.abspath(__file__))

# Папка, содержащая исходный код
src_folder = os.path.join(project_folder, 'src')

# Создаем временную папку для хранения скомпилированных файлов
build_folder = os.path.join(project_folder, 'build')
os.makedirs(build_folder, exist_ok=True)

# Компилируем все файлы .py в папке src
compiled_files = []
for root, dirs, files in os.walk(src_folder):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            output_file = os.path.join(build_folder, file[:-3] + '.pyc')
            subprocess.call(['python', '-m', 'py_compile', filepath, '-o', output_file])
            compiled_files.append(output_file)

# Копируем зависимости проекта во временную папку
dependencies_folder = os.path.join(project_folder, 'dependencies')
shutil.copytree(dependencies_folder, os.path.join(build_folder, 'dependencies'))

# Устанавливаем зависимости из файла requirements.txt
requirements_file = os.path.join(project_folder, 'requirements.txt')
subprocess.call(['pip', 'install', '-r', requirements_file, '-t', os.path.join(build_folder, 'dependencies')])

# Создаем файл spec для pyinstaller
spec_file = os.path.join(build_folder, 'project.spec')
with open(spec_file, 'w') as f:
    f.write('''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['ypprpo.py'], # Здесь указывается основной файл проекта
             pathex=['{build_folder}'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='project', # Имя выходного исполняемого файла
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
'''.format(build_folder=build_folder))

# Компилируем проект с помощью pyinstaller, используя созданный spec файл
subprocess.call(['pyinstaller', spec_file])

# Удаляем временную папку
shutil.rmtree(build_folder)

# Папка, содержащая скомпилированный exe файл
dist_folder = os.path.join(project_folder, 'dist')

print('Готово! Ваш исполняемый файл находится в папке', dist_folder)
