#include <SPI.h>
#include <MFRC522.h>

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>


// INFORMAÇÕES DA REDE
// const char* ssid = "batcaverna";
// const char* password = "joker2537";

const char* ssid = "F_PICHILIANI";
const char* password = "NOVAREDE";


ESP8266WebServer server(80);

// PORTAS DO LEITOR RFID

//Pins para o NodeMCU (ver Arquivo DiagramaNodeMCU.docx)
#define SS_PIN 4   // Porta SDA 
#define RST_PIN 5  // Porta RST

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
  
char st[20];

// LEDS. Somente 4 leds aqui por limitação de porta

const int led1 = 16; // Porta   D0
const int led2 = 0;  // Porta   D3
const int led3 = 02; // Porta   D4
const int led4 = 15;  // Porta   D8
// const int led5 = 9; // Porta   SD2
// const int led6 = 10; // Porta   SD3


void AcendeLed(int l)
{
  digitalWrite(l, 1);
  server.send(200, "text/plain", "Acendendo led:" + String(l));
}

void ApagaLed(int l)
{
  digitalWrite(l, 0);
  server.send(200, "text/plain", "Apagando led:" + String(l));
}
void PiscaLed(int l)
{
  server.send(200, "text/plain", "Piscando led:" + String(l));
  
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
/*
void handleLed5Acende() {
  AcendeLed(led5);
  }

void handleLed5Apaga() {
  ApagaLed(led5);
    }

void handleLed5Pisca() {
  PiscaLed(led5);
  }
*/
// led6
/*
void handleLed6Acende() {
  AcendeLed(led6);
  }

void handleLed6Apaga() {
  ApagaLed(led6);
    }

void handleLed6Pisca() {
  PiscaLed(led6);
  }
*/

void handleRoot() {
  server.send(200, "text/plain", "hello from esp8266!");
  }

void handleNotFound(){
  /*
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0); */
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
  // pinMode(led5, OUTPUT);
  // pinMode(led6, OUTPUT);
  
  digitalWrite(led1, 0);
  digitalWrite(led2, 0);
  digitalWrite(led3, 0);
  digitalWrite(led4, 0);
  // digitalWrite(led5, 0);
  // digitalWrite(led6, 0);
  
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  // Led1
  server.on("/A", handleLed1Acende);
  server.on("/B", handleLed1Apaga);
  server.on("/C", handleLed1Pisca);
  
  // Led2
  server.on("/D", handleLed2Acende);
  server.on("/E", handleLed2Apaga);
  server.on("/F", handleLed2Pisca);

  // Led3
  server.on("/G", handleLed3Acende);
  server.on("/H", handleLed3Apaga);
  server.on("/I", handleLed3Pisca);

  // Led4
  server.on("/J", handleLed4Acende);
  server.on("/K", handleLed4Apaga);
  server.on("/L", handleLed4Pisca);

  // Led5
  /*
  server.on("/M", handleLed5Acende);
  server.on("/N", handleLed5Apaga);
  server.on("/O", handleLed5Pisca);
  */
  
  // Led6
  /*
  server.on("/P", handleLed6Acende);
  server.on("/Q", handleLed6Apaga);
  server.on("/R", handleLed6Pisca);
  */

  server.on("/inline", [](){
    server.send(200, "text/plain", "this works as well");
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
  // Cuidas das requisições WEB
  server.handleClient();

  // Cuida do RDID

  handleRFID();
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
        Serial.println("Err?");
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
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.print(conteudo);
  Serial.println();
}


