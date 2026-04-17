async function sendMessage() {
    let input = document.getElementById("user-input");
    let chatBox = document.getElementById("chat-box");

    let message = input.value;

    chatBox.innerHTML += "<p><b>You:</b> " + message + "</p>";

    try {
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();

        chatBox.innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";
    } catch (error) {
        chatBox.innerHTML += "<p style='color:red;'>Error connecting to backend</p>";
        console.log(error);
    }

    input.value = "";
}