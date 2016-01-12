#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);        // Create MFRC522 instance.

int ledverde = 4;
int ledvermelho = 5;
int rele = 6;

int resposta;

void setup() {
		Serial.begin(9600);        // Initialize serial communications with the PC
		SPI.begin();                // Init SPI bus
		mfrc522.PCD_Init();        // Init MFRC522 card

		pinMode(ledverde, OUTPUT);
		pinMode(ledvermelho, OUTPUT);
		pinMode(rele, OUTPUT);
		digitalWrite(ledverde, LOW);
		digitalWrite(ledvermelho, LOW);
		digitalWrite(rele, LOW);
}

void sim()
{
	digitalWrite(ledvermelho,0);
	digitalWrite(ledverde, 1);
	digitalWrite(rele, 1);
	delay(20);
	digitalWrite(rele, 0);
	delay(980);
	digitalWrite(ledverde,0);
}

void nao()
{
	digitalWrite(ledvermelho,1);
	digitalWrite(ledverde, 0);
	delay(1000);
	digitalWrite(ledvermelho,0);
}

void serialEvent()
{
	resposta = Serial.read();
	if (resposta == 's')
		sim();
	if (resposta == 'n')
		nao();
}

void lerRfid()
{
		// Prepare key - all keys are set to FFFFFFFFFFFFh at chip delivery from the factory.
		MFRC522::MIFARE_Key key;
		for (byte i = 0; i < 6; i++) {
				key.keyByte[i] = 0xFF;
		}
		// Look for new cards
		if ( ! mfrc522.PICC_IsNewCardPresent()) {
				return;
		}

		// Select one of the cards
		if ( ! mfrc522.PICC_ReadCardSerial()) {
				return;
		}
		// Now a card is selected. The UID and SAK is in mfrc522.uid.
		
		// Dump UDI
		for (byte i = 0; i < mfrc522.uid.size; i++) {
				Serial.println(String(i)+" "+String(mfrc522.uid.uidByte[i]));
				// Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
				// Serial.print(mfrc522.uid.uidByte[i], HEX);
		} 
		// Serial.println();
		
		// Halt PICC
		mfrc522.PICC_HaltA();

		// Stop encryption on PCD
		mfrc522.PCD_StopCrypto1();
}

void loop() 
{
	lerRfid()
}
