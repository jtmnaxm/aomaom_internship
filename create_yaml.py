import yaml

# กำหนดค่าพาธและชื่อคลาส
dataset_config = {
    'path': '/home/aom/aomaom_internship/datasets',  # โฟลเดอร์หลักที่มี images/ และ labels/
    'train': 'images',  # โฟลเดอร์ย่อยสำหรับ train (ภายใต้ path)
    'val': 'images',    # ใช้ train เป็น val ชั่วคราว ถ้าไม่มีชุด val แยก
    'names': {
        0: 'cat',        # ชื่อคลาสตามที่ใช้ใน label
        1: 'dog'
    }
}

# สร้างไฟล์ .yaml
with open('dataset.yaml', 'w') as yaml_file:
    yaml.dump(dataset_config, yaml_file, default_flow_style=False)

print("สร้างไฟล์ dataset.yaml เสร็จแล้ว ✅")
