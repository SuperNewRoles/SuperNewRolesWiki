var texts =
[
    "まあまあ、[2つを比べて](/Roles/Crewmate/天秤)落ち着きましょう。",
    "まあまあ、[攻撃を防いで](/Roles/Crewmate/賢者)落ち着きましょう。",
    "まあまあ、[ムキムキ](/Roles/Crewmate/ボディービルダー)しましょう。",
    "まあまあ、[ハンバーガーでも作って](/Roles/Crewmate/ハンバーガー屋)お金を稼ぎましょう。",
    "まあまあ、[空でも飛んで](/Roles/Crewmate/プテラノドン)落ち着きましょう。",

    "まあまあ、[だれかの役職でも入れ替えて](/Roles/Neutral/モイラ)落ち着きましょう。",
    "まあまあ、[サウナにでも入って](/Roles/Neutral/サウナー)落ち着きましょう。",
    "まあまあ、[ラバーズでも爆破して](/Roles/Neutral/爆ぜ師)落ち着きましょう。",
    "まあまあ、[写真でも撮って](/Roles/Neutral/写真家)落ち着きましょう。",
    "まあまあ、[金庫でも破って](/Roles/Neutral/金庫破り)落ち着きましょう。",
    "まあまあ、[犬でも飼って](/Roles/Neutral/パブロフの犬)落ち着きましょう。",
    "まあまあ、[水に隠れて](/Roles/Neutral/マグロ)落ち着きましょう。",
    "まあまあ、[ダラダラと](/Roles/Neutral/ニート)しましょう。",

    "まあまあ、[横にでも動いて](/Roles/Impostor/カニ)落ち着きましょう。",
    "まあまあ、[波動砲でも打って](/Roles/Impostor/波動砲)落ち着きましょう。",
    "まあまあ、[ぬーん(´・ω・｀)](/Roles/Impostor/ぬーん)。",
    "まあまあ、[ワームホールでも置いて](/Roles/Impostor/ディメンションウォーカー)落ち着きましょう。",
    "まあまあ、[ハッキングでもして](/Roles/Impostor/イビルハッカー)落ち着きましょう。",
    "まあまあ、[バットでも持って](/Roles/Impostor/スラッガー)野球でもしましょう。",
    "まあまあ、[キノコでも栽培して](/Roles/Impostor/マッシュルーマー)食べましょう。",
    "まあまあ、[タスクでも盗って](/Roles/Impostor/泥棒)落ち着きましょう。"

]
document.addEventListener('DOMContentLoaded', function () {
    var RandomText = texts[Math.floor(Math.random() * texts.length)];
    // Parse Markdown
    RandomText = RandomText.replace(/\[(.*?)\]\((.*?)\)/g, "<a href='$2'>$1</a>");
    document.getElementById("RandomText").innerHTML = RandomText;
});