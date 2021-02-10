import os
import requests

model_name = os.environ.get('MODEL')

if model_name:
    url = "https://viso-public-storage.s3.eu-central-1.amazonaws.com/ObjDet/CPU/{}.tar.xz".format(model_name)
    print(f"Downloading - {url}")
    with open(f'/data/{model_name}.tar.gz', 'wb') as f:
        r = requests.get(url)
        f.write(r.content)
print("Finished!")
