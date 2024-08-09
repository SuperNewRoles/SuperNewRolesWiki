var files = [];
async function fetch_files()
{
    await fetch('{ORIGIN_PATH}/documents.list').then(res => res.text()).then(res =>
    {
        files = res.split("\n");
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
    var suggestions = [];
    for (var i = 0; i < files.length; i++)
    {
        // Katakana to hiragana
        const query_changed = KatakanaToHiragana(query.toLowerCase());
        const fileSplited = files[i].toLowerCase().split("/");
        const file = KatakanaToHiragana(fileSplited[fileSplited.length - 1]);
        if (file.includes(query_changed))
        {
            suggestions.push(files[i]);
        }
        if (suggestions.length >= max)
        {
            break;
        }
    }
    return suggestions;
}
// HTMLID_{index} という形で、ランダムに一つ表示する。
function RandomShow(HTMLId, len)
{
    var random = Math.floor(Math.random() * len);
    for (var i = 0; i < len; i++)
    {
        document.getElementById(HTMLId + "_" + i).style.display =
            i == random ? "block" : "none";
    }
}
function UpdateByStorage()
{
    // Local storage
    var darkMode = localStorage.getItem("DarkMode");
    if (darkMode == "true")
        document.body.classList.add("Dark");
    else
        document.body.classList.remove("Dark");
}
function UpdateStorage(key, value)
{
    // Local storage
    localStorage.setItem(key, value);
}
function UpdateHeadding()
{
    var headdings = document.getElementById("ContentsTableObject");
    for (var i = 0; i < headding_one.length; i++)
    {
        var headding = document.createElement("a");
        headding.innerText = headding_one[i];
        headding.classList.add("Button");
        headding.setAttribute("href", "#" + headding_one[i]);
        headdings.appendChild(headding);
        headdings.appendChild(document.createElement("br"));
    }
}
fetch_files();
let lastSearchText = "";
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("search").addEventListener("input", function () {
        var search = document.getElementById("search").value;
        if (search.length == 0)
        {
            document.getElementById("Suggestions").innerHTML = ""
            lastSearchText = "";
            return;
        }
        var suggestions = GetSuggestions(search, 5);
        if (suggestions.length == 0 && Math.abs(lastSearchText.length - search.length) < 2 && search.length > 1)
            return;
        var suggestionList = document.getElementById("Suggestions");
        suggestionList.innerHTML = "";
        for (var i = 0; i < suggestions.length; i++) {
            var suggestion = document.createElement("a");
            const SplitedSuggest = suggestions[i].split("/");
            suggestion.innerText = SplitedSuggest[SplitedSuggest.length - 1];
            suggestion.classList.add("Suggest");
            var url = "/" + suggestions[i];
            suggestion.setAttribute("href", url);
            suggestionList.appendChild(suggestion);
        }
        lastSearchText = search;
    });
    document.getElementById("Light-DarkToggleButton").addEventListener("click", function () {
        document.body.classList.toggle("Dark");
        // Set Cookie
        if (document.body.classList.contains("Dark")) {
            UpdateStorage("DarkMode", "true");
        } else {
            UpdateStorage("DarkMode", "false");
        }
    });
    UpdateByStorage();
    UpdateHeadding();
});