# 🤖 TikTok Live Mechatronics Bridge - WagnerMaker

Este projeto integra eventos em tempo real da plataforma **TikTok** com hardware físico através de um **Arduino**. 
O sistema monitora comentários e presentes (gifts) enviados durante uma Live e os traduz em movimentos coreografados para servos motores e sinalização via LEDs.

### Fiquem a vontade para alterar as funções, implementar novas, colocar mais atuadores, controladores, relés...

---
## 🚀 Como Configurar

### 1. Preparação do Arduino
Carregue o código disponível na pasta `/arduino` para sua placa. Certifique-se de que os servos estão conectados nos pinos 9 e 10. Leds, 12 e 13.

### 2. Configuração do Python
Clone este repositório e instale as dependências:
```bash
pip install tiktoklive pyserial
```
---
## 🛠️ Tecnologias e Hardware

* **Linguagem:** Python 3.10+
* **Hardware:** Arduino (Uno/Nano/Mega)
* **Comunicação:** Serial RS-232 (USB) | **Baud Rate:** 115200
* **Atuadores:** * 2x Servos Motores (Eixos X e Y)
    * 2x LEDs (Feedback Visual: Azul e Verde)

---

## 📐 Arquitetura do Sistema

O projeto é dividido em duas camadas principais:

1.  **Cérebro (Python):** Utiliza a biblioteca `TikTokLive` para escutar o socket da Live. Ao identificar um gatilho, ele processa a lógica de "dança" e envia uma string de comando para a porta serial.
2.  **Atuador (Arduino):** Recebe os dados no formato `pos1,pos2,led\n`, realiza o parsing e move os servos imediatamente para a posição desejada.

### Pinagem do Hardware
| Componente | Pino Arduino | Descrição |
| :--- | :--- | :--- |
| **Servo 1** | D9 | Movimento Horizontal |
| **Servo 2** | D10 | Movimento Vertical |
| **LED Azul** | D12 | Gatilho de Comentários |
| **LED Verde** | D13 | Gatilho de Presentes |

--- 
