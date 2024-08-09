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
    var headdings = document.getElementById("Headdings");
    for (var key in headding_dict)
    {
        if (key != "")
            Generate_Headding(key, headdings);
        for (var i = 0; i < headding_dict[key].length; i++) {
            Generate_Headding(headding_dict[key][i], headdings);
        }
    }
}
function Generate_Headding(key, headdings)
{
    var headding = document.createElement("a");
    headding.innerText = key;
    headding.classList.add("Button");
    headding.setAttribute("href", "#" + key);
    headdings.appendChild(headding);
}
function UpdateAnker() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            const headerOffset = 75; // 固定ヘッダーの高さに合わせる
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        });
    });
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
    UpdateAnker();
});