# register model 🏷️ ไฟล์ register_model.py คือ “บอก MLflow ว่าโมเดลนี้ใช้ได้แล้วนะ — เอาไปขึ้นทะเบียนไว้ในระบบ”

import json
import mlflow
import logging
import os

# Set up MLflow tracking URI
mlflow.set_tracking_uri("http://ec2-13-211-142-57.ap-southeast-2.compute.amazonaws.com:5000/")


# logging configuration
logger = logging.getLogger('model_registration')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

file_handler = logging.FileHandler('model_registration_errors.log')
file_handler.setLevel('ERROR')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_model_info(file_path: str) -> dict:
    """Load the model info from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logger.debug('Model info loaded from %s', file_path)
        return model_info
    except FileNotFoundError:
        logger.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred while loading the model info: %s', e)
        raise

def register_model(model_name: str, model_info: dict):
    """Register the model to the MLflow Model Registry."""
    try:
        model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"
        
        # Register the model
        model_version = mlflow.register_model(model_uri, model_name)
        
        # Transition the model to "Staging" stage
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name=model_name,
            version=model_version.version,
            stage="Staging"
        )
        
        logger.debug(f'Model {model_name} version {model_version.version} registered and transitioned to Staging.')
    except Exception as e:
        logger.error('Error during model registration: %s', e)
        raise

def main():
    try:
        model_info_path = 'experiment_info.json'
        model_info = load_model_info(model_info_path)
        
        model_name = "yt_chrome_plugin_model"
        # model_name = "my_model"
        register_model(model_name, model_info)
    except Exception as e:
        logger.error('Failed to complete the model registration process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()


# ใน MLflow Model Registry จะมีระบบคล้าย ๆ Git version:

# Version 1: โมเดลแรกที่ลงทะเบียน

# Version 2: โมเดลใหม่ที่ประเมินได้ดีกว่า

# สามารถตั้งสถานะได้ เช่น

# 🧪 Staging (ใช้ทดสอบ)

# 🚀 Production (ใช้งานจริง)

# 🗑️ Archived (เลิกใช้แล้ว

# 🚫 สิ่งที่ “จะไม่ได้” ถ้าไม่ register

# ❌ ไม่มี Model Registry

# MLflow จะไม่รู้ว่า “โมเดลนี้เป็นเวอร์ชันที่เท่าไหร่”

# ไม่สามารถติด tag ว่าเป็น “Production”, “Staging”, หรือ “Archived”

# ❌ ไม่สามารถใช้ “ชื่อโมเดล” อ้างอิงได้

# ถ้า register แล้วจะโหลดได้แบบนี้:

# mlflow.pyfunc.load_model("models:/yt_chrome_plugin_model/Production")


# แต่ถ้าไม่ register → ต้องใช้ run ID แบบยาว ๆ

# mlflow.pyfunc.load_model("runs:/e2c8a5e6b8f94b1ea63f5b09a0af7b22/lgbm_model")


# ❌ ไม่มีระบบจัดการเวอร์ชัน (Versioning)

# ไม่รู้ว่าโมเดลไหนใหม่สุด

# ไม่สามารถ promote/demote ระหว่าง “Staging → Production” ได้

# ❌ ยากต่อการ deploy แบบอัตโนมัติ

# ระบบ deployment ที่เชื่อมกับ MLflow (เช่น MLflow Serving, SageMaker, Airflow pipeline)
# มักจะดึงโมเดลจาก Model Registry โดยใช้ชื่อ + stage
# เช่น “โหลดโมเดล Production ล่าสุด”
# → ถ้าไม่ register ระบบเหล่านี้จะใช้ไม่ได้