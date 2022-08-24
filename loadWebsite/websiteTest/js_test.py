def returnJs():
    return """
<script>
window.addEventListener('load', function() {
    setTimeout(function(){
        var textArea = parent.document.getElementsByClassName("stTextArea");
        var ta = parent.document.querySelectorAll("textarea");

        console.log(textArea.length);
        console.log(ta.length);

        for (let i=0; i<textArea.length; i++) {
            ta[i].placeholder = "질문에 대한 답변을 적어주세요";
        }

        var submitResultButton = parent.document.querySelector(".u-btn");
    
        submitResultButton.addEventListener("click", ()=> {
            parent.document.querySelector("section").scrollTo(0, 0);
            parent.document.querySelectorAll(".stButton > button")[3].click();
        });
    }, 10);
})
</script>"""