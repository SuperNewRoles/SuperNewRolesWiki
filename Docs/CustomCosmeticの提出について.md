# カスタムコスメティック提出 規約
## カスタムコスメティックの提出の仕方
- **※提出データに不備がある場合は実装出来ませんのであらかじめご了承ください。**
- 実装テストをし、作成者目線問題なければコスメティック画像と実装イメージ画像(スクリーンショット)と必要事項を記入したテキストデータをzipにまとめて送ってください。
- テキストデータには下記を記入してください
  - コスメティック名
  - 制作者名
  - 二次創作の場合はガイドラインを確認した上でガイドラインのURL
  - オリジナル、二次創作関わらずライセンス表記が必要な場合はライセンス表記の記載
  - コスメティックに使用しているオプション(adaptive等)の明記(なければ不要)

## 実装できないコスメティック
- 公序良俗に違反すると思われるデザイン(過度に性的、暴力的なもの)
- ガイドラインが存在しない版権の二次創作
- ガイドライン上不適切な使用と判断出来る二次創作
- 他者の権利を侵害するデザイン
- その他開発者側で不適切と判断したもの

## 免責事項
- 実装テストを十分に行わない状態での実装依頼における実機上での見た目の不備に関しては一切責任を持ちません
- 今後提出ガイドラインや規約を改定することがあります。規約や実装基準につきましては提出時のものが適用されますのであらかじめご了承ください
- コスメティックを実装したことによるトラブルにつきましては、実装ミスなどの不備を除き、基本的にSNR側は責任を持ちません
- SNR側の独断(主に権利侵害等が発覚したりなど)で実装したコスメティックを削除することがあります。あらかじめご了承ください

<hr>

# コスメティック 提出方法
## ハットの作成の仕方
- テンプレ画像を元にハットを作成してください。画像サイズは変えないようにしてください。作成出来る箇所は、
  - front(帽子基本画像、必須、プレイヤー前面に描画)
  - back(プレイヤー背面に描画)
  - flip(向かって左側を向いたときに表示、プレイヤー前面に描画)
  - flip_back(向かって左側を向いたときに表示、プレイヤー背面に描画)
  - climb(ハシゴ画像、登るときにプレイヤー前面に描画)
の5箇所となります。最低frontの1枚から実装出来ます。

- ハットには3つのオプションを設定出来ます。
  - adaptive(指定色で描画した部分をプレイヤーの色に合わせて変更。具体的な色は別画像参照)
  - bounce(帽子を跳ねさせるオプション。公式ハットの鉢植えなどの挙動)
  - behind(front画像をプレイヤー背面に描画。前面が要らないときに使用)

## バイザーの作成の仕方
- テンプレ画像を元にハットを作成してください。
- 画像サイズは変えないようにしてください。<br><br>
- 作成可能な箇所は, 以下の2箇所です。最低frontの1枚から実装出来ます。
  - front(バイザー基本画像、必須、プレイヤー前面に描画)
  - flip(向かって左側を向いたときに表示、プレイヤー前面に描画)<br><br>
- バイザーには2つのオプションを設定出来ます。
  - adaptive(指定色で描画した部分をプレイヤーの色に合わせて変更。具体的な色は別画像参照)
  - behindHats(バイザーをハットの裏に重ねて表示する。)

## コスメティックのテストの仕方
- 必ずコスメティックのテスト機能を用いて、実装テストをし、実装イメージを添えて提出してください。
- Among Us\SuperNewRoles\CustomHatsChacheの中にtestというフォルダを作成し、下記命名規則に沿って名前を調整した画像を入れ、起動し、フリープレイに入ると、ハットを着用した状態になります。ハット名は半角英数字で書くようにしてください。
  - front…コスメティック名.png
  - back…コスメティック名_back.png
  - flip…コスメティック名_flip.png
  - flip_back…コスメティック名_flip_back.png
  - climb…コスメティック名_climb.png
- 3つのオプションを指定する場合は、front画像に_で区切って追記してください。front画像のみでOKです。
  - 例：コスメティック名_adaptive.png

<hr>

# コスメティック作成にかかわる情報
## テンプレート
### ハット
| オプション | Front, Back | Climb |
|:--|:--|:--|
| **画像** | <img src="https://github.com/SuperNewRoles/SuperNewRoles/assets/104145991/6c4424a6-7208-474a-ae92-3a4745ceb8c6" alt="SNCTemplate_HatMain" title="SNCTemplate_HatMain"> | <img src="https://github.com/SuperNewRoles/SuperNewRoles/assets/104145991/f0fb33a4-ea16-4fc5-b3c2-fcf6db24b76f" alt="SNCTemplate_Climb" title="SNCTemplate_Climb"> |

- [Seono968](https://github.com/seono968)作成
- Climbテンプレートはv2022.9.20以降の仕様に合わされたものとなっております。

### バイザー
| オプション | Front |
|:--|:--|
| **画像** | <img src="https://github.com/SuperNewRoles/SuperNewRoles/assets/104145991/6c4424a6-7208-474a-ae92-3a4745ceb8c6" alt="SNCTemplate_VisorMain" title="SNCTemplate_VisorMain"> |

- [Seono968](https://github.com/seono968)作成

### adaptive属性
| 画像 |
|:--|
| <img src="https://github.com/SuperNewRoles/SuperNewRoles/assets/104145991/b029237b-a4c9-4568-bfb9-b4ad368014d0" alt="SNCTemplate_ColorGuide" title="SNCTemplate_ColorGuide"> |

- [Seono968](https://github.com/seono968)作成

## [カスタムコスメティックのデータ名について](https://discord.com/channels/1019959796289523832/1027563077941612654/1181084424364900496)
最近たくさんの実装依頼をいただいています。<br>
それに伴い、実装済みハットとのデータ名の競合確率が上がっていくため、今後新規ハット作成時には作者名や村名等を画像名に含めて頂けると助かります。<br><br>
```
例：
【作者名の場合】foxSON_adaptivue.png
  [SON] が作者名 ("Seono" の頭文字)
【村名の場合】TONseono.png
  [TON] が村名 ("Tondemo" の頭3文字)
```

もちろん強制ではありませんので、付けなくてもそこまで問題はありませんが、付けて頂けると実装時の手間が多少軽くなりますのでご協力いただけると幸いです。<br><br>

また、画像保存の際に拡張子が二重になってしまっているデータ(.png.pngなど)がたまにありますので、拡張子を表示して拡張子が二重になったりしていないかも確認して頂けると幸いです。<br><br>
Windows10の場合 => https://askpc.panasonic.co.jp/beginner/guide/eight02/2034.html <br>
Windows11の場合 => https://askpc.panasonic.co.jp/beginner/guide/win11_02/2405.html