import os


NODE_ID = os.environ.get('NODE_ID')

ROOT_DIR = f'/data/od_{NODE_ID}'

BASE_MODEL_DIR = os.path.join(ROOT_DIR, 'models')
os.makedirs(BASE_MODEL_DIR, exist_ok=True)

COCO_LABELS_URL = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
