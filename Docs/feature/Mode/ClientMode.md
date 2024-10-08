# 説明

- ホストだけでなく**参加者全員**が、<br>**同バージョンのSNR**及び**同バージョンのAmongUs**を導入していないとプレイができないモードです。

# 開始制限について
- ClientModeには開始制限が存在します。<br><br>
- ホストとMod導入状態が異なる参加者がいる場合、開始ボタンが消えます。
  - ホストとMod導入状態が異なる参加者
    - バニラ状態の参加者 & 他Mod導入者(Mod側の認識はバニラ参加者になる)
      - <img src="Assets/209705435-51aabeb9-f2f8-4449-a1e9-07a5167b7db1.png" alt="バニラ状態の参加者" title="バニラ状態の参加者" width="535" height="320"><br><br>
    - ホストと異なるバージョンのSNRを導入している参加者
      - <img src="Assets/209706242-4a86fdbf-f854-48b6-ba3a-612452c6fb06.png" alt="ホストと異なるバージョンのSNRを導入している参加者" title="ホストと異なるバージョンのSNRを導入している参加者" width="535" height="320"><br><br>
    - ホストとバージョンの数字は同じだが, コードが(使用しているdllファイルが)異なるSNRを導入している参加者
      - <img src="Assets/209705656-d4c17e58-6cbe-40c6-b8a9-6dc56d73da31.png" alt="ホストと異なるバージョンのSNRを導入している参加者" title="ホストと異なるバージョンのSNRを導入している参加者" width="535" height="320"><br><br>

# 強制退出について
## 強制退出が必要な理由
- [正常動作が保証できない状態](#正常動作が保証できない状態)で参加する事を防ぐ為。
- **他Mod導入者及びバニラプレイヤーに迷惑をかけないようにする為の仕様**。<br><br>

## 正常動作が保証できない状態
  - SuperNewRolesは[ClientMod]である為、導入したままバニラの部屋に参加した場合、正常に動作しません。<br><br>
  - SNRを導入したまま、他のHostModに参加した場合、正常に動作しません。
    - バニラ状態では送信しないRpcを、ゲストが送信する事になる為。
    - ホストが送信してきたRpcが、SNR側では別の意味を持つ事がある為。
    - ゲストSNR導入者が送信したRpcが、ホストが導入しているModでは別の意味を持つことがある為。
    - etc...<br><br>
  - SNRを導入したまま、他のClientModに参加した場合、正常に動作しません。
    - 他ClientModも同じModで参加する事が前提である為。<br><br>
    - バニラ状態では送信しないRpcを、ゲストが送信する事になる為。
    - Hostが送信してきたRpcが、SNR側では別の意味を持つ事がある為。
    - ゲストSNR導入者が送信したRpcが、Hostが導入しているModでは別の意味を持つことがある為。<br><br>
  - ホストが導入しているSNRのバージョンが自身が導入しているSNRバージョンと異なる部屋に参加した場合、正常に動作しません。<br><br>
  - ホストが導入しているAmongUsバージョンが自身が導入しているAmongUSバージョンと異なる部屋に参加した場合、正常に動作しません。
    - **正常動作しませんがこの場合は強制退出の理由に含んでおりません。ご自身での確認及び対応をお願いします**<br><br>

## 強制退出の条件
- ホストがSNRを導入していない場合。
  - <img src="Assets/209704236-d2d8a216-9351-465a-af52-eda523b1bb25.png" alt="ホストがSNRを導入していない場合" title="ホストがSNRを導入していない場合" width="535" height="320">
- ホストが導入しているSNRのバージョンが、自身が導入しているSNRバージョンと異なる場合。
  - <img src="Assets/209706368-e124b103-fa50-4502-b862-f527710a05ef.png" alt="ホストが導入しているSNRのバージョンが、自身が導入しているSNRバージョンと異なる場合" title="ホストが導入しているSNRのバージョンが、自身が導入しているSNRバージョンと異なる場合" width="535" height="320">
  - <img src="Assets/209705842-c3bd0487-6263-4993-b33f-4fe779610479.png" alt="ホストが導入しているSNRのバージョンが、自身が導入しているSNRバージョンと異なる場合" title="ホストが導入しているSNRのバージョンが、自身が導入しているSNRバージョンと異なる場合" width="535" height="320">