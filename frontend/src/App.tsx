import './App.css'
import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;
async function rap(maxTokens : number, setOutput: (v: string) => void) {
  const res = await fetch(`${API_URL}/rap?max_tokens=${maxTokens}`);
  console.log(API_URL, res)

  const reader = res.body!.getReader();
  const decoder = new TextDecoder();

  let output = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    output += decoder.decode(value);
    setOutput(output);
  }
}


function App() {
  const [output, setOutput] = useState("");
  const [tokens, setTokens] = useState(100);

  return (
    <div className="app">
      <h1 className="title">RapGPT</h1>

        <span className="token-label">Max new tokens </span>
        <input
          type="number"
          value={tokens}
          onChange={e => setTokens(+e.target.value)}
          className="input" />
      <div>
      <button onClick={() => rap(tokens, setOutput)} className="rap-button">
        Rap!
      </button>
      </div>

      <pre>{output}</pre>
    </div>
  );
}

export default App
