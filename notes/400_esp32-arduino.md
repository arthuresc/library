#Esp32 usando o framework do Arduino

## Leituras básicas

### pinMode(pino, modo) [WIP]

Serve para configurar aquele pino da placa como sendo de entrada, saída ou entrada_pullup (??? WIP)

### digitalWrite(pino, output)

Usado para dar valor ao pino (HIGH ou LOW)

### digitalRead(pino)

Usado para 

## Configurando:

### Linux:
#### PlatformIO + VSCode

- Depois de instalar a Extensão
- https://docs.platformio.org/en/latest/core/installation/udev-rules.html
- https://community.platformio.org/t/platformio-in-vs-code-running-on-linux-debian-access-to-dev-ttyusb0-port-doesnt-exist/35552

https://gist.github.com/walidamriou/cfd92d6ba35763920a278314839ae22b

usando o platformio, corrigir o monitor serial: 
monitor_rts = 0
monitor_dtr = 0