from label_studio_sdk import Client
import json

# === ตั้งค่า ===
API_KEY = '6fd2471cec906b69ef5bf72141d50712427d97d8'
LABEL_STUDIO_URL = 'http://localhost:8080'
PROJECT_ID = 4 # เปลี่ยนให้ตรงกับโปรเจกต์ที่สร้างไว้

# === เชื่อมต่อกับ Label Studio ===
ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)


project = ls.get_project(PROJECT_ID)

# === โหลดไฟล์ JSON ที่แปลงไว้ ===
with open('labelstudio_data.json', 'r', encoding='utf-8') as f:
    tasks = json.load(f)

# === ส่งข้อมูลเข้า Label Studio ===
project.import_tasks(tasks)
print(f"✅ Import เสร็จแล้ว! ลองเปิดโปรเจกต์ ID {PROJECT_ID} ดูเลย")
