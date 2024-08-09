# 設定が基本必要なもの

# Web上でのパス
# Origin path.
# For Example: "/SimpleGitDocs"
OriginPath: str = ""

# ドメイン
# Domain
# For Example: "https://example.com"
URL_DOMAIN = "https://wiki.supernewroles.com"

# OGPの設定

# サイト名
# Site name
OGP_SITE_NAME = "SuperNewRolesWiki"

# Twitterのハンドルネーム
# Twitter HandleName
# For Example: "@example"
OGP_TWITTER_SITE = "@SNROfficials"

# リポジトリのパス
# Repository path
# For Example: "SimpleGitDocs/SimpleGitDocsDocument"
RepositoryPath: str = "SuperNewRoles/SuperNewRolesWiki"

# そのままでもいいもの

# ドキュメントのディレクトリ
# Directory of the documents
DocFolder = "Docs"
# アセットのディレクトリ
# Directory of the assets
AssetFolder: str = "Assets"
# テンプレートのHTMLのパス
# Path to the HTML template
TemplateHTMLPath: str = "template.html"
# 結果を出力するディレクトリ
# Output directory
ResultDirectory: str = "temp"
# 結果をプッシュするブランチ
# Branch to push the result
PushBranch: str = "gh-pages"
# Javascriptのパス
TemplateJavaScriptPath: str = "wiki.js"
# WebPに変換するか
# Whether to convert to WebP
IsConvertWEBP: bool = True
# 画像の最大横幅
# Maximum width of the image
Image_Max_Width_Px: int = 500
# 画像の品質
# Image quality
# 0-100
Image_Quality: int = 60
# 最大同時処理数
# Max threads
MaxThreads: int = 40
# マークダウン内のScriptタグをエスケープするか
# Whether to escape the script tag in the markdown
IsEscapeScript: bool = False
# AssetsでGitHackを使用するか
# Whether to use GitHack
IsUseGitHack: bool = False
# GitHackの対象ブランチ
# Branch of GitHack
GitHackBranch: str = "gh-pages"

# Twitterのカードタイプ
# Twitter card type
OGP_TWITTER_CARDTYPE = "summary_large_image"

# 変えないほうがいいもの

# HTML Template Settings
TEMPLATE_CONTENT: str = "{CONTENT}"
TEMPLATE_TITLE: str = "{TITLE}"
PATH_TEMPLATEJS_TAG = "{PATH_TEMPLATEJS}"
TEMPLATE_ORIGIN_PATH_TAG = "{ORIGIN_PATH}"
OGP_SITE_NAME_TAG = "{OGP_SITE_NAME}"
OGP_URL_BASE_TAG = "{OGP_URL_BASE}"
OGP_TWITTER_SITE_TAG = "{OGP_TWITTER_SITE}"
OGP_DESCRIPTION_TAG = "{OGP_DESCRIPTION}"
OGP_TWITTER_CARDTYPE_TAG = "{OGP_TWITTER_CARDTYPE}"