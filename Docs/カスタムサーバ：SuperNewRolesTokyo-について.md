# 謝辞
- **SuperNewRolesTokyoサーバの運営費は, FanBoxにてご支援いただいた中から捻出しております。**
- **支援者の皆様, ありがとうございます。**

## FanBoxについて
- SuperNewRolesは, [FANBOX](https://supernewroles.fanbox.cc)にて支援を受け付けております！
  - 詳細は[FANBOX(https://supernewroles.fanbox.cc)](https://supernewroles.fanbox.cc)でご覧ください！

# 接続方法
- SuperNewRolseを導入できるユーザの場合, SNRv2.2.0.1以降を起動すると自動的に, サーバリージョンに追加されます。<br><br>
- Android 及び iOS(iPhone, iPad) ユーザーは以下のリンクに接続する事で, サーバリージョンに追加されます。
  - https://add-cs.supernewroles.com/<br><br>
- switchユーザは接続する事ができません。

# カスタムサーバーでできること
- 16人以上での同時プレイ(/mp {人数}で最大人数を変更可能)

# SuperNewRolesTokyoサーバが選択できない問題について
- サーバリージョンがCustomServerのアドレスの入力ボックスと被り, SuperNewRolesTokyoサーバが選択できない問題について。
  - 以下の動作により, 対処をお願いいたします。

## 暫定対処法
- [ダウンロード](#ダウンロード)に掲載している``remove_region.zip``をダウンロードして展開した後, 中の``remove.bat``を実行して下さい。
- このbatファイルは, PC版 AmongUsのサーバリージョンを初期化する戻す物です。
  - [北米, 欧州, アジア] のバニラサーバのみに戻します。

### ダウンロード
[remove_region.zip](https://github.com/SuperNewRoles/SuperNewRoles/files/14623776/remove_region.zip)

### ``remove.bat``のコード
```bat
echo off
xcopy /s "regionInfo.json" "%appdata%\..\LocalLow\InnerSloth\Among Us"
pause
```

## 使用サーバー
- 処理サーバ：[Contabo](https://contabo.com/)のCPU6コア、メモリ16GB、東京サーバー
- リバースプロキシサーバー：[Vultr](https://www.vultr.com/)の東京サーバー