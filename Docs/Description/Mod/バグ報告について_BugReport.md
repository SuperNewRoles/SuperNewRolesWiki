# 頁案内
- [頁案内](#頁案内)
- [説明](#説明)
  - [報告場所](#報告場所)
  - [報告方法](#報告方法)
    - [テンプレート](#テンプレート)
  - [logの取得方法](#logの取得方法)
    - [自動的に保存されている物を取得する方法](#自動的に保存されている物を取得する方法)
    - [任意のタイミングでコマンドを使用して保存する方法](#任意のタイミングでコマンドを使用して保存する方法)
      - [保存方法](#保存方法)
        - [キーボードコマンド](#キーボードコマンド)
        - [チャットコマンド](#チャットコマンド)
      - [fileの取得方法](#fileの取得方法)
    - [リザルト画面遷移時に自動的にログを待避する方法](#リザルト画面遷移時に自動的にログを待避する方法)
    - [Among Us終了時に自動的にログを退避する方法](#AmongUs終了時に自動的にログを退避する方法)

# 説明
## 報告場所
- [SNR公式Discordサーバ](https://discord.gg/Cqfwx82ynN)の、[#バグ報告_bugreport]チャンネルでチケットを作成し、<br>作成されたチャンネルで報告を行ってください。
- GithubのIssuesでの報告は受け付けておりません。

## 報告方法
- テンプレートに情報を記載し、logを添付して報告を行ってください。

### テンプレート
```
[タイトル] 
[モード] 
[バージョン]
[内容]
[ログ]
```
## logの取得方法
### 自動的に保存されている物を取得する方法
- 此処に保存されているログは**再起動によって上書きされます**
  - バグ発生時, すぐ報告するようにして下さい。
  - もしくは, ゲーム終了後 別の場所に一時保管し, 上書きされることを防止するようにして下さい。
    - 以下の機能を使用する事で自動的に待避し、上書きを防止する事もできます。
      - [リザルト画面遷移時に自動的にログを待避する方法](#リザルト画面遷移時に自動的にログを待避する方法)
      - [Among Us終了時に自動的にログを退避する方法](#AmongUs終了時に自動的にログを退避する方法)
    - 以下の機能を使用する事で、ゲーム中に任意でログを待避し、上書きを防止する事もできます。
      - [任意のタイミングでコマンドを使用して保存する方法](#任意のタイミングでコマンドを使用して保存する方法)

<details><summary>自動的に保存されている物を取得する方法 説明</summary>

1. SNRが入っているフォルダを開く
   - <img src="Assets/209708969-533ab726-daa7-4305-a46a-5077f39b5a0f.png" alt="log取得方法_自動保存" title="log取得方法_自動保存" width="50%" height="50%">

2. その中のBeplnExフォルダを開く
   - <img src="Assets/209709081-2129d062-664f-40f2-87ec-20e8944c31ed.png" alt="log取得方法_自動保存" title="log取得方法_自動保存" width="25%" height="25%">
   - このスクリーンショットが正常にModが導入されている際のフォルダ構成です。
   - Modが起動できない場合此処のスクショとの比較おねがいします。

3. .LogOutput.logが有る為、それを開かずにDiscordにドラックアンドドロップで提出
   - <img src="Assets/209709133-d78dfc02-36ce-41f0-b020-f3ec5d638386.png" alt="log取得方法_自動保存" title="log取得方法_自動保存" width="25%" height="25%">

</details>

<hr>

### 任意のタイミングでコマンドを使用して保存する方法
- 保存方法は2種類あります。
- fileの保存場所のパスは``~\STEAM\steamapps\common\SNR導入Among Usフォルダ名\SuperNewRoles\SaveLogFolder``です。

#### 保存方法

<details><summary>保存方法 詳細</summary>

##### キーボードコマンド
- ``左Shift`` + ``右Shift`` + ``S``
  - <img src="Assets/215004469-9df426a9-e5c8-4581-aa2a-686253994979.png" alt="log保存方法_キーボードコマンド" title="log保存方法_キーボードコマンド" width="50%" height="50%">
##### チャットコマンド
- ``/sl``又は``/SaveLog``
  - <img src="Assets/215004670-7e1f850e-abcc-4c86-8aaf-56497d5e67fe.png" alt="log保存方法_チャットコマンド" title="log保存方法_チャットコマンド" width="50%" height="50%">
  - <img src="Assets/215004675-7bada639-6a0c-43e1-a884-25b38b919dc2.png" alt="log保存方法_チャットコマンド" title="log保存方法_チャットコマンド" width="50%" height="50%">
  - <img src="Assets/215004678-e0c4ed0c-a682-4b04-8c72-1bebfe75ab05.png" alt="log保存方法_チャットコマンド" title="log保存方法_チャットコマンド

</details>

<hr>

### リザルト画面遷移時に自動的にログを待避する方法
- Mod上の機能で、ゲーム終了時にログを待避する事ができます。
  - この方法の場合、リザルト画面に遷移しない終了方法では待避する事ができません。
    - 例
      - クラッシュ時
      - 回線落ち 及び エラー落ち時
      - ゲーム退出時

<details><summary>使用方法</summary>

#### 設定方法
- 1. modの設定から「試合終了時ログをコピーする」を有効にする
  - <img src="https://github.com/user-attachments/assets/db756b1e-7244-41ea-936b-8ccb89be4552" alt="試合終了時ログをコピーする" title="試合終了時ログをコピーする" width="500px">
- 2. ``~\STEAM\steamapps\common\SNR導入Among Usフォルダ名\SuperNewRoles\AutoSaveLogFolder``に待避される。
  - <img src="https://github.com/user-attachments/assets/c8b0b366-1f73-4274-8dcf-53cada21658d" alt="AutoSaveLogFolder" title="AutoSaveLogFolder" width="500px">
  - ファイル名は``yyyyMMdd_hhmm_SNR_vバージョン_機体情報(*1)_GameCount_x(*2)_master(*3)_LogOutput.log``になります
    - *1
      - Host : そのログがホスト時の物である事をしめします。
      - Guest : そのログがゲスト時の物である事をしめします。
    - *2
      - そのログが、Among Usを起動してから何試合目の物かが記載されます。
      - イントロ画面表示時にカウントされます
    - *3
      - ブランチ名が記載されます。
        - 基本的に``master``と表記されます。
        - FANBOXで公開している開発版はその時々の対応する名前になります。

</details>

<hr>

### AmongUs終了時に自動的にログを退避する方法
- アプリケーション終了時にログを退避し、上書きを防止するツールを提供しています。

#### ツール
- SNRを導入しているフォルダの Among Us.exeと同階層に置いて使用するバージョン
  - [AutomaticLogEvacuation_Ver_CD.zip](https://github.com/user-attachments/files/16312907/AutomaticLogEvacuation_Ver_CD.zip)
  - コード => https://github.com/SuperNewRoles/SuperNewRoles/blob/master/SNRDevTools/AutomaticLogEvacuation_Ver_CD.bat

<details><summary>使用方法</summary>

#### 使用方法

1. SNRが導入されているAmong Usフォルダの, Among Us.exeと同じ階層にバッチファイルを置く。
  - <img src="https://github.com/user-attachments/assets/b6ed9777-5abb-44e4-beda-3dd6fe4dcfd0" alt="" title="" width="500px">
2. バッチファイルをダブルクリックで起動する。
  - <img src="https://github.com/user-attachments/assets/505705df-73fa-4e46-87ea-b2e52ce10486" alt="" title="" width="500px">
3. Among Usを終了する(クラッシュも含む)
  - この画面がすぐ閉じて確認できないのは正常な挙動です。
  - <img src="https://github.com/user-attachments/assets/7e6b2666-3e24-47d3-8ad4-2494c540c2b9" alt="" title="" width="500px">
4. 退避先は``~\STEAM\steamapps\common\SNR導入Among Usフォルダ名\SuperNewRoles\AutoSaveLogFolder``です。
  - <img src="https://github.com/user-attachments/assets/14f3b32c-fc10-4b75-b3f8-446a00e93cd9" alt="" title="" width="500px">

</details>
