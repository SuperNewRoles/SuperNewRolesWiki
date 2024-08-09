var files = []
async function fetch_files()
{
    await fetch('{ORIGIN_PATH}/documents.list').then(res => res.text()).then(res =>
    {
        files = res.split("\n")
    });
}
function KatakanaToHiragana(str)
{
    return str.replace(/[\u30a1-\u30f6]/g, function(match)
    {
        var chr = match.charCodeAt(0) - 0x60;
        return String.fromCharCode(chr);
    });
}
function GetSuggestions(query, max)
{
    console.log(query)
    var suggestions = []
    for (var i = 0; i < files.length; i++)
    {
        // Katakana to hiragana
        const query_changed = KatakanaToHiragana(query.toLowerCase())
        const fileSplited = files[i].toLowerCase().split("/")
        const file = KatakanaToHiragana(fileSplited[fileSplited.length - 1])
        if (file.includes(query_changed))
        {
            suggestions.push(files[i])
        }
        if (suggestions.length >= max)
        {
            break
        }
    }
    return suggestions
}
// HTMLID_{index} という形で、ランダムに一つ表示する。
function RandomShow(HTMLId, len)
{
    var random = Math.floor(Math.random() * len)
    for (var i = 0; i < len; i++)
    {
        document.getElementById(HTMLId + "_" + i).style.display =
            i == random ? "block" : "none";
    }
}
fetch_files()
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("search").addEventListener("input", function () {
        var search = document.getElementById("search").value;
        var suggestions = GetSuggestions(search, 5)
        var suggestionList = document.getElementById("Suggestions")
        suggestionList.innerHTML = ""
        for (var i = 0; i < suggestions.length; i++) {
            var suggestion = document.createElement("div")
            suggestion.innerText = suggestions[i]
            suggestion.classList.add("Suggestion");
            suggestionList.appendChild(suggestion)
        }
    });
    document.getElementById("Light-DarkToggleButton").addEventListener("click", function () {
        document.body.classList.toggle("Dark");
    });
});