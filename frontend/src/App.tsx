import './App.css'
import { useState } from "react";

async function rap(maxTokens : number, setOutput: (v: string) => void) {
  const res = await fetch(`http://127.0.0.1:8000/rap?max_tokens=${maxTokens}`);

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

      <pre className="output">{output}</pre>
    </div>
  );
}

export default App
