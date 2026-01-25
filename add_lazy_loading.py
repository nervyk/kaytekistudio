#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Счётчик
lazy_count = 0

# Функция для замены img тегов
def add_lazy_loading(match):
    global lazy_count
    img_tag = match.group(0)
    
    # Пропускаем если уже есть loading атрибут
    if 'loading=' in img_tag:
        return img_tag
    
    # Пропускаем класс header-logo - он у самого верхнего, должен быть eager
    if 'header-logo' in img_tag:
        img_tag = img_tag.replace('>', ' loading="eager">')
        lazy_count += 1
        return img_tag
    
    # Остальным добавляем lazy
    img_tag = img_tag.replace('>', ' loading="lazy">')
    lazy_count += 1
    return img_tag

# Находим все img теги и добавляем loading
html = re.sub(r'<img[^>]*?/?>', add_lazy_loading, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Добавлено loading атрибутов: {lazy_count}")
