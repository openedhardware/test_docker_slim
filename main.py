import os
import threading
import time

import requests
from settings import BASE_MODEL_DIR, COCO_LABELS_URL


NODE_ID = os.environ.get('NODE_ID')
NODERED_URL = 'http://0.0.0.0:1880'


def get_node_config():
    headers = {"Node-RED-API-Version": "v2"}
    try:
        r = requests.get(f'{NODERED_URL}/flows', headers=headers)
        flows = r.json()['flows']
        if flows:
            for f in flows:
                if f['type'] == 'object-detect' and f['id'] == NODE_ID:
                    print(f'Parsed flow - {f}')
                    return f
    except Exception as e:
        print(f'Failed to download flow - {e}')


def download_model(model_name, device):

    folder = os.path.join(BASE_MODEL_DIR, f'{model_name}_{device}')
    os.makedirs(folder, exist_ok=True)

    print(f"Downloading label file - {COCO_LABELS_URL}")
    with open(os.path.join(folder, 'labels.txt'), 'wb') as f:
        r = requests.get(COCO_LABELS_URL)
        f.write(r.content)


class TestDockerSlim(threading.Thread):

    def run(self):
        config = get_node_config()

        # download the model
        model_name = config.get('model_name')
        detect_mode = str(config.get('detect_mode', '')).lower()
        download_model(model_name=model_name, device=detect_mode)

        while True:
            print("Finished!")
            time.sleep(1)


if __name__ == '__main__':

    t = TestDockerSlim()
    t.start()
