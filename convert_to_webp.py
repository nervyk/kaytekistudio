#!/usr/bin/env python3
import os
from PIL import Image
import glob

# Пути к папкам
assets_dir = "assets"
quality = 80
max_width = 1920

def convert_to_webp(image_path):
    """Конвертирует PNG/JPG в WebP с оптимизацией размера"""
    try:
        img = Image.open(image_path)
        
        # Уменьшаем если больше max_width
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Конвертируем в RGB если нужно (для WebP)
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = rgb_img
        
        # Сохраняем в WebP
        webp_path = image_path.rsplit('.', 1)[0] + '.webp'
        img.save(webp_path, 'WEBP', quality=quality, method=6)
        
        # Удаляем оригинал
        os.remove(image_path)
        print(f"✓ {image_path} → {webp_path}")
        return True
    except Exception as e:
        print(f"✗ Ошибка {image_path}: {e}")
        return False

# Конвертируем все PNG/JPG файлы в WebP
png_files = glob.glob(f"{assets_dir}/**/*.png", recursive=True)
jpg_files = glob.glob(f"{assets_dir}/**/*.jpg", recursive=True)

total = len(png_files) + len(jpg_files)
converted = 0

for png_file in png_files:
    if convert_to_webp(png_file):
        converted += 1

for jpg_file in jpg_files:
    if convert_to_webp(jpg_file):
        converted += 1

print(f"\n✅ Конвертировано: {converted}/{total} файлов")
