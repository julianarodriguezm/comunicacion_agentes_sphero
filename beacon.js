async function sendWeakIRMessage() {

    setMainLed({
        r: 0,
        g: 255,
        b: 0
    });

    while (true) {
        sendIRMessage(0, 1);
        await delay(0.1);
    }
}

async function startProgram() {
    sendWeakIRMessage()
}