click_to_record.addEventListener('click',function(){
    var speech = true;

    const convert_text= document.getElementById("convert_text");
    window.SpeechRecognition = window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();
    recognition.interimResults = true;

    recognition.addEventListener('result', e => {
        const transcript = Array.from(e.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join('')
            // if (outputDiv) {
            //     outputDiv.innerHTML = "Transcript: " + e.results[0][0].transcript;
                console.log(transcript);
        convert_text.textContent = transcript;
    });
    
    if (speech == true) {
        recognition.start();
    }
})