import React, { useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  return (
    <div className="App" style={{padding:'2rem'}}>
      counter : {count}
      <div style={{marginTop:'2rem'}}>
        <button id="plus" style={{marginRight:'2rem'}} onClick={() => setCount(count + 1)}>+</button>
        <button id="minus" onClick={() => setCount(count - 1)}>-</button>
      </div>
    </div>
  );
}

export default App;
