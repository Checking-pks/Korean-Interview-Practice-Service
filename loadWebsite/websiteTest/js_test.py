def returnJs():
    return """
<script>
window.addEventListener('load', function() {
    setTimeout(function(){
        var textArea = top.document.getElementsByClassName("stTextArea");
        var ta = top.document.querySelectorAll("textarea");

        console.log(textArea.length);
        console.log(ta.length);

        for (let i=0; i<textArea.length; i++) {
            ta[i].placeholder = "질문에 대한 답변을 적어주세요";
        }

        var submitResultButton = top.document.querySelector(".u-btn");
    
        submitResultButton.addEventListener("click", ()=> {
            top.document.querySelector("section").scrollTo(0, 0);
            top.document.querySelectorAll(".stButton > button")[6].click();
        });
    }, 10);
})
</script>"""