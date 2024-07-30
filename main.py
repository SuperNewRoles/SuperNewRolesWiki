import os
import shutil
import Constants
import glob
import markdown
from PIL.WebPImagePlugin import Image
import re
from pathlib import Path
import rjsmin
import datetime
import concurrent.futures
import xml.etree.ElementTree as ET

md: markdown.Markdown = markdown.Markdown(extensions=["extra"])

def DocLinks() -> list[str]:
    result: list[str] = []
    for filePath in glob.glob(f'./{Constants.DocFolder}/**', recursive=True):
        if os.path.isfile(filePath) and filePath.lower().endswith(".md"):
            fileName = os.path.relpath(filePath, Constants.DocFolder)
            fileName = "".join(os.path.splitext(fileName)[:-1])
            result.append(f"{fileName}")
    return result

docLinks = DocLinks()

def InitializeResultFolder():
    if os.path.exists(Constants.ResultDirectory):
        print(f"{Constants.ResultDirectory} is exitsts.")
        print(f"Removing {Constants.ResultDirectory}")
        shutil.rmtree(Constants.ResultDirectory)     
        print(f"Removed {Constants.ResultDirectory}")   
    os.mkdir(Constants.ResultDirectory)
    print("Initialized main module")

def GetFileData(path: str, defaultData: str) -> str:
    if not os.path.exists(path):
        return defaultData
    with open(path, "r") as file:
        return file.read()

def GenerateDocumentListFile():
    with open(f"{Constants.ResultDirectory}/documents.list", "w", encoding="utf-8") as docList:
        docList.write("\n".join(docLinks).replace("\\","/").replace("\r",""))

def convert_asset_paths(content, markdown_file_path):   
    # URLの正規表現パターン
    url_pattern = r'\(([^)]+)\)'
    
    def replace_url(match):
        url: str = match.group(1)
        if url.startswith("Assets/"):
            base_dir = os.path.dirname(markdown_file_path)
            new_url = RemoveExtension(os.path.relpath(url, base_dir)) + ".webp"
            return f'({new_url})'.replace("\\","/")
        return match.group(0)
    
    new_content = re.sub(url_pattern, replace_url, content)
    return new_content

def ProcessAssets():
    print("Processing assets")
    if not os.path.exists(f"{Constants.ResultDirectory}/Assets"):
        os.mkdir(f"{Constants.ResultDirectory}/Assets")
    for filePath in glob.glob(f'./{Constants.AssetFolder}/**', recursive=True):
        if os.path.isfile(filePath):
            print(f"Processing Asset:   {filePath}")
            # 相対パスを取得
            fileName = os.path.relpath(filePath, Constants.AssetFolder)
            # ディレクトリを生成
            os.makedirs(f"{Constants.ResultDirectory}/{os.path.dirname(fileName)}", exist_ok=True)
            print("IMAGE_SAVE:")
            print(Image.SAVE)
            # ファイルをコピー
            with open(filePath, "rb") as asset:
                if Constants.IsConvertWEBP and (fileName.endswith(".png") or fileName.endswith(".jpg")):
                    # PNGをWEBPに変換
                    with Image.open(asset) as img:
                        basePath: str = os.path.basename(filePath)
                        beforeName: str = "".join(basePath.split('.')[:-1])
                        # 横幅が設定したものを超える場合は比率を保ったまま縮小
                        if img.width > Constants.Image_Max_Width_Px:
                            # 比率を保つための新しい高さを計算
                            newHeight = int(img.height * (Constants.Image_Max_Width_Px / img.width))
                            img = img.resize((Constants.Image_Max_Width_Px, newHeight), Image.LANCZOS)
                        img.save(f"{Constants.ResultDirectory}/Assets/{beforeName}.webp", "WEBP", quality=Constants.Image_Quality)
                else:
                    # そのままコピー
                    with open(f"{Constants.ResultDirectory}/Assets/{fileName}", "wb") as newAsset:
                        newAsset.write(asset.read())
                        
def Replace_OGP(html: str) -> str:
    return html.replace(Constants.OGP_SITE_NAME_TAG, Constants.OGP_SITE_NAME)\
               .replace(Constants.OGP_URL_BASE_TAG, Constants.URL_DOMAIN)\
               .replace(Constants.OGP_TWITTER_SITE_TAG, Constants.OGP_TWITTER_SITE)\
               .replace(Constants.OGP_TWITTER_CARDTYPE_TAG, Constants.OGP_TWITTER_CARDTYPE)

def ToOGPDescription(text: str) -> str:
    # #や[]()や- などのマークダウンのタグと、HTMLタグならタグ全体を消す
    content: str = re.sub(r"#+\s", "", text)
    # []()なら、[]の中のみ()で囲って表示する
    content = re.sub(r"\[(.*?)\]\((.*?)\)", r"(\1)", content)
    content = re.sub(r"<.*?>", "", content)
    content = content.replace("- ","").replace("\n", "  ")
    # 200文字以内に収める
    return content[:200] if len(content) <= 300 else content[:300] + "..."

def Replace_Assets(html: str, path: str) -> str:
    return convert_asset_paths(html, path)

def replace_wikilinks(content, file_list, current_file):
    # 現在のファイルのディレクトリを取得
    current_dir = os.path.dirname(current_file)

    # ファイル名からパスを検索する関数
    def find_file_path(file_name, file_list):
        for file_path in file_list:
            if file_path.endswith(file_name):
                return file_path
        return None

    # 正規表現で[[...]]のパターンを探す
    def repl(match):
        wiki_link = match.group(1)
        file_path = find_file_path(wiki_link, file_list)
        if file_path:
            # 相対パスを計算
            relative_path = os.path.relpath(file_path, current_dir)
            # remove .html
            relative_path = "".join(os.path.splitext(relative_path)[:-1]).replace("\\","/")
            return f'[{wiki_link}]({relative_path}/index.html)'
        else:
            return match.group(0)  # 見つからなかった場合はそのまま返す

    # [[...]]を置換
    replaced_content = re.sub(r'\[\[(.*?)\]\]', repl, content)
    return replaced_content
def remove_tags(text):
    # タグを削除
    return re.sub(r'<[^>]+>', '', text)

def AddAnkerId(content: str) -> str:
    # h1, h2, h3 タグをそれぞれ処理
    content = re.sub(r'<h1>(.*?)</h1>', lambda m: f'<h1 id="{remove_tags(m.group(1))}">{m.group(1)}</h1>', content)
    content = re.sub(r'<h2>(.*?)</h2>', lambda m: f'<h2 id="{remove_tags(m.group(1))}">{m.group(1)}</h2>', content)
    content = re.sub(r'<h3>(.*?)</h3>', lambda m: f'<h3 id="{remove_tags(m.group(1))}">{m.group(1)}</h3>', content)
    return content

def convert_date_format(date_string: str) -> str:
    # Strip leading/trailing whitespace
    date_string = date_string.strip()
    # 変換のためのdatetimeオブジェクトを作成
    dt = datetime.datetime.strptime(date_string, '%a %b %d %H:%M:%S %Y %z')
    # 新しい形式の文字列に変換
    new_format_str = dt.strftime('%Y-%m-%dT%H:%M:%S%z')
    # タイムゾーンのコロンを追加
    new_format_str = new_format_str[:-2] + ':' + new_format_str[-2:]
    return new_format_str


def GetDocumentLastMod(filePath: str) -> str or None:
    result = os.popen(f"git log -1 --format=%cd -- ./{Constants.DocFolder}/{filePath}.md").read()
    if result == "":
        print(f"Get lastMod failed. filePath:{filePath}.md")
        return None
    result = convert_date_format(result)
    return result

def RemoveExtension(path: str) -> str:
    return ".".join(os.path.splitext(path)[:-1])

def Replace_Content(content: str, Template: str, filePath: str, fileName: str) -> str:
    # Get Document Title from File Path Extension off
    docTitle = RemoveExtension(os.path.basename(filePath))
    
    # Set Title and Description to OGP
    result = Template\
        .replace(Constants.TEMPLATE_TITLE, f"{docTitle} : {Constants.OGP_SITE_NAME}")\
        .replace(Constants.OGP_DESCRIPTION_TAG, ToOGPDescription(content))
    
    # Replace Assets Path
    content = Replace_Assets(content, filePath)
    
    # Escape Script Tags
    if Constants.IsEscapeScript:
        content = content\
            .replace('<script', '&lt;script')\
            .replace('</script>', '&lt;/script&gt;')
    
    # Replace Template Javascript
    FolderName = os.path.dirname(os.path.dirname(fileName)+".md")
    result = result.replace(Constants.PATH_TEMPLATEJS_TAG, Constants.OriginPath+"/wiki.js")
    
    # replace_wikilinks
    content = replace_wikilinks(content, docLinks, filePath)
    
    # Support Markdown in details Tag and div Tag
    content = content.replace('<details>', '<details markdown="1">')
    content = content.replace('<div', '<div markdown="1"')

    # Add title to Markdown
    if docTitle.lower() != "index" and docTitle.lower() != "404":
        content = f"# {docTitle}\n\n{content}"
    
    # Convert Markdown to HTML
    result = result.replace(Constants.TEMPLATE_CONTENT, md.convert(content))
    
    # Add anker id
    result = AddAnkerId(result)
    
    # Replace OGP Tags
    result = Replace_OGP(result)
    
    # Remove NewLine
    result = result.replace("\n","")
    
    return result

HTMLTemplate = GetFileData(Constants.TemplateHTMLPath, "{CONTENT}").replace("  "," ").replace("\n","")

def ProcessDocuments():
    print("Processing Documents")
    # Docsフォルダ内の一覧を取得
    for filePath in glob.glob(f'./{Constants.DocFolder}/**', recursive=True):
      # ファイルかどうかを判定
      if os.path.isfile(filePath) and filePath.lower().endswith(".md"):
         with open(filePath, "r", encoding="utf-8") as doc:
            content = doc.read()
            # 相対パスを取得
            fileName = os.path.relpath(filePath, Constants.DocFolder)
            print(f"Processing Document: {fileName}")
            # 拡張子を削除
            fileName = "".join(os.path.splitext(fileName)[:-1])
            # ディレクトリを生成
            if fileName != "index" and fileName != "404":
                os.makedirs(f"{Constants.ResultDirectory}/{fileName}/", exist_ok=True)
            
            if not (fileName == "index" or fileName == "404"):
                fileName += "/index"
            
            # ファイル名を使ってHTMLファイルを生成
            with open(f"{Constants.ResultDirectory}/{fileName}.html", "w", encoding="utf-8") as html:
                html.write(Replace_Content(content, HTMLTemplate, filePath, fileName))
    GenerateDocumentListFile()
    GenerateFolderDocuments()

def GenerateFolderDocuments():
    # 各フォルダのindex.htmlを生成
    writes = {}
    for folder in glob.glob(f'./{Constants.ResultDirectory}/**', recursive=True):
        if os.path.isdir(folder) and not os.path.exists(f"{folder}/index.html"):
            print(f"Processing Folder: {folder}")
            # フォルダ名を取得
            folderName = os.path.relpath(folder, Constants.ResultDirectory)
            # フォルダ名を使ってHTMLファイルを生成
            content = """# ドキュメント一覧
## [前に戻る](../index.html)"""
            # フォルダ内のフォルダ一覧を取得する
            for doc in glob.glob(f'{folder}/**'):
                if os.path.isdir(doc) and not os.path.exists(f"{doc}/index.html"):
                    # docLinks内に存在するフォルダのみリンクを生成
                    docName = os.path.relpath(doc, folder)
                    content += f"\n- Folder:[{docName}](./{docName}/index.html)"
            
            # フォルダ内のフォルダ一覧を取得する
            for doc in glob.glob(f'{folder}/**'):
                if os.path.isdir(doc) and os.path.exists(f"{doc}/index.html"):
                    # docLinks内に存在するフォルダのみリンクを生成
                    docName = os.path.relpath(doc, folder)
                    content += f"\n- [{docName}](./{docName}/index.html)" 
            
            writes[f"{folder}/index.html"] = Replace_Content(content, HTMLTemplate, folder+"/index.html", folderName)
    
    for key in writes.keys():
        with open(key, "w", encoding="utf-8") as html:
            html.write(writes[key])
def ProcessJavaScript():
    print("Processing JavaScript")
    if not os.path.exists(f"./{Constants.TemplateJavaScriptPath}"):
        print("Template JavaScript is not found. Skip processing JS.")
        return
    with open(f"./{Constants.TemplateJavaScriptPath}", "r", encoding="utf-8") as js:
        jsData = js.read()
        with open(f"{Constants.ResultDirectory}/wiki.js", "w", encoding="utf-8") as newJS:
            newJS.write(rjsmin.jsmin(jsData).replace("{ORIGIN_PATH}", Constants.OriginPath))

def ProcessRobotsTxt():
    print("Processing robots.txt")
    if not os.path.exists(f"./robots.txt"):
        print("robots.txt is not found. Skip processing robots.txt.")
        return
    with open ("./robots.txt", "r", encoding="utf-8") as robotsTxt:
        with open(f"{Constants.ResultDirectory}/robots.txt", "w") as robotsTarget:
            robotsTarget.write(robotsTxt.read().replace(Constants.OGP_URL_BASE_TAG, Constants.URL_DOMAIN))

def ProcessSiteMap():
    print("Processing sitemap.xml")
    # LastModを事前に複数スレッドで取得しておく
    # 最大同時実行数は10
    LastMods = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=Constants.MaxThreads) as executor:
        futures = {executor.submit(GetDocumentLastMod, doc): doc for doc in docLinks}

        for future in concurrent.futures.as_completed(futures):
            task_id = futures[future]
            try:
                result = future.result()
                LastMods[task_id] = result
                print(f"Processed GetLastMod: {task_id}({result})")
            except Exception as exc:
                print(f"Task {task_id} generated an exception: {exc}")
    
    LastModKeys = LastMods.keys()

    # Generate Sitemap
    with open(f"./{Constants.ResultDirectory}/sitemap.xml", "w", encoding="utf-8") as sitemap:
        sitemap.write('<?xml version="1.0" encoding="UTF-8"?>')
        sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
        for doc in docLinks:
            docPath: str = doc.replace("\\", "/").replace("&","＆")
            if docPath == "404":
                continue
            if docPath == "index":
                docPath = ""
            print(f"Writing Sitemap: {doc}")
            docLinkText: str = "<url><loc>"
            docLinkText += Constants.URL_DOMAIN + "/" + docPath
            docLinkText += "</loc>"
            if doc in LastModKeys:
                docLinkText += f"<lastmod>{LastMods[doc]}</lastmod>"
            docLinkText += "</url>"
            sitemap.write(docLinkText.replace("\n",""))
        sitemap.write('</urlset>')
    print("Checking Generated Sitemap.")
    with open(f"./{Constants.ResultDirectory}/sitemap.xml", "r", encoding="utf-8") as sitemap:
        try:
            ET.fromstring(sitemap.read())
            print("Success: Sitemap is valid.")
        except ET.ParseError as e:
            print("Error!!!!!!!!!!")
            print("Sitemap is invalid.")
            print(e)
            
def main():
    InitializeResultFolder()
    ProcessAssets()
    ProcessDocuments()
    ProcessJavaScript()
    ProcessRobotsTxt()
    ProcessSiteMap()
    print("Finished")
    
if __name__ == "__main__":
    main()
else:
    print("main.py is imported as a module.")
