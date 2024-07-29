function sendMessage() {
    let inputValue = document.getElementById('input_text').value;

    if (inputValue === "")
        return;

    // Display user input in 'output'
    let ansDiv = document.createElement('div');
    ansDiv.className = 'answer';
    ansDiv.textContent = inputValue;
    document.getElementById('replies').appendChild(ansDiv);
    document.getElementById('chat_canvas').scrollTop = document.getElementById('chat_canvas').scrollHeight;

    const userInput = document.getElementById('input_text').value;
    document.getElementById('input_text').value = '';

    let repDiv = document.createElement('div');
    repDiv.className = 'reply';
    repDiv.textContent = "Thinking.....";  // Use 'pythonResponse' instead of 'data.output'
    document.getElementById('replies').appendChild(repDiv);
    document.getElementById('chat_canvas').scrollTop = document.getElementById('chat_canvas').scrollHeight;
    // Send user input to Flask server and get the chatbot's response
    fetch('/process_input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        pythonResponse = data.replies;
        console.log("Python Response:", pythonResponse);  // Add this line for debugging

        // Display chatbot's response in 'replies'
        repDiv.textContent = pythonResponse;  
        setTimeout(() => {
            repDiv.textContent = pythonResponse;  
        }, 1000);
        
        document.getElementById('chat_canvas').scrollTop = document.getElementById('chat_canvas').scrollHeight;
        
        
    });
}