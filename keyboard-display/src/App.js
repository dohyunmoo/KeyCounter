import React from 'react';
import './App.css';
// import { initializeApp } from 'firebase/App';
// import { getFirestore } from 'firebase/firestore';

let jsonData

fetch('../../.secret/credentials.json')
    .then(response => response.json())
    .then(data => {
        jsonData = data;
        console.log(jsonData);
    })
    .catch(error => {
        console.error('Error fetching the JSON file:', error);
});

const firebaseConfig = {
    apiKey: "AIzaSyDNFYGIFDVdiaFh4ubixHTUiIh2NSCThqw"
}

class Key{
    constructor(label, width=1) {
        this.label = label;
        this.width = width;
    }
    getWidth() {
        return this.width;
    }
    getLabel() {
        return this.label;
    }
}

function App() {

    const row1 = [new Key("ESC"), new Key("F1"), new Key("F2"), new Key("F3"), new Key("F4"), new Key("F5"), new Key("F6"), new Key("F7"), new Key("F8"), new Key("F9"), new Key("F10"), new Key("F11"), new Key("F12")]
    const row2 = [new Key("`"), new Key("1"), new Key("2"), new Key("3"), new Key("4"), new Key("5"), new Key("6"), new Key("7"), new Key("8"), new Key("9"), new Key("0"), new Key("-"), new Key("="), new Key("BACKSPACE", 2)]
    const row3 = [new Key("TAB", 1.3), new Key("Q"), new Key("W"), new Key("E"), new Key("R"), new Key("T"), new Key("Y"), new Key("U"), new Key("I"), new Key("O"), new Key("P"), new Key("["), new Key("]"), new Key("\\")]
    const row4 = [new Key("CAPS LOCK", 1.5), new Key("A"), new Key("S"), new Key("D"), new Key("F"), new Key("G"), new Key("H"), new Key("J"), new Key("K"), new Key("L"), new Key(";"), new Key("'"), new Key("ENTER", 2.3)]
    const row5 = [new Key("SHIFT", 2), new Key("Z"), new Key("X"), new Key("C"), new Key("V"), new Key("B"), new Key("N"), new Key("M"), new Key(","), new Key("."), new Key("/"), new Key("SHIFT", 2)]
    const row6 = [new Key("CTRL", 1.3), new Key("WIN"), new Key("ALT", 1.2), new Key("SPACE", 7), new Key("ALT", 1.2), new Key("FN"), new Key("CTRL", 1.3)]

    const specKeys = [[new Key("PRINT SCREEN"), new Key("SCROLL LOCK"), new Key("PAUSE")],
                     [new Key("INSERT"), new Key("HOME"), new Key("PAGE UP")],
                     [new Key("DELETE"), new Key("END"), new Key("PAGE DOWN")]]
    const arrowKeys = [[new Key("\u2191")], [new Key("\u2190"), new Key("\u2193"), new Key("\u2192")]] // up left down right

    const keyboardRows = [row1, row2, row3, row4, row5, row6]

    const unitLength = 40

    return (
        <div className="App">
            <h1>Virtual Keyboard</h1>

            <div id='keyboard'>

                <div id='mainKeyGroup'>
                    {keyboardRows.map((row, rowIndex) => (
                        <div key={`row-${rowIndex}`} className="Keys">
                            {row.map((letter) => (
                                <div key={letter.getLabel()} className="key-button" style={{ width: `${letter.getWidth() * unitLength}px` }}>
                                    {letter.getLabel()}
                                </div>
                            ))}
                        </div>
                    ))}
                </div>

                <div id='sideKeyGroup'>
                    <div id='specKeyGroup'>
                        {specKeys.map((row, rowIndex) => (
                            <div key={`row-${rowIndex}`} className="Keys">
                                {row.map((letter) => (
                                    <div key={letter.getLabel()} className="key-button" style={{ width: `${letter.getWidth() * unitLength}px` }}>
                                        {letter.getLabel()}
                                    </div>
                                ))}
                            </div>
                        ))}
                    </div>

                    <div id='filler'>
                        <div className='Keys'>
                            <div className='filler-key-button'></div>
                        </div>
                    </div>

                    <div id='arrowKeyGroup'>
                        {arrowKeys.map((row, rowIndex) => (
                            <div key={`row-arrow-${rowIndex}`} className="Keys">
                                {row.map((letter) => (
                                    <div key={letter.getLabel()} className="key-button" style={{ width: `${letter.getWidth() * unitLength}px` }}>
                                        {letter.getLabel()}
                                    </div>
                                ))}
                            </div>
                        ))}
                    </div>
                </div>

            <div id='mouse'>
                
            </div>

            </div>
        </div>
    );
}

export default App;
