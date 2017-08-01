#include <SPI.h>
#include <MFRC522.h>

// PORTAS DO LEITOR RFID

//Pins para o NodeMCU (ver Arquivo DiagramaNodeMCU.docx)
#define SS_PIN 10   // Porta SDA 
#define RST_PIN 9  // Porta RST

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
  
char st[20];

// LEDS. 

const int led1 = 2; 
const int led2 = 3;  
const int led3 = 4; 
const int led4 = 5;   
const int led5 = 6; 
const int led6 = 7; 


void AcendeLed(int l)
{
  digitalWrite(l, 1);
}

void ApagaLed(int l)
{
  digitalWrite(l, 0);
}
void PiscaLed(int l)
{
  
  digitalWrite(l, 0);
  delay(200);
  digitalWrite(l, 1);
  delay(200);
  digitalWrite(l, 0);
  delay(200);
  digitalWrite(l, 1);
  delay(200);
  digitalWrite(l, 0);
  delay(200);
  digitalWrite(l, 1);
  delay(200);
  digitalWrite(l, 0);
  delay(200);
  
}



// led1

void handleLed1Acende() {
  AcendeLed(led1);
  }

void handleLed1Apaga() {
  ApagaLed(led1);
    }

void handleLed1Pisca() {
  PiscaLed(led1);
  }

// led2

void handleLed2Acende() {
  AcendeLed(led2);
  }

void handleLed2Apaga() {
  ApagaLed(led2);
    }

void handleLed2Pisca() {
  PiscaLed(led2);
  }

// led3

void handleLed3Acende() {
  AcendeLed(led3);
  }

void handleLed3Apaga() {
  ApagaLed(led3);
    }

void handleLed3Pisca() {
  PiscaLed(led3);
  }

// led4

void handleLed4Acende() {
  AcendeLed(led4);
  }

void handleLed4Apaga() {
  ApagaLed(led4);
    }

void handleLed4Pisca() {
  PiscaLed(led4);
  }

// led5

void handleLed5Acende() {
  AcendeLed(led5);
  }

void handleLed5Apaga() {
  ApagaLed(led5);
    }

void handleLed5Pisca() {
  PiscaLed(led5);
  }

// led6

void handleLed6Acende() {
  AcendeLed(led6);
  }

void handleLed6Apaga() {
  ApagaLed(led6);
    }

void handleLed6Pisca() {
  PiscaLed(led6);
  }



void setup(void){
  
  
  
  // LEITOR RFID
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522
  
 
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  
  digitalWrite(led1, 0);
  digitalWrite(led2, 0);
  digitalWrite(led3, 0);
  digitalWrite(led4, 0);
  digitalWrite(led5, 0);
  digitalWrite(led6, 0);
 
  Serial.println("CoCoa Arduino server started!");
}

void loop(void){

  // Cuida das chamadas vindas pela porta seria
  handleSerial();

  
  // Cuida do RDID
  handleRFID();

  delay(10);
}

void handleSerial()
{
  String receivedChar;
  
  if (Serial.available() > 0) {
    receivedChar = Serial.readString();

   // Led1
   if (receivedChar=="A")
      handleLed1Acende();
   if (receivedChar=="B")
      handleLed1Apaga();
   if (receivedChar=="C")
      handleLed1Pisca();

   // Led2
   if (receivedChar=="D")
      handleLed2Acende();
   if (receivedChar=="E")
      handleLed2Apaga();
   if (receivedChar=="F")
      handleLed2Pisca();

   // Led3
   if (receivedChar=="G")
      handleLed3Acende();
   if (receivedChar=="H")
      handleLed3Apaga();
   if (receivedChar=="I")
      handleLed3Pisca();

   // Led4
   if (receivedChar=="J")
      handleLed4Acende();
   if (receivedChar=="K")
      handleLed4Apaga();
   if (receivedChar=="L")
      handleLed4Pisca();

  // Led5
   if (receivedChar=="M")
      handleLed5Acende();
   if (receivedChar=="N")
      handleLed5Apaga();
   if (receivedChar=="O")
      handleLed5Pisca();

   // Led6
   if (receivedChar=="P")
      handleLed6Acende();
   if (receivedChar=="Q")
      handleLed6Apaga();
   if (receivedChar=="R")
      handleLed6Pisca();
   
   // Serial.println("Recebido:" + receivedChar);

    
  }
}

void handleRFID()
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
        // Serial.println("Sem cartão : ");
        return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
        // Serial.println("Err?");
        return;
  }
  //Mostra UID na serial
  // Serial.print("UID da tag :");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     // Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     // Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println(conteudo);
  // Serial.println();

 
}


