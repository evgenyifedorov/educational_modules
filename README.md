# " Образовательные модули"

Проект "Образовательные Модули" представляет собой небольшое веб-приложение, разработанное с использованием Django и Django Rest Framework.
Оно позволяет управлять учебными модулями каждый из которых содержит порядковый номер, название, описание, свой блок уроков и пользователей с различными правами доступа.

## Задача:

Целью проекта является реализация следующих функций для модели "Образовательные Модули":

CRUD операции: Создание (Create), Чтение (Read), Обновление (Update), Удаление (Delete) для каждого образовательного модуля.

Тестирование: Полностью покрыть все модели, сериализаторы и представления автоматизированными юнит-тестами.

## Стэк:

Python 3.12: Язык программирования, на котором основан проект.

Django: Высокоуровневый Python-фреймворк для веб-разработки.

Django Rest Framework: Набор инструментов для построения Web APIs на базе Django.

СУБД: PostgresSQL

Docker: Платформа для разработки, развертывания и управления приложениями в контейнерах


Код размещен в открытом репозитории на GitHub.

Документация: Создана документация по API redoc/swagger.

Автоматизированные юнит-тесты: Весь код покрыт автоматизированными юнит-тестами для обеспечения стабильности и надежности,

в файле coverage находиться читабельная информация о процентах покрытия тестами.

Оформление кода: Код оформлен согласно стандарту PEP8, чтобы обеспечить его читаемость и совместимость.

Readme файл: Предоставлен Readme файл, как этот, с описанием проекта, инструкциями по установке и запуску.

Использование Docker: В проекте использован Docker для упрощения процесса установки и запуска приложения.

## Установка и развертывание проекта:
Клонируйте репозиторий с github на локальный компьютер

Создайте виртуальное окружение командой python -m venv venv, /venv/Scripts/activate.(для venv)

Установите зависимости командой pip install requirements.txt

Создайте в корне проекта файл в .env и заполните его согласно шаблона в файле env.sample

## Команды для удобства(без контейнера):

python makemigrations, python migrate - для создания миграций в базу данных

python manage.py runserver для запуска проекта

python manage.py test, coverage run manage.py test, manage.py test coverage report - 

для проверки тестов и проверки процентов их покрытия

## Команды для удобства(с контейнером):

Соберите и поднимите docker-контейнер командой docker compose up --build
