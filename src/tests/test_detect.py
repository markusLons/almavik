import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ..detectorDrop import detectorDrop

import pkg_resources

file_path = pkg_resources.resource_filename("almavik", "exp1")

# Путь к тестовым изображениям
TEST_IMAGE_DIR = file_path

def test_shaded_contours():
    # Создаем объект класса detectorDrop
    detector = detectorDrop()

    # Создаем тестовое изображение
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    # Вызываем метод shaded_contours и проверяем результат
    result = detector.shaded_contours(image)
    assert result.shape == image.shape
    assert result.dtype == np.float64

def test_detectorDrop_initialization():
    # Создаем объект класса detectorDrop с тестовым путем к изображениям
    detector = detectorDrop(TEST_IMAGE_DIR)

    # Проверяем, что список изображений не пустой
    assert len(detector.img) > 0

    # Проверяем, что списки center_mass и img_contour также не пустые
    assert len(detector.center_mass) > 0
    assert len(detector.img_contour) > 0

def test_detectorDrop_methods():
    # Создаем объект класса detectorDrop с тестовым путем к изображениям
    detector = detectorDrop(TEST_IMAGE_DIR)

    # Проверяем, что методы работают без ошибок
    assert len(detector.img) == len(detector.img_contour) == len(detector.center_mass)

    # Проверяем, что все элементы в списке center_mass имеют правильный формат
    for item in detector.center_mass:
        assert isinstance(item, tuple)
        assert len(item) == 3
        assert isinstance(item[0], int)
        assert isinstance(item[1], int)
        assert isinstance(item[2], int)

    # Проверяем, что все элементы в списке img и img_contour являются изображениями
    for img, img_contour in zip(detector.img, detector.img_contour):
        assert isinstance(img, np.ndarray)
        assert isinstance(img_contour, np.ndarray)
        assert img.shape[2] == 3
        assert img_contour.shape[2] == 3

        # Проверяем, что изображения имеют правильный тип данных
        assert img.dtype == np.uint8
        assert img_contour.dtype == np.uint8

        # Проверяем, что изображения не являются пустыми
        assert img.size > 0
        assert img_contour.size > 0

def test_detectorDrop_process_images():
    # Создаем объект класса detectorDrop с тестовым путем к изображениям
    detector = detectorDrop(TEST_IMAGE_DIR)

    # Обрабатываем изображения и проверяем результаты
    for img, img_contour in zip(detector.img, detector.img_contour):
        assert img.shape == img_contour.shape

        # Проверяем, что изображения имеют правильный тип данных после обработки
        assert img.dtype == np.uint8
        assert img_contour.dtype == np.uint8

        # Проверяем, что изображения не являются пустыми
        assert img.size > 0
        assert img_contour.size > 0

        # Проверяем, что изображения имеют правильное количество каналов
        assert img.shape[2] == 3
        assert img_contour.shape[2] == 3

        # Проверяем, что обработанные изображения имеют правильный тип данных
        assert img_contour.dtype == np.uint8

        # Проверяем, что обработанные изображения не являются пустыми
        assert img_contour.size > 0

def test_detectorDrop_center_of_mass():
    # Создаем объект класса detectorDrop с тестовым путем к изображениям
    detector = detectorDrop(TEST_IMAGE_DIR)

    # Проверяем, что список center_mass не пустой
    assert len(detector.center_mass) > 0

    # Проверяем, что все элементы в списке center_mass имеют правильный формат
    for item in detector.center_mass:
        assert isinstance(item, tuple)
        assert len(item) == 3
        assert isinstance(item[0], int)
        assert isinstance(item[1], int)
        assert isinstance(item[2], int)

def test_plot_center_of_mass():
    # Создаем объект класса detectorDrop с тестовым путем к изображениям
    detector = detectorDrop(TEST_IMAGE_DIR)

    # Проверяем, что список center_mass не пустой
    assert len(detector.center_mass) > 0

    # Проверяем, что график успешно строится без ошибок
    detector.plot_center_of_mass()

    # Проверяем, что график отображается
    assert plt.fignum_exists(1)

