let detectado = false;
let encontrado = false;

async function onIRMessage() {

    if (detectado) return;

    detectado = true;

    // Amarillo = señal encontrada
    setMainLed({
        r: 255,
        g: 255,
        b: 0
    });

    await speak("senal detectada", false);

    // Detener exploración
    stopRoll();

    // Comenzar seguimiento IR
    startIRFollow(0, 1);

    // Seguir durante 6 segundos
    await delay(6);

    encontrado = true;

    // Detener seguimiento 
    stopIRFollow();
    stopRoll();

    // Rojo = objetivo encontrado
    setMainLed({
        r: 255,
        g: 0,
        b: 0
    });

    await speak("objetivo encontrado", false);

    // Convertirse en beacon por broadcast canal 1
    startIRBroadcast(1, 1);
}

registerEvent(EventType.onIRMessage, onIRMessage);

async function startProgram() {

    // Escuchar mensajes del beacon inicial
    listenForIRMessage([0]);

    // Verde = explorando
    setMainLed({
        r: 0,
        g: 255,
        b: 0
    });

    // Buscar la señal mediante movimiento aleatorio
    while (!detectado) {

        let direccion = Math.floor(Math.random() * 360);

        await roll(direccion, 60, 1);

        await delay(0.2);
    }

    while (true) {
        await delay(1);
    }
}