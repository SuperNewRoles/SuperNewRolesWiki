import os
import Constants
import glob
import requests
import re
import urllib.parse

def unEscapeAndWikiLink(match):
    return f"[[{urllib.parse.unquote(match.group(1))}]]"
os.makedirs("./DownloadAssets", exist_ok=True)
files = []
for filePath in glob.glob(f'./{Constants.DocFolder}/**', recursive=True):
    if os.path.isfile(filePath) and filePath.lower().endswith(".md"):
        files.append(filePath)
for filePath in glob.glob(f'./{Constants.DocFolder}/**', recursive=True):
    if os.path.isfile(filePath) and filePath.lower().endswith(".md"):
        # find URL startswith https://user-images.githubusercontent.com/
        with open(filePath, "r", encoding="utf-8") as file:
            content = file.read()
            url_pattern = r"https://user-images\.githubusercontent\.com/\d+/[a-zA-Z0-9\-\.]+"
            urls = re.findall(url_pattern, content)
            if len(urls) == 0 and \
                "github.com/SuperNewRoles/SuperNewRoles/wiki/" not in content and \
                "supernewroles.com/wiki" not in content:
                continue
            for url in urls:
                fileName = url.split("/")[-1]
                if not os.path.exists(f"./Assets/{fileName}"):
                    print(f"Downloading: {fileName}")
                    with open(f"./Assets/{fileName}", "wb") as file:
                        file.write(requests.get(url).content)
                # replace URL
                content = content.replace(url, f"Assets/{fileName}")
            # https://github.com/SuperNewRoles/SuperNewRoles/wiki/* convert To [[*]] and URL unescape
            content = re.sub(r"https://github\.com/SuperNewRoles/SuperNewRoles/wiki/([^ ]+)", unEscapeAndWikiLink, content)
            print(f"Writing: {filePath}")
            with open(filePath, "w", encoding="utf-8") as file:
                file.write(content)