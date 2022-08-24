def returnJs():
    return """
<script>
window.addEventListener('load', function() {
    var startTestButton = top.document.getElementsByClassName("u-active-palette-1-light-1 u-border-none u-btn u-btn-round u-button-style u-hover-palette-1-light-1 u-palette-1-base u-radius-6 u-text-active-white u-text-body-alt-color u-text-hover-white u-btn-1")[0];
    
    startTestButton.addEventListener("click", ()=> {
        top.document.querySelector("section").scrollTo(0, 0);
        top.document.querySelectorAll(".stButton > button")[5].click();
    });
})
</script>"""