def returnJs():
    return """
<script>
window.onload = function() {
    var logo = top.document.getElementsByClassName("u-image u-logo u-image-1")[0];
    var pages = top.document.querySelectorAll(".stButton > button");
    var topBar = top.document.querySelectorAll(".u-nav-item > button.u-nav-link");
    
    logo.addEventListener("click", ()=> {pages[0].click()});

    topBar[0].addEventListener("click", ()=> {pages[0].click()});
    topBar[1].addEventListener("click", ()=> {pages[1].click()});
    topBar[2].addEventListener("click", ()=> {pages[2].click()});

    topBar[3].addEventListener("click", ()=> {pages[0].click()});
    topBar[4].addEventListener("click", ()=> {pages[1].click()});
    topBar[5].addEventListener("click", ()=> {pages[2].click()});
}
</script>"""