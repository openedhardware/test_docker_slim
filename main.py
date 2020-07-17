import os
import threading
import time
import requests


COCO_LABELS_URL = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
NODERED_URL = 'http://0.0.0.0:1880'


class TestDockerSlim(threading.Thread):

    def run(self):
        r = requests.get(f'{NODERED_URL}/flows', headers={"Node-RED-API-Version": "v2"})
        nodered_flows = r.json()['flows']
        print(f"Node-RED flows: {nodered_flows}")

        print(f"Downloading label file - {COCO_LABELS_URL}")
        with open(os.path.join('/data/', 'labels.txt'), 'wb') as f:
            r = requests.get(COCO_LABELS_URL)
            f.write(r.content)

        while True:
            print("Finished!")
            time.sleep(1)


if __name__ == '__main__':

    print("Starting Testing APP...")

    t = TestDockerSlim()
    t.start()
