# KAYTEKI Studio

Официальный веб-сайт студии графического дизайна KAYTEKI.

## Структура проекта

```
site/
├── index.html          # Главная страница
├── styles.css          # Стили
├── assets/
│   └── images/        # Все изображения и иконки
├── .gitignore         # Git конфигурация
└── README.md          # Этот файл
```

## Локальный запуск

1. Откройте `index.html` в браузере или используйте Live Server VS Code

## Развертывание

### Шаг 1: Создание GitHub репозитория

1. Перейдите на https://github.com/new
2. Создайте новый репозиторий с названием `kaytekistudio`
3. Выберите "Public"
4. Не инициализируйте с README (репо уже инициализирован локально)

### Шаг 2: Загрузка на GitHub

После создания репозитория выполните в терминале:

```bash
cd d:\KAYTOKI\site
git remote add origin https://github.com/YOUR_USERNAME/kaytekistudio.git
git branch -M main
git push -u origin main
```

Замените `YOUR_USERNAME` на ваше имя пользователя GitHub.

### Шаг 3: Развертывание на Netlify

1. Перейдите на https://app.netlify.com
2. Нажмите "Connect to Git"
3. Выберите GitHub и авторизуйтесь
4. Выберите репозиторий `kaytekistudio`
5. Настройки деплоя:
   - **Build command**: оставьте пусто
   - **Publish directory**: `.` (корень проекта)
6. Нажмите "Deploy site"

### Шаг 4: Настройка кастомного домена

1. В Netlify перейдите в "Site settings" → "Domain management"
2. Нажмите "Add custom domain"
3. Добавьте `kaytekistudio.ru`
4. Следуйте инструкциям Netlify для настройки DNS у вашего регистратора

## Технологический стек

- HTML5
- CSS3 (с поддержкой современных браузеров)
- Vanilla JavaScript
- Google Fonts для типографики

## Контакты

- Telegram: [@kaytekistudio](https://t.me/kaytekistudio)

---

Развернут на Netlify: `https://kaytekistudio.netlify.app`
