let encontrado = false;

async function onCollision() {

    if (encontrado) return;

    encontrado = true;

    stopRoll();

    setMainLed({
        r: 255,
        g: 0,
        b: 0
    });

    await speak("Objetivo encontrado", false);

    // Comienza a actuar como baliza IR
    startIRBroadcast(0, 1);

    // Mantener la baliza activa
    while (true) {

        setMainLed({
            r: 255,
            g: 0,
            b: 0
        });

        await delay(0.5);

        setMainLed({
            r: 255,
            g: 255,
            b: 255
        });

        await delay(0.5);
    }
}

registerEvent(EventType.onCollision, onCollision);

async function startProgram() {

    setMainLed({
        r: 0,
        g: 255,
        b: 0
    });

    while (!encontrado) {

        let direccion = Math.floor(Math.random() * 360);

        await roll(direccion, 60, 1);

        await delay(0.2);
    }
}