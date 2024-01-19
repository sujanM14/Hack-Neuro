import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    scrollToBottom();
  }, [chats]);

  const scrollToBottom = () => {
    const chatContainer = document.getElementById("chat-container");
    if (chatContainer) {
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  };

  const chat = async (e, message) => {
    e.preventDefault();

    if (!message) return;

    setIsTyping(true);

    let msgs = chats.slice(); // Create a copy of the chats array

    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");

    fetch("http://localhost:8000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: message, // Send the message as "query" to match the backend model
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        msgs.push({ role: "AI", content: data.result }); // Assuming the response structure is { "result": "response content" }
        setChats(msgs);
        setIsTyping(false);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <main>
      <h1>Hive Chatbot</h1>

      <section id="chat-container">
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p
                key={index}
                className={chat.role === "user" ? "user_msg" : "AI_msg"} // Add a class for AI messages
              >
                <span>
                  <b>{chat.role.toUpperCase()}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>

      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>

      <form onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Type a message here and hit Enter..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
    </main>
  );
}

export default App;
