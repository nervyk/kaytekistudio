#!/usr/bin/env python3
"""Конверсия PNG/JPG в WebP с сохранением прозрачности"""

from PIL import Image
import os
from pathlib import Path

def convert_to_webp(input_path):
    """Конверсия изображения в WebP с правильной обработкой прозрачности"""
    try:
        img = Image.open(input_path)
        output_path = input_path.rsplit('.', 1)[0] + '.webp'
        
        # Проверяем наличие альфа-канала (прозрачность)
        has_alpha = img.mode in ('RGBA', 'LA', 'PA') or (img.mode == 'P' and 'transparency' in img.info)
        
        if has_alpha:
            # Для изображений с прозрачностью используем lossless
            img.save(output_path, 'WEBP', lossless=True, method=6)
            print(f"✓ {Path(input_path).name} → {Path(output_path).name} (lossless, прозрачность сохранена)")
        else:
            # Для остальных используем lossy с высоким качеством
            # Переводим в RGB если нужно
            if img.mode in ('RGBA', 'LA', 'PA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if img.mode != 'P' else None)
                background.save(output_path, 'WEBP', quality=90, method=6)
            else:
                img.save(output_path, 'WEBP', quality=90, method=6)
            print(f"✓ {Path(input_path).name} → {Path(output_path).name} (lossy, качество 90)")
        
        return True
    except Exception as e:
        print(f"✗ Ошибка при конверсии {input_path}: {e}")
        return False

# Конвертируем все PNG файлы в assets
assets_dir = Path('assets')
png_files = list(assets_dir.rglob('*.png'))

print(f"Найдено PNG файлов: {len(png_files)}\n")

success_count = 0
for png_file in sorted(png_files):
    if convert_to_webp(str(png_file)):
        success_count += 1
        # Удаляем исходный PNG
        png_file.unlink()

print(f"\n✅ Конвертировано: {success_count}/{len(png_files)} файлов")
