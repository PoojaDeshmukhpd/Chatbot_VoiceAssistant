let subMenuText="";
function clicked(d)
{
let html='';
console.log("Done");
subMenuText=d.textContent;
  var inputElement = document.querySelector('input');
//
 const textToType = subMenuText; // Text to type in the input box
   let currentText = "";

      // Update the value of the input box with a slice of the text to type
      function typeText() {
        if (currentText.length < textToType.length) {
          currentText = textToType.slice(0, currentText.length + 1);
          inputElement.value = currentText;
        }
      }
setInterval(typeText, 100);
inputElement.value=subMenuText;


//const chatmessage = document.querySelector('.chatbox__messages');
//console.log(chatmessage);
// html+= '<div class="messages__item messages__item--operator" >' + subMenuText + '</div>';
console.log(d.textContent);
// chatmessage.innerHTML = html;
}
class Chatbox {

    constructor(){

        this.args = {
            openButton : document.querySelector('.chatbox__button'),
            chatBox : document.querySelector('.chatbox__support'),
            sendButton : document.querySelector('.send__button'),
            voiceButton : document.querySelector('.voice__button'),
            subMenuDiv : document.querySelector('.msg_item_visitor')
        }



        this.state = false;
        this.messages = [];
    }


    display(){
        const {openButton, chatBox, sendButton,voiceButton,subMenuDiv} = this.args;

        openButton.addEventListener('click',() => this.toggleState(chatBox))

        sendButton.addEventListener('click',() => this.onSendButton(chatBox))

        voiceButton.addEventListener('click',() => this.onVoiceButton(chatBox))

//        subMenuDiv.addEventListener('click',() => this.onSubMenuDiv(this))

        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({key}) => {

            if(key=='Enter') {
                this.onSendButton(chatBox)}

            })
        }






    toggleState(chatbox){
        this.state = !this.state;
        var top=document.querySelector(".top-banner");
        console.log(top)
//        top.style="vibility:hidden";


        //show or hides the box

        if(this.state){
         top.classList.add("hide-website");
            chatbox.classList.add('chatbox--active')

        }else{
            chatbox.classList.remove('chatbox--active')
            	top.classList.remove("hide-website");

        }
    }



    onSendButton(chatbox){
//    let text1="";
//        if(subMenuText=="")
//        {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value;
        if(text1==""){
            return;
        }
//        }
//        else{
//        text1=subMenuText;
//        }


        let msg1 = {name:"User", message:text1}
        this.messages.push(msg1);

        // http://127.0.0.1:5000/predict

        fetch($SCRIPT_ROOT + 'predict', {
            method: 'POST',
            body: JSON.stringify({message:text1}),
            mode: 'cors',
            headers: {
                'Content-Type' : 'application/json'
            }

       })
       .then(r => r.json())
       .then(r =>{
            let msg2 = {name:"SNJBIA", message: r.answer};
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            textField.value='';
       }).catch((error)=>{
            console.error('Error',error);
            this.updateChatText(chatbox);
            textField.value=''
       });

       $.ajax({
    type: 'GET',
    url: '/voice',
    success: function(response) {
        // Do something with the response
        console.log(response.result);
    }
});

    }

     onVoiceButton(chatbox){
         var textField = chatbox.querySelector('input');
          var speech = true;
          let text1;
    const outputDiv = document.getElementById('convert_text');
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

        textField.value = transcript;
        text1=transcript;
        console.log(transcript);
    });

    if (speech == true) {
        recognition.start();
    }
//
//
        if(text1==""){
            return;
        }

//
//       .then(r => r.json())
//       .then(r =>{
//            let msg2 = {name:"SNJBIA", message: r.answer};
//            this.messages.push(msg2);
//            this.updateChatText(chatbox);
//            textField.value='';
//       }).catch((error)=>{
//            console.error('Error',error);
//            this.updateChatText(chatbox);
//            textField.value=''
//       });
//
//       $.ajax({
//    type: 'GET',
//    url: '/voice',
//    success: function(response) {
//        // Do something with the response
//        console.log(response.result);
//    }
//});
//
//
    }


    updateChatText(chatbox){
        var html = '';
        const chatmessage = chatbox.querySelector('.chatbox__messages');

        this.messages.slice().reverse().forEach(function(item, number){
        console.log(item.name)
            if(item.name=="SNJBIA"){
                html+= '<div style="width: 650px; background: #c2d9e8; padding: 4px; border: 2px solid #1695b4;  border-bottom-right-radius: 20px; border-top-right-radius: 20px; border-bottom-left-radius: 20px;margin:10px;">' + item.message + '</div>'
//                html+= '<div class="messages__item messages__item--visitor">' + item.message + '</div>'

//                chatmessage.addChild(chatmessage.createElement('button'));
            }else{
                            html+= '<div class="messages__item messages__item--operator" >' + item.message + '</div>'
            }
        });

        //        const tempElement = document.createElement('div');
//        tempElement.innerHTML = html;

        chatmessage.innerHTML = html;
//        var i=0;
//        var txt=document.getElementByClass('messages__item--visitor').innerHTML;

//        var speed=70;
//
//        function typeWriter() {
//            if (i < txt.length) {
//                chatmessage.innerHTML += txt.charAt(i);
//                i++;
//                setTimeout(typeWriter, speed);
//              }
//}
//        typeWriter();





    }

}

const chatbox = new Chatbox();

chatbox.display()