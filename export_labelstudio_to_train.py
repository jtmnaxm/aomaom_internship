import os
import cv2
import json
from label_studio_sdk import Client

# === CONFIG ===
API_KEY = '6fd2471cec906b69ef5bf72141d50712427d97d8'
LABEL_STUDIO_URL = 'http://localhost:8080'
PROJECT_ID = 4 # เปลี่ยนให้ตรงกับโปรเจกต์ที่สร้างไว้
OUTPUT_DIR = 'datasets/yolo_export'

# === ฟังก์ชันแปลง box จาก Label Studio เป็น YOLO ===
def xywh_percent_to_yolo(x, y, w, h):
    cx = x + w / 2
    cy = y + h / 2
    return cx, cy, w, h

# === เตรียมโฟลเดอร์ ===
images_dir = os.path.join(OUTPUT_DIR, 'images')
labels_dir = os.path.join(OUTPUT_DIR, 'labels')
os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

# === เชื่อมต่อ Label Studio ===
ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
project = ls.get_project(PROJECT_ID)
tasks = project.get_tasks()

# === Export ทีละ Task ===
for task in tasks:
    image_url = task['data']['image']  # รูปแบบ: /data/local-files/?d=/path/to/image
    image_path = image_url.split('=')[-1]
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)

    # คัดลอกภาพ
    dst_img_path = os.path.join(images_dir, name + ext)
    if not os.path.exists(dst_img_path):
        os.system(f'cp "{image_path}" "{dst_img_path}"')

    # Export label
    if not task['annotations']:
        continue

    results = task['annotations'][0]['result']
    label_lines = []

    for r in results:
        if r['type'] != 'rectanglelabels':
            continue
        value = r['value']
        x, y, w, h = value['x'], value['y'], value['width'], value['height']
        x /= 100
        y /= 100
        w /= 100
        h /= 100
        cx, cy, w, h = xywh_percent_to_yolo(x, y, w, h)

        label_name = r['value']['rectanglelabels'][0]
        class_id = 0  # หรือ mapping จากชื่อ label → class_id ถ้ามีหลายคลาส

        line = f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}"
        label_lines.append(line)

    label_path = os.path.join(labels_dir, name + '.txt')
    with open(label_path, 'w') as f:
        f.write('\n'.join(label_lines))

print("✅ Export เสร็จเรียบร้อย! พร้อมใช้เทรน YOLO")
