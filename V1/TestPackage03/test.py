import os
import yaml


print(os.path.join(os.path.dirname(__file__), '..', 'extract.yaml'))

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extract.yaml'))

data={"1231":"1231"}
with open(file_path, encoding="utf-8", mode="a+") as f:
    yaml.dump(data, stream=f, allow_unicode=True)
