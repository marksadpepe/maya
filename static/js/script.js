async function handleInput(event) {
    if (event.key === "Enter") {
        await sendMessage();
    }
}

async function sendMessage() {
    let userInput = document.getElementById("user-input");
    let chatWindow = document.getElementById("chat-window");

    let userMessage = userInput.value.trim();
    if (userMessage !== "") {
        appendMessage("You", userMessage);
        userInput.value = "";

        const res = await fetch("/sendMessage", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: userMessage}),
        });

        const data = await res.json();
        appendMessage("Maya", data["message"]);

        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

function appendMessage(sender, message) {
    let chatWindow = document.getElementById("chat-window");
    let newMessage = document.createElement("p");
    newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatWindow.appendChild(newMessage);
}