def returnJs():
    return """
<script>
window.onload = function() {
    var logo = parent.document.getElementsByClassName("u-image u-logo u-image-1")[0];
    var pages = parent.document.querySelectorAll(".stButton > button");
    var topBar = parent.document.querySelectorAll(".u-nav-item > button.u-nav-link");
    
    logo.addEventListener("click", ()=> {pages[6].click()});

    topBar[0].addEventListener("click", ()=> {pages[6].click()});
    topBar[1].addEventListener("click", ()=> {pages[5].click()});
    topBar[2].addEventListener("click", ()=> {pages[4].click()});

    topBar[3].addEventListener("click", ()=> {pages[6].click()});
    topBar[4].addEventListener("click", ()=> {pages[5].click()});
    topBar[5].addEventListener("click", ()=> {pages[4].click()});
}
</script>"""