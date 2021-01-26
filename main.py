import time
import requests


S3_BASE_URL = "https://viso-public-storage.s3.eu-central-1.amazonaws.com/ObjDet/CPU/{}.tar.xz"


def main():
    model_name = None
    r = requests.get('http://0.0.0.0:1880/flows')
    for f in r.json():
        if f['type'] == 'object-detection':
            print(f"Found a flow - {f}")
            model_name = f['model_name']
            break
    url = S3_BASE_URL.format(model_name)
    print(f"Downloading - {url}")
    with open(f'/data/{model_name}.tar.gz', 'wb') as f:
        r = requests.get(url)
        f.write(r.content)

    while True:
        print("Finished!")
        time.sleep(1)


if __name__ == '__main__':

    print("Starting Testing APP...")

    main()
