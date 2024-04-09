# Проект сервис YaCut

## Описание
Проект YaCut — это сервис укорачивания ссылок.
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

## Технологии

- Python
- Flask

### Развертывание и запуск парсера

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Xizillimax/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции:

```
flask db upgrade
```

Запустить в терминале командой:
```
flask run
```


Автор - [Maxim Zelenin](https://github.com/Xizillimax)