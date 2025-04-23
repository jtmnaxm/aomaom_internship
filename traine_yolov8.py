from ultralytics import YOLO

# กำหนดพาธไปยังไฟล์ dataset.yaml ที่เตรียมไว้
dataset_yaml = '/home/aom/aomaom_internship/dataset.yaml'  # เปลี่ยนเป็นพาธที่ถูกต้อง

# โหลดโมเดล YOLOv8 (เลือกโมเดลที่ต้องการ เช่น yolov8n, yolov8s, yolov8m, yolov8l)
model = YOLO("yolov8n.pt")  # โมเดลขนาดเล็กที่สุด (สามารถเปลี่ยนเป็น yolov8s.pt, yolov8m.pt หรือ yolov8l.pt ได้)

# เริ่มต้นการเทรนโมเดล
model.train(data=dataset_yaml, epochs=50, imgsz=640)

# หลังจากเทรนเสร็จ โมเดลที่ดีที่สุดจะถูกบันทึกไว้ในโฟลเดอร์ runs/train/exp/weights/best.pt

# หลังจากการเทรนเสร็จสิ้น สามารถโหลดโมเดลที่ดีที่สุดมาใช้ในการทำนายได้:
results = model.predict('/home/aom/aomaom_internship/datasets/images')  # ระบุพาธไปยังโฟลเดอร์ที่มีภาพใหม่ที่ต้องการทำนาย

# แสดงผลการทำนาย
results[0].show() 
