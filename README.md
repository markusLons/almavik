# Алмавик

![Логотип Алмавик](formalization/logoza.png)
<br>
<div>
    <a href="https://hub.docker.com/repository/docker/markuslons/almavik"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Pulls"></a>
   <a href="https://pypi.org/project/almavik/"><img src="https://pypi.org/static/images/logo-small.2a411bc6.svg" alt="PyPi Pulls"></a>
   
  </div>
  <br>
Алмавик - программа для определения центра масс капли по изображению. Она предоставляет удобный интерфейс и функции обработки изображений, которые позволяют точно и быстро определить центр масс капли.

## Особенности

- **Определение центра масс**: Алмавик использует современные алгоритмы обработки изображений для точного определения центра масс капли.
- **Интерфейс**: Программа имеет интуитивно понятный интерфейс, который позволяет легко загружать изображения и просматривать результаты обработки.
- **Графическое представление**: Алмавик предоставляет графическое представление капли, позволяя визуально оценить ее форму и размер.

![Логотип Алмавик](formalization/int.jpg)

## Интерфейс:
- Кнопки "Previous Image" и "Next Image": отвечают за переключение картинок на предыдущую и следующую соответственно;
- Конпки "Enable Drop Contour mode" и "Disable Drop Contour mode": появляются в зависимости от включенного режима на данный момент, изначально показывается изображение без выделенного контура капли, но при нажатии на "Enable Drop Contour mode" он выделяется;
- Слайдер: необходим для быстрого переключения картинок, так как в нашей папке 401 изображение, слайдер помогает быстро перейти от первого изображения к последнему;
- График: на графике красной точкой обозначается нахождение центра масс на текущей картинке, 4 точки до нее относятся к предыдущим изображениям, а 5 точк после к следующим.

## Запуск

### Локальный запуск 
    1. Установите зависимости из файла requirements.txt, выполнив команду: 
    $ pip install -r requirements.txt
    2. Создайте папку "exp1" в корневой директории проекта. В этой папке будут храниться изображения.
    3. Для запуска Алмавик локально, выполните команду:
    $ python YPPRPO.py
### Запуск в Docker контейнере
    1. Загрузите Docker образ Алмавик из репозитория Docker Hub, выполнив команду: 
    $ docker pull markuslons/almavik
    2. Запустите контейнер, используя следующую команду: 
    $ docker run -it markuslons/almavik
### Запуск через pip
    Для скачивания проекта введите в терминале строку:
    $ pip install almavik
    Это автоматически установит все нужные зависимости проекта, также папку с тестовыми изображениями
    Чтобы запустить скачанную библиотеку, нужно создать и запустить python файл с данными строками кода:
    $ from almavik.YPPRPO import main 
    $ main()
    После запуска данного файла откроется дополнительное окно с последней версией проекта "Алмавик"
     
## Создатели 
<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/markusLons">
          <img src="formalization/markus.jpg" width="200px" alt="Markus">
        </a>
        <br />
        <sub><b>Markus</b></sub>
      </td>
      <td align="center">
        <a href="https://github.com/avdovichenko1">
          <img src="formalization/blubbery.jpg" width="200px" alt="Blubbery">
        </a>
        <br />
        <sub><b>Blubbery</b></sub>
      </td>
      <td align="center">
        <a href="https://github.com/ViktoriaTix">
          <img src="formalization/viktoriatix.jpg" width="200px" alt="ViktoriaTix">
        </a>
        <br />
        <sub><b>ViktoriaTix</b></sub>
      </td>
    </tr>
  </table>
</div>

## Ссылки
https://pypi.org/project/almavik/

https://hub.docker.com/repository/docker/markuslons/almavik
