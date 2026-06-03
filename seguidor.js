let detectoBeacon = false;

async function onIRMessage() {

    if (detectoBeacon) return;

    detectoBeacon = true;

    // Detener seguimiento y movimiento
    stopIRFollow();
    stopRoll();

    // Rojo = encontró beacon canal 0
    setMainLed({
        r: 255,
        g: 0,
        b: 0
    });

    await speak("beacon detectado", false);
}

registerEvent(EventType.onIRMessage, onIRMessage);

async function startProgram() {

    // Escuchar canal 0
    listenForIRMessage([0]);

    // Verde mientras sigue
    setMainLed({
        r: 0,
        g: 255,
        b: 0
    });

    await speak("siguiendo baliza", false);

    // Seguir canal 1
    startIRFollow(1, 1);

    while (true) {
        await delay(1);
    }
}