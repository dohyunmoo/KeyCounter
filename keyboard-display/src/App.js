import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText] = useState('');

  const row1 = ["ESC", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
  const row2 = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE"]
  const row3 = ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"]
  const row4 = ["CAPS LOCK", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ENTER"]
  const row5 = ["L SHIFT", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "R SHIFT"]
  const row6 = ["L CTRL", "WIN", "L ALT", "SPACE", "R ALT", "FN", "R CTRL"]

  return (
    <div className="App">
      <h1>Virtual Keyboard</h1>
      <input type="text" value={inputText} readOnly />
      <div className="keyboard">
        {row1.map((letter) => (
          <button key={letter}>
            {letter}
          </button>
        ))}
      </div>
        <div className="keyboard">
            {row2.map((letter) => (
                <button key={letter}>
                    {letter}
                </button>
            ))}
        </div>
        <div className="keyboard">
            {row3.map((letter) => (
                <button key={letter}>
                    {letter}
                </button>
            ))}
        </div>
        <div className="keyboard">
            {row4.map((letter) => (
                <button key={letter}>
                    {letter}
                </button>
            ))}
        </div>
        <div className="keyboard">
            {row5.map((letter) => (
                <button key={letter}>
                    {letter}
                </button>
            ))}
        </div>
        <div className="keyboard">
            {row6.map((letter) => (
                <button key={letter}>
                    {letter}
                </button>
            ))}
        </div>
    </div>
  );
}

export default App;
