from ultralytics import YOLO

# โหลดโมเดลที่เทรนเสร็จ
model = YOLO("runs/detect/train/weights/best.pt")

# ทำนายภาพทั้งหมดในโฟลเดอร์ test_images แล้วเซฟผลไว้ในโฟลเดอร์ที่กำหนด
results = model.predict(
    source="/home/aom/aomaom_internship/datasets/images",  # โฟลเดอร์ภาพใหม่
    save=True,                                         # เซฟภาพผลลัพธ์
    project="runs/detect",                            # โฟลเดอร์หลักที่ใช้เก็บผล
    name="test_output",                               # โฟลเดอร์ย่อยที่ตั้งชื่อเอง
    save_txt=True,                                     # (ถ้าต้องการ) เซฟไฟล์ label เป็น .txt
    conf=0.25                                          # ตั้งค่า confidence threshold ตามต้องการ
)

# ถ้าอยากแสดงผลลัพธ์บนหน้าจอทีละภาพ
for r in results:
    r.show()
