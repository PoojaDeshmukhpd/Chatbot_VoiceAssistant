// create a new SpeechRecognition object
const recognition = new window.SpeechRecognition();

// set recognition options
recognition.lang = 'en-US'; // set language to English
recognition.interimResults = true; // enable interim results

// add event listeners
recognition.onresult = (event) => {
  const transcript = event.results[event.results.length - 1][0].transcript;
  console.log(`You said: ${transcript}`);
};

recognition.onerror = (event) => {
  console.error(event.error);
};

// start recognition
recognition.start();