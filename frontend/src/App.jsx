import { useState, useEffect, useRef } from "react";
import "./App.css";

import botAvatar from "./assets/bot.png";
import userAvatar from "./assets/user.png";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const askQuestion = async () => {
    if (!question.trim() || loading) return;

    const userQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5001/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: userQuestion,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: data.answer,
          source: data.source,
        },
      ]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "Server Error!",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>ABC RAG Chatbot</h1>

      <div className="chat-box">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={
              msg.sender === "user"
                ? "message-row user-row"
                : "message-row bot-row"
            }
          >

            <img
              src={
                msg.sender === "user"
                  ? userAvatar
                  : botAvatar
              }
              alt=""
              className="avatar"
            />

            <div
              className={
                msg.sender === "user"
                  ? "user-message"
                  : "bot-message"
              }
            >

              <strong>
                {msg.sender === "user"
                  ? "You"
                  : "Bot"}
                :
              </strong>

              <br />

              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
              >
                {msg.text}
              </ReactMarkdown>

              {msg.sender === "bot" &&
                msg.source && (
                  <>
                    <hr />

                    <small>
                      📄 <b>Source:</b>

                      <br />

                      {msg.source}
                    </small>
                  </>
                )}

            </div>

          </div>

        ))}

        {loading && (

          <div className="message-row bot-row">

            <img
              src={botAvatar}
              alt=""
              className="avatar"
            />

            <div className="bot-message">

              <strong>Bot:</strong>

              <br />

              Thinking...

            </div>

          </div>

        )}

        <div ref={chatEndRef}></div>

      </div>

      <div className="input-area">

        <input
          type="text"
          placeholder="Ask anything..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
        />

        <button
          onClick={askQuestion}
          disabled={loading}
        >
          {loading
            ? "Sending..."
            : "Send"}
        </button>

      </div>

    </div>
  );
}

export default App;