/* Programa para exibir dados recebidos de XBee.

   Possibilidades atuais:
      1 - Receber o endereco (SL )de um End Device cadastrado

   Possibilidades a serem implementadas:
   1 - Montar o pacote:
    1.1 - Pegar COMPRIMENTO
    1.2 - Pegar TIPO DE FRAME
    1.3 - Pegar o END. 64-bit
    1.4 - Pegar o END. 16-bit (MY)
    1.5 - Pegar o COMANDO (hex)
    1.6 - Calcular o CHECKSUM
   2 - Enviar o pacote
   3 - Verificar porta serial. Se disponivel, armazenar em um vetor o valor retornado
   4 - Enviar o vetor para o programa em Python.
*/
#include "SoftwareSerial.h"
SoftwareSerial xbee_serial(2, 3); //RX, TX

uint8_t option;
// const byte E1_64BIT_ADDRESS[] = {0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFF};
// const byte E2_64BIT_ADDRESS[] = {0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27};
// const byte E3_64BIT_ADDRESS[] = {0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE};

//00 13 A2 00 40 7C 48 FF - E1
//00 13 A2 00 40 7C 49 27 - E2
//00 13 A2 00 40 7C 48 FE - E3
//00 13 A2 00 40 4A 4B C6
//00 13 A2 00 40 7C 49 27 - R1
//00 13 A2 00 40 7C 48 FE - R2
int response[2] = {};

byte sl_frames[][19] = { // Array de frames SL
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFF, 0xFF, 0xFE, 0x02, 0x53, 0x4C, 0x91}, //E1
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27, 0xFF, 0xFE, 0x02, 0x53, 0x4C, 0x68}, // E2
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE, 0xFF, 0xFE, 0x02, 0x53, 0x4C, 0x92},  //E3
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x4A, 0x4B, 0xC6, 0xFF, 0xFE, 0x02, 0x73, 0x6C, 0xB9}, //
  {0X7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27, 0xFF, 0xFE, 0x02, 0x53, 0x4C, 0x68}, //R1
  {0X7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE, 0xFF, 0xFE, 0x02, 0x53, 0x4C, 0x92}
};
//Ex. respo SL: 7E 00 13 97 01 00 13 A2 00 40 7C 48 FF FE 59 53 4C 00 40 7C 48 FF B6

byte mp_frames[][19] = { // Array de frames MP
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFF, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0x93},
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0x6A},
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0x94},
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x4A, 0x4B, 0xC6, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0xFB},
  {0X7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0x6A}, //R1
  {0X7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE, 0xFF, 0xFE, 0x02, 0x4D, 0x50, 0x94}
};
//Ex. resp MP: 7E 00 11 97 01 00 13 A2 00 40 7C 48 FF FE 59 4D 50 00 00 00 BB


byte my_frames[][19] = {
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x49, 0x27, 0xFF, 0xFE, 0x02, 0x4D, 0x59, 0x61},//R1
  {0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7C, 0x48, 0xFE, 0xFF, 0xFE, 0x02, 0x4D, 0x59, 0x8B}
  //{0x7E, 0x00, 0x0F, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x4A, 0x4B, 0xC6, 0xFF, 0xFE, 0x02, 0x4D, 0x59, 0xF2};
};

void setup() {
  Serial.begin(9600);
  xbee_serial.begin(9600);
}

void send_frame(byte frame[19], char param) {
  xbee_serial.flush();
  Serial.println("\nEnviando frame...");
  for (int i = 0; i < 19; i++) {
    Serial.print((byte)frame[i], HEX);
    xbee_serial.write((byte)frame[i]);
  }
  Serial.println();
  if (param == 'L') {
    Serial.print("SL: ");
  } else if (param == 'P') {
    Serial.print("MP: ");
  } else if (param == 'Y') {
    Serial.print("MY: ");
  }
}


void loop() {

  if (Serial.available() == 1) {
    option = Serial.read();
    switch (option) {
      case '1': // envia frame para o ED 1 [SL]
        send_frame(sl_frames[0], 'L');
        break;
      case '2': // envia frame para o ED 2 [SL]
        send_frame(sl_frames[1], 'L');
        break;
      case '3': // envia frame para o ED 3 [SL]
        send_frame(sl_frames[2], 'L');
        break;
      case '4': // envia frame para o ED 1 [MP]
        send_frame(mp_frames[0], 'P');
        break;
      case '5': // envia frame para o ED 2 [MP]
        send_frame(mp_frames[1], 'P');
        break;
      case '6': // envia frame para o ED 3 [MP]
        send_frame(mp_frames[2], 'P');
        break;
      case '7': // envia frame para o R1 [SL]
        send_frame(sl_frames[4], 'L');
        break;
      case '8': // envia frame para o R1 [MP]
        send_frame(mp_frames[4], 'P');
        break;
      case '9':
        send_frame(my_frames[0], 'Y'); // envia frame para o R2 [MY]
        break;
      case 'A': // envia frame para o R1 [SL]
        send_frame(sl_frames[5], 'L');
        break;
      case 'B': // envia frame para o R1 [MP]
        send_frame(mp_frames[5], 'P');
        break;
      case 'C':
        send_frame(my_frames[1], 'Y'); // envia frame para o R2 [MY]
        break;
    }
  }
  if (xbee_serial.available() > 21) {
    if (xbee_serial.read() == 0x7E) { // se for o inicio do pacote
      for (int i = 0; i < 21; i++) {
        Serial.print(xbee_serial.read(), HEX);
        Serial.print('-');
      }
      //      for (int i = 0; i < 17; i++) { // loop sobre a resposta
      //        uint8_t waste = xbee_serial.read(); // lixo
      //      }
      //      Serial.print("\nMP: ");
      //      for (int i = 0; i < 2; i++) { // loop para armazenar o SL do pacote recebido
      //        response[i] = xbee_serial.read();
      //        Serial.print(response[i], HEX);
      //        Serial.print('-');
      //      }// Ler somente 2 bytes para MP
      //      Serial.println();
    }
  }
  Serial.flush();

}