import traceback
import requests
import time
import json
import sys
import os
import codecs

def AddNewKey(data: dict, new: dict) -> dict:
    result = data.copy()
    for key, value in new.items():
        if isinstance(value, dict):
            result[key] = AddNewKey(result.get(key, {}), value)
        result.setdefault(key, value)
    return result

def CheckUpdate(filename: str, githuburl: str) -> bool:
    print(f'Checking update for {filename}...')
    try:
        if "/" in filename:
            os.makedirs("/".join(filename.split("/")[:-1]), exist_ok=True)
        for count, text in enumerate(filename[::-1]):
            if text == ".":
                filename_ = filename[:len(filename) - count - 1]
                extension = filename[-count - 1:]
                break
        else:
            extension = ""
        if extension in [".py", ".bat", ".txt", ".md", ".sh", ""]:
            if os.path.isfile(filename):
                with codecs.open(filename, "r", encoding='utf-8') as f:
                    current = f.read()
            else:
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(f'Failed to get data for {filename}\n')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text.encode(encoding='utf-8')
                with codecs.open(filename, "wb") as f:
                    f.write(github)
                with codecs.open(filename, "r", encoding='utf-8') as f:
                    current = f.read()
            github = requests.get(githuburl + filename)
            if github.status_code != 200:
                print(f'Failed to get data for {filename}\n')
                return None
            github.encoding = github.apparent_encoding
            github = github.text.encode(encoding='utf-8')
            if current.replace('\n', '').replace('\r', '').encode(encoding='utf-8') != github.decode().replace('\n', '').replace('\r', '').encode(encoding='utf-8'):
                print(f'Update found for {filename}!')
                print(f'Backuping {filename}...\n')
                if os.path.isfile(f'{filename_}_old{extension}'):
                    try:
                        os.remove(f'{filename_}_old{extension}')
                    except PermissionError:
                        print(f'Failed to remove file {filename}\n')
                        print(traceback.format_exc())
                try:
                    os.rename(filename, f'{filename_}_old{extension}')
                except PermissionError:
                    print(f'Failed to backup file {filename}\n')
                    print(traceback.format_exc())
                else:
                    with codecs.open(filename, "wb") as f:
                        f.write(github)
                    print(f'Update for {filename} done!\n')
                    return True
            else:
                print(f'No update for {filename}!\n')
                return False
        elif extension == ".json":
            if os.path.isfile(filename):
                with codecs.open(filename, "r", encoding='utf-8') as f:
                    current = json.load(f)
            else:
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(f'Failed to get data for {filename}\n')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text.encode(encoding='utf-8')
                with codecs.open(filename, "wb") as f:
                    f.write(github)
                try:
                    with codecs.open(filename, "r", encoding='utf-8') as f:
                        current = json.load(f)
                except json.decoder.JSONDecodeError:
                    with codecs.open(filename, "r", encoding='utf-8-sig') as f:
                        current = json.load(f)
            github = requests.get(githuburl + filename)
            if github.status_code != 200:
                print(f'Failed to get data for {filename}\n')
                return None
            github.encoding = github.apparent_encoding
            github = github.text.encode(encoding='utf-8')
            if current != json.loads(github.decode()):
                print(f'Update found for {filename}!')
                print(f'Backuping {filename}...\n')
                if os.path.isfile(f'{filename_}_old{extension}'):
                    try:
                        os.remove(f'{filename_}_old{extension}')
                    except PermissionError:
                        print(f'Failed to remove file {filename}\n')
                        print(traceback.format_exc())
                try:
                    os.rename(filename, f'{filename_}_old{extension}')
                except PermissionError:
                    print(f'Failed to backup file {filename}\n')
                    print(traceback.format_exc())
                else:
                    with codecs.open(filename, "wb") as f:
                        f.write(github)
                    print(f'Update for {filename} done!\n')
                    return True
            else:
                print(f'No update for {filename}!\n')
                return False
        elif extension == ".png":
            if os.path.isfile(filename):
                with open(filename, "rb") as f:
                    current = f.read()
            else:
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(f'Failed to get data for {filename}\n')
                    return None
                github = github.content
                with open(filename, "wb") as f:
                    f.write(github)
                with open(filename, "rb") as f:
                    current = f.read()
            github = requests.get(githuburl + filename)
            if github.status_code != 200:
                print(f'Failed to get data for {filename}\n')
                return None
            github = github.content
            if current != github:
                print(f'Update found for {filename}!')
                print(f'Backuping {filename}...\n')
                if os.path.isfile(f'{filename_}_old{extension}'):
                    try:
                        os.remove(f'{filename_}_old{extension}')
                    except PermissionError:
                        print(f'Failed to remove file {filename}\n')
                        print(traceback.format_exc())
                try:
                    os.rename(filename, f'{filename_}_old{extension}')
                except PermissionError:
                    print(f'Failed to backup file {filename}\n')
                    print(traceback.format_exc())
                else:
                    with open(filename, "wb") as f:
                        f.write(github)
                    print(f'Update for {filename} done!\n')
                    return True
            else:
                print(f'No update for {filename}!\n')
                return False
        else:
            print(f'Extension {extension} not supported!\n')
            return None
    except Exception:
        print(f'Error while checking update for {filename}\n')
        print(traceback.format_exc())
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <githuburl> <filenames...>")
        sys.exit(1)

    githuburl = sys.argv[1]
    filenames = sys.argv[2:]

    while True:
        for filename in filenames:
            CheckUpdate(filename, githuburl)
        print("All update finished")
        os.chdir(os.getcwd())
        os.execv(os.sys.executable,['python3', "-m", "pip", "install", "--user", "-U", "-r", "requirements.txt"])
        sys.exit(0)
