import os
import ast
from collections import Counter


API_COUNTER = Counter()


def extract_api(node):
    if isinstance(node, ast.Call):
        func = node.func

        if isinstance(func, ast.Attribute):
            names=[]

            while isinstance(func, ast.Attribute):
                names.append(func.attr)
                func=func.value

            if isinstance(func, ast.Name):
                names.append(func.id)

            names.reverse()

            api=".".join(names)

            if api.startswith("torch"):
                API_COUNTER[api]+=1


def scan_file(path):
    with open(path,"r",encoding="utf-8") as f:
        try:
            tree=ast.parse(f.read())
            for node in ast.walk(tree):
                extract_api(node)

        except Exception:
            pass


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CODE_DIR = os.path.join(BASE_DIR, "../reproduction_code")


for file in os.listdir(CODE_DIR):

    if file.endswith(".py"):
        scan_file(os.path.join(CODE_DIR, file))

for api,count in API_COUNTER.most_common():
    print(api,count)
