import os
import threading
import time
import requests


COCO_LABELS_URL = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"


class TestDockerSlim(threading.Thread):

    def run(self):
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
