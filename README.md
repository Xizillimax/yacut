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

## Примеры работы API:

### Создание ссылки:

POST http://127.0.0.1:5000/api/id/

Пример запроса:
```
{
  "url": "string",
  "custom_id": "string"
}
```
Пример ответа:
```
{
  "url": "string",
  "short_link": "string"
}
```

### Получение полной ссылки:

GET http://127.0.0.1:5000/api/id/{short_id}/

Пример ответа:
```
{
  "url": "string"
}
```

### Получение сообщения об ошибки:

В случае отправки некорректного запроса сервер ответит сообщением об ошибке.
В данном сообщение будет написано, что пошло не так.

Пример ответа:
```
{
  "message": "string"
}
```

Автор - [Maxim Zelenin](https://github.com/Xizillimax)