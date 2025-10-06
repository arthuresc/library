# 📚 Plano de Estudos: C++ com ESP32 para Hacking RF/WiFi/BLE

## 🗓️ **Cronograma Detalhado (16 Semanas)**

### **FASE 1: Fundamentos do ESP32 e C++ (Semanas 1-4)**

**Semana 1: Ambiente e Sintaxe Básica**
- **Dia 1-2:** Setup PlatformIO + ESP-IDF com C++
- **Dia 3-4:** Estrutura de projetos ESP-IDF e `app_main()`
- **Dia 5:** GPIO básico - Piscar LED com classe
```cpp
class RFModule {
protected:
    gpio_num_t power_pin;
public:
    RFModule(gpio_num_t pin) : power_pin(pin) {}
    virtual void enable() { gpio_set_level(power_pin, 1); }
};
```

**Semana 2: Comunicação SPI para nRF905**
- **Dia 1-2:** Protocolo SPI no ESP32
- **Dia 3-4:** Driver básico para nRF905
- **Dia 5:** Configuração de registros do nRF905

**Semana 3: Classes e Encapsulamento**
- **Dia 1-2:** Membros private/public e métodos
- **Dia 3-4:** Getters/Setters para configuração RF
- **Dia 5:** Projeto: Configurador de frequência

**Semana 4: Herança e Polimorfismo**
- **Dia 1-2:** Classe base para módulos RF
- **Dia 3-4:** Classes derivadas específicas
- **Dia 5:** Sistema de módulos intercambiáveis

### **FASE 2: Sistema de Menu e nRF905 (Semanas 5-8)**

**Semana 5: Framework de Menu**
- **Dia 1-2:** Biblioteca TFT_eSPI para display
- **Dia 3-4:** Sistema de navegação com encoder
- **Dia 5:** Estrutura hierárquica de menus

**Semana 6: Driver nRF905 Completo**
- **Dia 1-2:** Modos TX/RX e controle de energia
- **Dia 3-4:** Protocolo de comunicação do módulo
- **Dia 5:** Auto-detecção de frequência

**Semana 7: Sistema de Captura RF**
- **Dia 1-2:** Sniffer de pacotes na frequência alvo
- **Dia 3-4:** Análise de protocolos comuns (portões)
- **Dia 5:** Armazenamento de sinais capturados

**Semana 8: Replay Attack Básico**
- **Dia 1-2:** Implementação do modo replay
- **Dia 3-4:** Gestão de códigos capturados
- **Dia 5:** Interface menu para replay

### **FASE 3: Hacks Avançados (Semanas 9-12)**

**Semana 9: WiFi Hacking**
- **Dia 1-2:** Scanner de redes WiFi
- **Dia 3-4:** Portal cativo fake
- **Dia 5:** Deauth attack (modo monitor)

**Semana 10: Bluetooth Low Energy**
- **Dia 1-2:** Scanner BLE e dispositivos
- **Dia 3-4:** Spoofing de dispositivos BLE
- **Dia 5:** Ataques a beacons (iBeacon/Eddystone)

**Semana 11: RFID/NFC**
- **Dia 1-2:** Módulo RC522 - leitura tags
- **Dia 3-4:** Clonagem básica de RFID
- **Dia 5:** Análise de protocolos MIFARE

**Semana 12: Integração Multi-módulo**
- **Dia 1-2:** Sistema de módulos plugáveis
- **Dia 3-4:** Gestão de recursos compartilhados
- **Dia 5:** Menu unificado para todos os hacks

### **FASE 4: Projeto Final (Semanas 13-16)**

**Semana 13: Otimização e Performance**
- **Dia 1-2:** Gestão de memória no ESP32
- **Dia 3-4:** Power management para bateria
- **Dia 5:** Otimização do código C++

**Semana 14: Interface Avançada**
- **Dia 1-2:** Gráficos e visualização de sinais
- **Dia 3-4:** Sistema de configurações persistente
- **Dia 5:** Logging e debug integrado

**Semana 15: Testes e Refinamento**
- **Dia 1-2:** Testes com hardware real
- **Dia 3-4:** Correção de bugs e melhorias
- **Dia 5:** Documentação do projeto

**Semana 16: Features Avançadas**
- **Dia 1-2:** Scripting para automação
- **Dia 3-4:** Comunicação com PC/interface web
- **Dia 5:** Preparação para próximos módulos

## 🎯 **Projetos Práticos por Semana**

### **Semana 4: Classe Base RF**
```cpp
class GenericRFModule {
protected:
    uint32_t frequency;
    uint8_t output_power;
    spi_device_handle_t spi;
    
public:
    GenericRFModule(spi_host_device_t host, int miso, int mosi, int sclk, int cs);
    virtual bool setFrequency(uint32_t freq) = 0;
    virtual bool transmit(const uint8_t* data, size_t len) = 0;
    virtual int receive(uint8_t* buffer, size_t max_len) = 0;
};
```

### **Semana 6: Driver nRF905 Específico**
```cpp
class NRF905Module : public GenericRFModule {
private:
    gpio_num_t trx_en, pwr, cd, am;
    
public:
    NRF905Module(spi_host_device_t host, int miso, int mosi, int sclk, int cs,
                 gpio_num_t trx_en, gpio_num_t pwr, gpio_num_t cd, gpio_num_t am);
    
    bool setFrequency(uint32_t freq) override;
    bool transmit(const uint8_t* data, size_t len) override;
    int receive(uint8_t* buffer, size_t max_len) override;
    
    // Métodos específicos do nRF905
    bool enterStandby();
    bool enterPowerDown();
    bool setChannel(uint8_t channel);
};
```

### **Semana 8: Sistema de Captura com Menu**
```cpp
class SignalCapture {
private:
    std::array<RFSignal, 100> captured_signals;
    size_t signal_count = 0;
    
public:
    void startCapture(uint32_t freq, uint32_t duration_ms);
    void saveSignal(const std::string& name);
    void replaySignal(size_t index);
    void analyzeSignal(size_t index);
};

class CaptureMenu : public MenuItem {
    SignalCapture& capture;
public:
    void draw(Display& display) override;
    void onEncoderTurn(int delta) override;
    void onButtonPress() override;
};
```

## 🔧 **Hardware Necessário**

### **Essencial:**
- ESP32 Dev Board
- Módulo nRF905 (433/868MHz)
- Display OLED 128x64 (I2C)
- Encoder rotativo + botões
- Antenas para 433MHz e 2.4GHz

### **Recomendado para expansão:**
- Módulo WiFi externo (ESP32 já tem)
- Módulo Bluetooth (ESP32 já tem)
- Leitor RFID RC522
- Módulo CC1101 (para mais frequências)
- Cartão SD para armazenamento

## 📖 **Recursos de Estudo por Fase**

### **Fase 1-2:**
- **C++:** "C++ Primer" (capítulos 1-10)
- **ESP32:** Documentação oficial ESP-IDF
- **nRF905:** Datasheet e aplicação notes

### **Fase 3-4:**
- **RF:** "Hacking Wireless Exposed"
- **WiFi:** Documentação ESP32 WiFi API
- **BLE:** ESP32 Bluetooth Guide

## ⚠️ **Considerações de Segurança e Legalidade**

### **Apenas para Educação:**
```cpp
// Todas as ferramentas devem incluir avisos
class SecurityTool {
protected:
    void showLegalWarning() {
        printf("AVISO: Use apenas em dispositivos próprios\n");
        printf("e com permissão explícita.\n");
    }
public:
    virtual void enable() {
        showLegalWarning();
        // ... resto da implementação
    }
};
```

### **Boas Práticas:**
- Testar apenas em equipamentos próprios
- Usar em ambiente controlado
- Documentar apenas para fins educacionais

## 🔄 **Plano de Estudos Diário Típico**

**Segunda:** Teoria + Exemplos (45min)
**Terça:** Implementação básica (1h)
**Quarta:** Debug e melhorias (1h)
**Quinta:** Integração com projeto (1h)
**Sexta:** Testes e documentação (45min)

## 🎯 **Checkpoints de Progresso**

### **Ao final do mês 1:**
- [ ] Ambiente configurado e funcionando
- [ ] Classe básica para nRF905 operacional
- [ ] Menu simples navegável

### **Ao final do mês 2:**
- [ ] Captura e replay de sinais RF básicos
- [ ] Sistema de menu completo
- [ ] Interface com display funcional

### **Ao final do mês 3:**
- [ ] Múltiplos módulos de hacking integrados
- [ ] Sistema de configuração persistente
- [ ] Documentação básica completa

### **Ao final do mês 4:**
- [ ] Projeto totalmente funcional
- [ ] Otimizado para performance
- [ ] Preparado para expansões futuras

## 💡 **Dicas para Sucesso:**

1. **Comece simples** - nRF905 básico antes de features complexas
2. **Teste incrementalmente** - cada função separadamente
3. **Documente o aprendizado** - anote descobertas sobre protocolos
4. **Participe da comunidade** - forums de RF e ESP32


Vamos estruturar o plano de estudos em formato de módulos, cada um com:

    Objetivos de aprendizagem

    Textos de referência (documentações, artigos, livros)

    Exemplos de código

    Exercícios práticos

Vamos dividir em 16 semanas, com 5 dias de estudo por semana.
Módulo 1: Ambiente de Desenvolvimento e Fundamentos de C++ para Embarcados
Semana 1: Configuração do Ambiente e Primeiro Programa
Dia 1: Instalação e Configuração do PlatformIO

Objetivo: Configurar o ambiente de desenvolvimento no VSCode com PlatformIO para ESP32 usando o framework ESP-IDF e C++.

Texto de Referência:

    PlatformIO Documentation: ESP32 with ESP-IDF

    ESP-IDF Programming Guide: Getting Started

Exemplo:
Crie um novo projeto no PlatformIO:

    Selecione a board “ESP32 Dev Module”

    Framework: ESP-IDF

    Crie um arquivo main.cpp na pasta src

Exercício:

    Siga o guia de instalação do PlatformIO e crie um projeto "Hello World" que imprima uma mensagem via serial.

    Conecte o ESP32, faça o upload e abra o monitor serial para ver a mensagem.

Dia 2: Estrutura de um Projeto ESP-IDF e Função app_main

Objetivo: Entender a estrutura de projetos ESP-IDF e a função app_main como ponto de entrada.

Texto de Referência:

    ESP-IDF Application Startup Flow

Exemplo:
cpp

#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

extern "C" void app_main(void)
{
    printf("Hello from app_main!\n");
    while (1) {
        printf("Looping...\n");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

Exercício:

    Modifique o exemplo para imprimir uma contagem a cada segundo.

    Adicione uma tarefa FreeRTOS que imprime "Task running" a cada 2 segundos.

Dia 3: GPIO Básico com C++ - Piscar LED

Objetivo: Controlar um LED usando GPIO com C++.

Texto de Referência:

    ESP-IDF GPIO API

Exemplo:
cpp

#include <driver/gpio.h>

#define LED_GPIO GPIO_NUM_2

extern "C" void app_main(void)
{
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);
    while (1) {
        gpio_set_level(LED_GPIO, 1);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        gpio_set_level(LED_GPIO, 0);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

Exercício:

    Conecte um LED ao pino 2 do ESP32 e faça piscar.

    Altere o código para que o LED pisque a cada 500ms.

Dia 4: Introdução a Classes em C++ - Controle de LED

Objetivo: Criar uma classe para encapsular o controle do LED.

Texto de Referência:

    C++ Classes

Exemplo:
cpp

class Led {
private:
    gpio_num_t pin;
public:
    Led(gpio_num_t p) : pin(p) {
        gpio_set_direction(pin, GPIO_MODE_OUTPUT);
    }
    void on() { gpio_set_level(pin, 1); }
    void off() { gpio_set_level(pin, 0); }
    void toggle() {
        int level = gpio_get_level(pin);
        gpio_set_level(pin, !level);
    }
};

extern "C" void app_main(void)
{
    Led led(GPIO_NUM_2);
    while (1) {
        led.toggle();
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

Exercício:

    Crie uma classe BlinkingLed que herda de Led e adiciona um método blink(int delay_ms).

    Use a classe para piscar dois LEDs com intervalos diferentes.

Dia 5: SPI Básico - Compreendendo o Protocolo

Objetivo: Entender o protocolo SPI e como configurá-lo no ESP32.

Texto de Referência:

    ESP-IDF SPI Master Driver

Exemplo:
Configuração básica do SPI:
cpp

#include <driver/spi_master.h>

void init_spi() {
    spi_bus_config_t bus_cfg = {
        .mosi_io_num = 23,
        .miso_io_num = 19,
        .sclk_io_num = 18,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
        .max_transfer_sz = 4096
    };
    spi_bus_initialize(SPI2_HOST, &bus_cfg, SPI_DMA_CH_AUTO);
}

Exercício:

    Configure o SPI no ESP32 com os pinos MOSI (23), MISO (19), SCLK (18).

    Teste a comunicação com um dispositivo SPI simples (ex: leitor de cartão SD) para verificar a configuração.

Semana 2: Driver nRF905 e Comunicação SPI
Dia 1: Datasheet nRF905 - Registros e Configuração

Objetivo: Estudar o datasheet do nRF905 para entender seus registros e como configurá-lo.

Texto de Referência:

    nRF905 Product Specification (buscar o datasheet)

Exemplo:
Estrutura de registros do nRF905 (exemplo de configuração):
cpp

typedef struct {
    uint8_t config[10]; // Registros de configuração
} nrf905_config_t;

void nrf905_init_config(nrf905_config_t* cfg) {
    // Configuração base para 433MHz, 1Mbps, etc.
}

Exercício:

    Liste os registros de configuração do nRF905 e suas funções.

    Escreva uma função em C++ que define a frequência de operação.

Dia 2: Classe para Controle nRF905 - Parte 1

Objetivo: Criar uma classe para o nRF905 que inicialize o módulo.

Texto de Referência:

    nRF905 Application Note

Exemplo:
cpp

class NRF905 {
private:
    spi_device_handle_t spi;
    gpio_num_t cs_pin;
    gpio_num_t trx_en;
    gpio_num_t pwr;
    // ... outros pinos

public:
    NRF905(spi_host_device_t host, int miso, int mosi, int sclk, int cs,
           gpio_num_t trx_en, gpio_num_t pwr, gpio_num_t cd, gpio_num_t am);
    bool init();
    bool setFrequency(uint32_t freq);
};

Exercício:

    Implemente o construtor da classe NRF905 que inicializa os pinos e SPI.

    Implemente o método init() que configura os pinos e SPI.

Dia 3: Classe para Controle nRF905 - Parte 2

Objetivo: Implementar métodos de leitura e escrita de registros.

Texto de Referência:

    SPI Master Driver - Transações

Exemplo:
cpp

class NRF905 {
    // ...
    uint8_t readRegister(uint8_t reg) {
        uint8_t cmd = 0x00 | (reg & 0x0F); // Comando de leitura
        uint8_t data;
        spi_transaction_t t = {
            .tx_buffer = &cmd,
            .rx_buffer = &data,
            .length = 8
        };
        spi_device_transmit(spi, &t);
        return data;
    }

    void writeRegister(uint8_t reg, uint8_t value) {
        uint8_t cmd = 0x20 | (reg & 0x0F); // Comando de escrita
        spi_transaction_t t = {
            .tx_buffer = &cmd,
            .length = 8
        };
        spi_device_transmit(spi, &t);
        t.tx_buffer = &value;
        spi_device_transmit(spi, &t);
    }
};

Exercício:

    Implemente a leitura e escrita de registros.

    Teste lendo e escrevendo um registro (ex: registro de configuração 0) e verifique no logic analyzer ou osciloscópio.

Dia 4: Configuração de Frequência e Potência

Objetivo: Configurar a frequência e potência de transmissão do nRF905.

Texto de Referência:

    nRF905 Datasheet: Frequency Setting (seção de configuração de frequência)

Exemplo:
cpp

class NRF905 {
    // ...
    bool setFrequency(uint32_t freq) {
        // Cálculo do valor do registro de frequência
        uint32_t f = (freq - 422400000) / 100000;
        if (f > 0x7F) return false;
        writeRegister(0x00, (uint8_t)f);
        return true;
    }

    void setTxPower(uint8_t power) {
        // power: 0 (min) a 3 (max)
        uint8_t reg = readRegister(0x01);
        reg = (reg & 0xFC) | (power & 0x03);
        writeRegister(0x01, reg);
    }
};

Exercício:

    Configure o nRF905 para 433MHz e potência máxima.

    Verifique a configuração lendo os registros e imprimindo via serial.

Dia 5: Modos de Operação (TX, RX, Standby)

Objetivo: Controlar os modos de operação do nRF905 (TX, RX, Standby).

Texto de Referência:

    nRF905 Datasheet: Operating Modes (seção de modos de operação)

Exemplo:
cpp

class NRF905 {
    // ...
    void setModeTX() {
        gpio_set_level(trx_en, 1);
        gpio_set_level(pwr, 1);
    }

    void setModeRX() {
        gpio_set_level(trx_en, 0);
        gpio_set_level(pwr, 1);
    }

    void setModeStandby() {
        gpio_set_level(trx_en, 0);
        gpio_set_level(pwr, 0);
    }
};

Exercício:

    Implemente os métodos para mudar entre modos.

    Crie um programa que fica 5 segundos em RX, depois 5 segundos em Standby, e repete.

Semana 3: Sistema de Menu Básico
Dia 1: Display OLED com I2C

Objetivo: Configurar um display OLED 128x64 via I2C.

Texto de Referência:

    ESP-IDF I2C Driver

    SSD1306 Datasheet

Exemplo:
cpp

#include "driver/i2c.h"
#include "ssd1306.h"

void init_oled() {
    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = 21,
        .scl_io_num = 22,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = 400000
    };
    i2c_param_config(I2C_NUM_0, &conf);
    i2c_driver_install(I2C_NUM_0, I2C_MODE_MASTER, 0, 0, 0);
    ssd1306_init(); // Inicializa o display
}

Exercício:

    Conecte o display OLED aos pinos I2C (SDA: 21, SCL: 22) e inicialize.

    Escreva uma função para mostrar um texto no display.

Dia 2: Biblioteca de Menu Simples

Objetivo: Criar uma biblioteca simples para menu no display.

Texto de Referência:

    TFT_eSPI Library (para ideias, mas usaremos SSD1306)

Exemplo:
cpp

class Menu {
private:
    std::vector<std::string> items;
    int selected = 0;
public:
    void addItem(const std::string& item) {
        items.push_back(item);
    }
    void draw(SSD1306& display) {
        display.clear();
        for (size_t i = 0; i < items.size(); i++) {
            if (i == selected) {
                display.drawString(0, i*10, "> " + items[i]);
            } else {
                display.drawString(0, i*10, "  " + items[i]);
            }
        }
        display.display();
    }
    void next() { selected = (selected + 1) % items.size(); }
    void prev() { selected = (selected - 1 + items.size()) % items.size(); }
    int getSelected() { return selected; }
};

Exercício:

    Implemente a classe Menu e teste com 3 itens.

    Navegue pelos itens com botões ou serial.

Dia 3: Navegação com Encoder Rotativo

Objetivo: Usar um encoder rotativo para navegar no menu.

Texto de Referência:

    ESP-IDF PCNT (Pulse Counter) ou usar interrupções GPIO

Exemplo:
cpp

class Encoder {
private:
    gpio_num_t clk, dt;
    int count = 0;
    static void isr_handler(void* arg) {
        Encoder* self = (Encoder*)arg;
        // Lógica do encoder
    }
public:
    Encoder(gpio_num_t clk_pin, gpio_num_t dt_pin) : clk(clk_pin), dt(dt_pin) {
        gpio_set_direction(clk, GPIO_MODE_INPUT);
        gpio_set_direction(dt, GPIO_MODE_INPUT);
        gpio_set_intr_type(clk, GPIO_INTR_ANYEDGE);
        gpio_install_isr_service(0);
        gpio_isr_handler_add(clk, isr_handler, this);
    }
    int getCount() { return count; }
};

Exercício:

    Conecte um encoder rotativo e implemente a leitura.

    Use o encoder para navegar no menu.

Dia 4: Integração Menu e nRF905

Objetivo: Integrar o menu com as funções do nRF905.

Exemplo:
cpp

class NRF905Menu {
private:
    Menu menu;
    NRF905& radio;
public:
    NRF905Menu(NRF905& r) : radio(r) {
        menu.addItem("Set Frequency");
        menu.addItem("Set Power");
        menu.addItem("TX Mode");
        menu.addItem("RX Mode");
    }
    void draw(SSD1306& display) { menu.draw(display); }
    void handleSelection() {
        switch(menu.getSelected()) {
            case 0: // Set Frequency
                // Lógica para configurar frequência
                break;
            // ... outros casos
        }
    }
};

Exercício:

    Crie um menu com opções para configurar frequência, potência e modo do nRF905.

    Implemente a lógica para cada opção.

Dia 5: Sistema de Configuração Persistente

Objetivo: Salvar e carregar configurações na NVS (Non-Volatile Storage).

Texto de Referência:

    ESP-IDF NVS

Exemplo:
cpp

#include "nvs_flash.h"
#include "nvs.h"

class Settings {
public:
    bool saveFrequency(uint32_t freq) {
        nvs_handle_t handle;
        if (nvs_open("storage", NVS_READWRITE, &handle) == ESP_OK) {
            nvs_set_u32(handle, "freq", freq);
            nvs_commit(handle);
            nvs_close(handle);
            return true;
        }
        return false;
    }
    uint32_t loadFrequency() {
        nvs_handle_t handle;
        uint32_t freq = 433000000; // default
        if (nvs_open("storage", NVS_READONLY, &handle) == ESP_OK) {
            nvs_get_u32(handle, "freq", &freq);
            nvs_close(handle);
        }
        return freq;
    }
};

Exercício:

    Salve a frequência configurada na NVS.

    Ao iniciar, carregue a frequência salva.

Semana 4: Captura e Replay de Sinais RF
Dia 1: Modo Sniffer do nRF905

Objetivo: Implementar um modo sniffer para capturar pacotes.

Exemplo:
cpp

class NRF905 {
    // ...
    void startSniffing() {
        setModeRX();
        // Configurar para receber pacotes
    }
    bool packetAvailable() {
        // Verificar pino CD (Carrier Detect) ou AM (Address Match)
        return gpio_get_level(cd) == 1;
    }
    int receivePacket(uint8_t* buffer, size_t max_len) {
        // Ler pacote via SPI
    }
};

Exercício:

    Implemente a captura de pacotes quando o pino CD for ativado.

    Imprima os pacotes capturados via serial.

Dia 2: Análise de Protocolos Comuns

Objetivo: Analisar protocolos comuns de controles de portão.

Texto de Referência:

    Análise de protocolos RF 433MHz

Exemplo:
cpp

class ProtocolAnalyzer {
public:
    void analyze(const uint8_t* data, size_t len) {
        // Verificar se é um protocolo conhecido
        if (len == 4) {
            printf("Possível protocolo de 4 bytes\n");
        }
        // ... outros
    }
};

Exercício:

    Capture sinais de um controle de portão e analise o padrão (tamanho, repetições, etc.).

    Implemente detecção de protocolo por tamanho de pacote.

Dia 3: Armazenamento de Sinais Capturados

Objetivo: Armazenar sinais capturados na NVS ou em um buffer.

Exemplo:
cpp

class SignalDatabase {
private:
    std::vector<Signal> signals;
public:
    void addSignal(const Signal& sig) {
        signals.push_back(sig);
    }
    void saveToNVS() {
        // Salvar no NVS
    }
    void loadFromNVS() {
        // Carregar do NVS
    }
};

Exercício:

    Crie uma estrutura para armazenar sinais (dados, timestamp, etc.).

    Implemente a gravação e leitura de sinais na NVS.

Dia 4: Replay Attack Básico

Objetivo: Implementar o replay de sinais capturados.

Exemplo:
cpp

class NRF905 {
    // ...
    bool transmit(const uint8_t* data, size_t len) {
        setModeTX();
        // Escrever dados no registrador de TX
        // Iniciar transmissão
        // Esperar fim de TX (pino DR)
        setModeStandby();
        return true;
    }
};

class ReplayModule {
private:
    NRF905& radio;
    SignalDatabase& db;
public:
    void replay(size_t index) {
        Signal sig = db.getSignal(index);
        radio.transmit(sig.data, sig.length);
    }
};

Exercício:

    Implemente a transmissão de um sinal capturado.

    Teste com um controle de portão: capture e replique o sinal.

Dia 5: Menu para Captura e Replay

Objetivo: Integrar captura e replay no menu.

Exemplo:
cpp

class MainMenu {
    Menu menu;
    NRF905& radio;
    SignalDatabase& db;
    enum { CAPTURE, REPLAY, SETTINGS } state;
public:
    void draw(SSD1306& display) {
        // Desenhar menu de acordo com o estado
    }
    void handleEncoder(int delta) {
        // Navegar
    }
    void handleButton() {
        // Selecionar
        if (state == CAPTURE) {
            // Iniciar captura
        }
    }
};

Exercício:

    Adicione itens de menu para "Capturar Sinal" e "Repetir Sinal".

    Implemente a lógica para capturar e repetir sinais via menu.

Semanas 5-16: Continuaremos com os módulos de WiFi, BLE, RFID e integração.

Vamos parar por aqui na semana 4. Se você deseja, posso continuar com as próximas semanas (5 a 16) com o mesmo nível de detalhe.

Este plano é intenso e requer dedicação. Ajuste o ritmo conforme sua disponibilidade. Lembre-se de sempre testar com hardware real e documentar seus resultados.

Boa sorte!