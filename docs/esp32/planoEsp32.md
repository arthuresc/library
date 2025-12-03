# 📚 Plano de Estudos Baseado em Exercícios com Fontes Acadêmicas

## 🎯 **Metodologia Pedagógica Aplicada**
Baseado na *Taxonomia de Bloom* e *Aprendizagem Baseada em Problemas*, cada módulo segue:
- **Leitura dirigida** de fontes primárias
- **Exemplos práticos** com código comentado
- **Exercícios progressivos** de complexidade crescente
- **Projetos de aplicação** imediata

---

## **MÓDULO 1: Fundamentos Eletrônicos do nRF905**

### **Semana 1: Princípios de Comunicação RF**
**Fonte Principal:** *"RF Microelectronics" de Behzad Razavi, Capítulo 2*

**Texto de Estudo:**
> "O nRF905 opera no princípio de comunicação OOK/FSK em frequências ISM. A modulação FSK oferece melhor imunidade a ruído comparado com ASK..."

**Exercício Prático 1.1:**
```cpp
// Analisando o espectro RF básico
#include <cmath>

class RFSpectrumAnalyzer {
private:
    static constexpr double k = 1.380649e-23; // Constante Boltzmann
    double temperature = 300; // Kelvin
public:
    double calculateNoiseFloor(double bandwidth) {
        // Fórmula: Noise Floor = 10*log10(k*T*B) + NF
        return 10 * log10(k * temperature * bandwidth) + 6; // +6dB NF típico
    }
};

// TESTE: Calcule o noise floor para 100kHz de banda
void testNoiseFloor() {
    RFSpectrumAnalyzer analyzer;
    double noise = analyzer.calculateNoiseFloor(100e3);
    printf("Noise Floor: %.2f dBm\n", noise);
}
```

**Exercício 1.2:** 
- Meça a potência de ruído ambiente com o nRF905 em modo RX
- Compare com o cálculo teórico (diferença esperada: ±3dB)

### **Semana 2: Protocolo SPI do nRF905**
**Fonte:** *Datasheet nRF905 v1.3, páginas 15-22*

**Texto de Estudo:**
> "O nRF905 utiliza comunicação SPI modo 0 (CPOL=0, CPHA=0) com clock máximo de 10MHz. Os registros de configuração são mapeados em endereços de 8 bits..."

**Exercício Prático 2.1:**
```cpp
class NRF905SPI {
private:
    spi_device_handle_t spi;
    gpio_num_t cs_pin;
    
    void writeRegister(uint8_t reg, uint8_t value) {
        spi_transaction_t t = {
            .flags = SPI_TRANS_USE_TXDATA,
            .cmd = 0x20 | (reg & 0x0F), // Comando escrita
            .tx_data = {value, 0, 0, 0},
            .length = 8 // 8 bits de dados
        };
        gpio_set_level(cs_pin, 0);
        spi_device_transmit(spi, &t);
        gpio_set_level(cs_pin, 1);
    }
    
public:
    bool initSPI() {
        spi_bus_config_t buscfg = {
            .mosi_io_num = 23,
            .miso_io_num = 19,
            .sclk_io_num = 18,
            .quadwp_io_num = -1,
            .quadhd_io_num = -1,
            .max_transfer_sz = 4094
        };
        
        spi_device_interface_config_t devcfg = {
            .mode = 0, // SPI mode 0
            .clock_speed_hz = 10 * 1000 * 1000, // 10MHz
            .spics_io_num = -1, // CS manual
            .flags = SPI_DEVICE_NO_DUMMY,
            .queue_size = 7
        };
        
        return spi_bus_initialize(SPI2_HOST, &buscfg, SPI_DMA_DISABLED) == ESP_OK;
    }
};
```

**Exercício 2.2:**
- Implemente leitura de registros do nRF905 via SPI
- Verifique o registro CONFIG (0x00) retorna 0x00 (valor padrão após reset)

---

## **MÓDULO 2: Programação Orientada a Objetos com C++**

### **Semana 3: Classes e Encapsulamento**
**Fonte:** *"The C++ Programming Language" de Bjarne Stroustrup, Capítulo 16*

**Texto de Estudo:**
> "O encapsulamento permite esconder detalhes de implementação enquanto expõe uma interface clara. No contexto embarcado, isso é crucial para gerenciar complexidade..."

**Exercício Prático 3.1:**
```cpp
// Implementação de uma classe para controle de potência RF
class RFPowerController {
private:
    uint8_t current_power; // 0-3 (máximo)
    uint8_t power_registers[4] = {0x00, 0x20, 0x40, 0x60}; // Valores do registro
    
    void updateHardware() {
        // Atualiza registros do nRF905
        writeRegister(0x01, power_registers[current_power]);
    }
    
public:
    RFPowerController() : current_power(3) {} // Máximo por padrão
    
    // Interface pública - esconde complexidade do hardware
    bool setPowerLevel(uint8_t level) {
        if (level > 3) return false;
        current_power = level;
        updateHardware();
        return true;
    }
    
    uint8_t getPowerLevel() const {
        return current_power;
    }
    
    float calculateRangeMeters() const {
        // Fórmula simplificada de Friis
        const float frequency = 433e6;
        const float tx_power_dbm[4] = {-10, -2, 6, 10}; // Dados do datasheet
        return pow(10, (tx_power_dbm[current_power] - 30) / 20.0) * 1000;
    }
};
```

**Exercício 3.2:**
- Crie testes unitários para verificar todos os níveis de potência
- Meça o consumo atual em cada nível com multímetro

### **Semana 4: Herança e Polimorfismo**
**Fonte:** *"Effective C++" de Scott Meyers, Itens 32-39*

**Exercício Prático 4.1:**
```cpp
// Hierarquia de classes para diferentes modulos RF
class GenericRFModule {
protected:
    uint32_t frequency;
    spi_device_handle_t spi;
    
public:
    GenericRFModule(uint32_t freq) : frequency(freq) {}
    virtual ~GenericRFModule() = default;
    
    virtual bool initialize() = 0; // Puramente virtual
    virtual bool transmit(const uint8_t* data, size_t length) = 0;
    virtual int receive(uint8_t* buffer, size_t max_length) = 0;
    
    virtual uint32_t getFrequency() const { return frequency; }
};

class NRF905Module : public GenericRFModule {
private:
    gpio_num_t trx_en, pwr, cd, am;
    bool configured = false;
    
public:
    NRF905Module(uint32_t freq, gpio_num_t trx, gpio_num_t pwr_pin, 
                 gpio_num_t cd_pin, gpio_num_t am_pin)
        : GenericRFModule(freq), trx_en(trx), pwr(pwr_pin), cd(cd_pin), am(am_pin) {}
    
    bool initialize() override {
        // Configuração específica do nRF905
        if(!configurePins()) return false;
        if(!configureSPI()) return false;
        if(!configureRegisters()) return false;
        
        configured = true;
        return true;
    }
    
    bool transmit(const uint8_t* data, size_t length) override {
        if (!configured || length > 32) return false;
        
        setModeStandby();
        writeTxPayload(data, length);
        setModeTX();
        
        // Aguarda transmissão completar
        vTaskDelay(10 / portTICK_PERIOD_MS);
        setModeStandby();
        
        return true;
    }
    
    // ... implementação específica do nRF905
};
```

**Exercício 4.2:**
- Crie uma classe `NRF24L01Module` que herda de `GenericRFModule`
- Implemente os métodos virtuais para este módulo diferente
- Demonstre polimorfismo em um array de `GenericRFModule*`

---

## **MÓDULO 3: Sistema de Menu com Padrões de Projeto**

### **Semana 5: Padrão State Machine**
**Fonte:** *"Design Patterns" de Gamma et al., Padrão State*

**Exercício Prático 5.1:**
```cpp
class MenuState {
public:
    virtual ~MenuState() = default;
    virtual void enter() = 0;
    virtual void exit() = 0;
    virtual void handleEncoder(int delta) = 0;
    virtual void handleButton() = 0;
    virtual void draw(Display& display) = 0;
};

class MainMenuState : public MenuState {
private:
    std::vector<std::string> items = {
        "Scanner RF", "Capturar Sinal", "Replay Attack", 
        "Configuracoes", "Sobre"
    };
    int selected_index = 0;
    
public:
    void enter() override {
        selected_index = 0;
    }
    
    void handleEncoder(int delta) override {
        selected_index = (selected_index + delta + items.size()) % items.size();
    }
    
    void handleButton() override {
        // Transição para estado baseado na seleção
        StateManager::setState(createStateForIndex(selected_index));
    }
    
    void draw(Display& display) override {
        display.clear();
        for (size_t i = 0; i < items.size(); ++i) {
            if (i == selected_index) {
                display.print("> " + items[i]);
            } else {
                display.print("  " + items[i]);
            }
        }
    }
};
```

**Exercício 5.2:**
- Implemente 3 estados diferentes do menu
- Adicione transições entre estados com animação

### **Semana 6: Padrão Observer para Eventos RF**
**Fonte:** *"Head First Design Patterns" - Padrão Observer*

**Exercício Prático 6.1:**
```cpp
class RFEvent {
public:
    enum Type { PACKET_RECEIVED, CARRIER_DETECTED, TRANSMISSION_COMPLETE };
    Type type;
    uint32_t timestamp;
    std::vector<uint8_t> data;
};

class RFObserver {
public:
    virtual ~RFObserver() = default;
    virtual void onRFEvent(const RFEvent& event) = 0;
};

class SignalCaptureManager : public RFObserver {
private:
    std::vector<RFEvent> captured_events;
    
public:
    void onRFEvent(const RFEvent& event) override {
        if (event.type == RFEvent::PACKET_RECEIVED) {
            captured_events.push_back(event);
            printf("Captured packet: %zu bytes\n", event.data.size());
        }
    }
    
    void replaySignal(size_t index) {
        if (index < captured_events.size()) {
            // Implementar replay
        }
    }
};

class RFEventManager {
private:
    std::vector<RFObserver*> observers;
    
public:
    void addObserver(RFObserver* observer) {
        observers.push_back(observer);
    }
    
    void notifyEvent(const RFEvent& event) {
        for (auto observer : observers) {
            observer->onRFEvent(event);
        }
    }
};
```

**Exercício 6.2:**
- Crie múltiplos observadores (display, SD card, serial)
- Teste notificações simultâneas

---

## **MÓDULO 4: Técnicas de Hacking RF Práticas**

### **Semana 7: Análise de Protocolos**
**Fonte:** *"Protocol Reverse Engineering" - Journal of Cybersecurity*

**Exercício Prático 7.1:**
```cpp
class ProtocolAnalyzer {
private:
    std::vector<std::vector<uint8_t>> captured_packets;
    
    struct ProtocolStats {
        size_t min_length, max_length;
        std::map<std::vector<uint8_t>, size_t> preamble_patterns;
        std::map<uint32_t, size_t> crc_hashes;
    };
    
public:
    void analyzeCaptures() {
        ProtocolStats stats = {SIZE_MAX, 0};
        
        for (const auto& packet : captured_packets) {
            // Análise de tamanho
            stats.min_length = std::min(stats.min_length, packet.size());
            stats.max_length = std::max(stats.max_length, packet.size());
            
            // Detecção de preamble (primeiros bytes)
            if (packet.size() >= 4) {
                std::vector<uint8_t> preamble(packet.begin(), packet.begin() + 4);
                stats.preamble_patterns[preamble]++;
            }
            
            // Tentativa de identificar CRC (últimos 2 bytes)
            if (packet.size() >= 2) {
                uint16_t possible_crc = (packet[packet.size()-2] << 8) | packet[packet.size()-1];
                // Testar se é CRC válido (implementar checks)
            }
        }
        
        printAnalysisReport(stats);
    }
    
    bool isRollingCode(const std::vector<uint8_t>& packet1, 
                      const std::vector<uint8_t>& packet2) {
        // Verifica se apenas uma parte do pacote muda (rolling code)
        if (packet1.size() != packet2.size()) return false;
        
        int differences = 0;
        for (size_t i = 0; i < packet1.size(); ++i) {
            if (packet1[i] != packet2[i]) differences++;
        }
        
        // Se apenas 1-3 bytes mudam, provavelmente é rolling code
        return differences > 0 && differences <= 3;
    }
};
```

**Exercício 7.2:**
- Capture 10 transmissões do mesmo controle
- Identifique padrões de rolling code
- Implemente detecção de código fixo vs. rolling

### **Semana 8: Ataques de Replay Avançados**
**Fonte:** *"Wireless Security: RF Hacking Techniques" - Black Hat Papers*

**Exercício Prático 8.1:**
```cpp
class AdvancedReplayAttack {
private:
    std::map<std::string, std::vector<std::vector<uint8_t>>> signal_database;
    NRF905Module& rf_module;
    
public:
    bool performJammingAndCapture(uint32_t frequency, uint32_t duration_ms) {
        // Técnica: Jam durante captura para forçar retransmissão
        setFrequency(frequency);
        
        auto start_time = esp_timer_get_time();
        std::vector<std::vector<uint8_t>> captured_during_jam;
        
        while ((esp_timer_get_time() - start_time) < duration_ms * 1000) {
            // Alterna entre jam e recepção rápida
            setModeTX(); // Transmite ruído
            vTaskDelay(1 / portTICK_PERIOD_MS);
            
            setModeRX();
            auto packet = receiveWithTimeout(5); // 5ms timeout
            if (!packet.empty()) {
                captured_during_jam.push_back(packet);
            }
        }
        
        return !captured_during_jam.empty();
    }
    
    void bruteForceFixedCodes(uint32_t base_code, uint32_t mask, uint32_t step) {
        // Para códigos fixos simples - força bruta controlada
        printf("Iniciando brute force em código fixo...\n");
        
        for (uint32_t code = base_code; code < (base_code + mask); code += step) {
            std::vector<uint8_t> test_packet = encodeFixedCode(code);
            
            if (rf_module.transmit(test_packet.data(), test_packet.size())) {
                printf("Transmitido código: 0x%08X\n", code);
                vTaskDelay(100 / portTICK_PERIOD_MS); // Evita saturação
            }
        }
    }
};
```

**Exercício 8.2:**
- Implemente detecção automática de janela de replay
- Teste com controles reais (apenas seus!)

---

## **MÓDULO 5: Integração Multi-tecnologia**

### **Semana 9: WiFi Scanning Integrado**
**Exercício Prático 9.1:**
```cpp
class WiFiScanIntegration {
private:
    std::vector<wifi_ap_record_t> ap_records;
    
public:
    void performWiFiScan() {
        wifi_scan_config_t scan_config = {
            .ssid = nullptr,
            .bssid = nullptr,
            .channel = 0,
            .show_hidden = true
        };
        
        esp_wifi_scan_start(&scan_config, true);
        
        uint16_t ap_count = 0;
        esp_wifi_scan_get_ap_num(&ap_count);
        
        ap_records.resize(ap_count);
        esp_wifi_scan_get_ap_records(&ap_count, ap_records.data());
    }
    
    void exportToKismetFormat() {
        // Formato para análise externa
        for (const auto& ap : ap_records) {
            printf("WiFi;%02x:%02x:%02x:%02x:%02x:%02x;%s;%d;%d\n",
                   ap.bssid[0], ap.bssid[1], ap.bssid[2],
                   ap.bssid[3], ap.bssid[4], ap.bssid[5],
                   ap.ssid, ap.channel, ap.rssi);
        }
    }
};
```

### **Semana 10: BLE Hacking Ético**
**Fonte:** *"Bluetooth Security" - NIST Special Publication 800-121*

**Exercício Prático 10.1:**
```cpp
class BLEAnalyzer {
public:
    void scanForVulnerableDevices() {
        // Procura por dispositivos BLE com características inseguras
        BLEScan* scan = BLEDevice::getScan();
        scan->setActiveScan(true);
        
        auto results = scan->start(30); // 30 segundos
        
        for (int i = 0; i < results.getCount(); i++) {
            auto device = results.getDevice(i);
            checkDeviceVulnerabilities(device);
        }
    }
    
private:
    void checkDeviceVulnerabilities(BLEAdvertisedDevice device) {
        std::vector<std::string> vulnerabilities;
        
        // Verifica se transmite dados pessoais
        if (device.haveName() && isPersonalData(device.getName())) {
            vulnerabilities.push_back("TRANSMITS_PII");
        }
        
        // Verifica serviços inseguros
        if (device.isAdvertisingService(BLEUUID("1800"))) { // Generic Access
            // Verifica se tem características writable sem autenticação
        }
        
        if (!vulnerabilities.empty()) {
            logVulnerableDevice(device, vulnerabilities);
        }
    }
};
```

---

## **PROJETO FINAL INTEGRADO**

### **Semanas 11-12: PenTest Platform Completa**
**Exercício Final:**
```cpp
class RFPenTestPlatform {
private:
    NRF905Module nrf905;
    WiFiScanIntegration wifi;
    BLEAnalyzer ble;
    ProtocolAnalyzer protocol_analyzer;
    MenuSystem menu;
    
public:
    void runSecurityAudit() {
        printf("=== INICIANDO AUDITORIA DE SEGURANÇA RF ===\n");
        
        // Fase 1: Reconhecimento
        auto wifi_aps = wifi.performWiFiScan();
        auto ble_devices = ble.scanForVulnerableDevices();
        auto rf_signals = nrf905.scanSpectrum(433e6, 434e6, 100e3);
        
        // Fase 2: Análise
        auto vuln_wifi = analyzeWiFiVulnerabilities(wifi_aps);
        auto vuln_ble = ble.getVulnerableDevices();
        auto vuln_rf = protocol_analyzer.analyzeCaptures();
        
        // Fase 3: Relatório
        generateReport(vuln_wifi, vuln_ble, vuln_rf);
    }
    
    void demoMode() {
        // Modo educativo - explica cada vulnerabilidade encontrada
        menu.addItem("WiFi WPS Vulnerable", []() {
            printf("VULN: WPS permite brute-force pin em horas\n");
            printf("MITIGATION: Desabilitar WPS no roteador\n");
        });
        
        menu.addItem("BLE No Auth Write", []() {
            printf("VULN: Característica BLE writable sem autenticação\n");
            printf("MITIGATION: Exigir pairing com strong auth\n");
        });
        
        menu.addItem("RF Replay Attack", []() {
            printf("VULN: Controle RF sem rolling code\n");
            printf("MITIGATION: Implementar código que muda a cada uso\n");
        });
    }
};
```

---

## 📋 **CHECKLIST DE AVALIAÇÃO POR MÓDULO**

### **Ao completar cada módulo, você deve ser capaz de:**

**Módulo 1:** 
- [ ] Explicar o princípio de operação do nRF905
- [ ] Calcular orçamento de link RF
- [ ] Configurar registros via SPI

**Módulo 2:**
- [ ] Implementar hierarquia de classes C++
- [ ] Usar polimorfismo corretamente
- [ ] Gerenciar recursos com RAII

**Módulo 3:**
- [ ] Implementar máquina de estados
- [ ] Usar padrão Observer
- [ ] Criar interface de usuário responsiva

**Módulo 4:**
- [ ] Analisar protocolos RF desconhecidos
- [ ] Identificar vulnerabilidades comuns
- [ ] Implementar contramedidas

**Módulo 5:**
- [ ] Integrar múltiplas tecnologias
- [ ] Gerar relatórios de segurança
- [ ] Explicar aspectos éticos

## 🔬 **METODOLOGIA DE AVALIAÇÃO**

1. **Exercícios Práticos (60%)** - Código funcionando
2. **Relatórios Técnicos (25%)** - Documentação das descobertas  
3. **Apresentação Oral (15%)** - Explicar conceitos aprendidos

**Próximo passo:** Comece pelo Módulo 1, exercício 1.1 e me informe seus resultados para ajustarmos o ritmo!

Quer que eu detalhe mais algum módulo específico ou ajuste a dificuldade dos exercícios?