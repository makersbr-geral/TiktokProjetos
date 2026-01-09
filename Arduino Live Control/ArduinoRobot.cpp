#include <Arduino.h> //OBS : Necessário para PlatformIO (Arduino Framework) No VSCode
#include <Servo.h>

Servo s1; Servo s2;
const int pinAzul = 12; 
const int pinVerde = 13;

void setup() {
  Serial.begin(115200);
  s1.attach(9); s2.attach(10);
  pinMode(pinAzul, OUTPUT); pinMode(pinVerde, OUTPUT);
  s1.write(90); s2.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int c1 = data.indexOf(',');
    int c2 = data.lastIndexOf(',');
    
    if (c1 != -1 && c2 != -1) {
      int pos1 = data.substring(0, c1).toInt();
      int pos2 = data.substring(c1 + 1, c2).toInt();
      int led = data.substring(c2 + 1).toInt();

      s1.write(pos1);
      s2.write(pos2);

      // Controle simples de LED: 0=Off, 1=Azul, 2=Verde, 3=Ambos
      digitalWrite(pinAzul, (led == 1 || led == 3) ? HIGH : LOW);
      digitalWrite(pinVerde, (led == 2 || led == 3) ? HIGH : LOW);
    }
  }
}