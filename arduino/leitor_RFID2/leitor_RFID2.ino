//Incluses no cdigo para o funcionamento adequado do leitor de RFID
#include <SPI.h>
#include <MFRC522.h>

//Definies de pinos requeridas pela biblioteca
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);        // Create MFRC522 instance.

//Definies dos pinos dos ledes e do rele
int ledverde = 14;
int ledvermelho = 15;
int rele = 6;

//Variavel auxiliar necessaria para comunicao serial
int resposta;

void setup() {
		Serial.begin(9600);        // Initialize serial communications with the PC
		SPI.begin();                // Init SPI bus
		mfrc522.PCD_Init();        // Init MFRC522 card

                //definindo os pinos de saida de dados
		pinMode(ledverde, OUTPUT); 
		pinMode(ledvermelho, OUTPUT);
		pinMode(rele, OUTPUT);
                //Garantido que eles estejam desligados ao iniciar o programa
		digitalWrite(ledverde, LOW);
		digitalWrite(ledvermelho, LOW);
		digitalWrite(rele, LOW);
}

void abri()//funcao que abre a porta e liga o led verde para indicar acesso concedido
{
	digitalWrite(ledvermelho,0);
	digitalWrite(ledverde, 1);
	digitalWrite(rele, 1);
	delay(30);
	digitalWrite(rele, 0);
	delay(2470);
	digitalWrite(ledverde,0);
}
void nao_entra()//funcao que liga o led vermelho para indicar acesso negado
{
	digitalWrite(ledvermelho,1);
	digitalWrite(ledverde, 0);
	delay(2500);
	digitalWrite(ledvermelho,0);
}

void ponto_entrada()//funcao que abre a porta e deixa o led verde intermotente para indicar que o ponto de entrada foi batido
{
        digitalWrite(ledvermelho,0);
        digitalWrite(ledverde,1);
        digitalWrite(rele, 1);
	delay(30);
	digitalWrite(rele, 0);
        delay(470);
        digitalWrite(ledverde,0);
        delay(500);
        digitalWrite(ledverde,1);
        delay(500);
        digitalWrite(ledverde,0);
        delay(500);
        digitalWrite(ledverde,1);
        delay(500);
        digitalWrite(ledverde,0);
}

void ponto_saida()//funcao que deicha o led vermelho itermitente para indicar que o ponto de saida foi batido
{
        digitalWrite(ledvermelho,1);
        digitalWrite(ledverde,0);
        delay(470);
        digitalWrite(ledvermelho,0);
        delay(500);
        digitalWrite(ledvermelho,1);
        delay(500);
        digitalWrite(ledvermelho,0);
        delay(500);
        digitalWrite(ledvermelho,1);
        delay(500);
        digitalWrite(ledvermelho,0);
}


void serialEvent()//funcao de interrupicao com gatilho serial
{
	resposta = Serial.read();
        resposta -= '0';
	if (resposta == 1)
		abri();
	else if (resposta == 2)
		ponto_entrada();
        else if (resposta == 3)
                ponto_saida();
        else if(resposta == 0)
                nao_entra();
        else if(resposta == 4)
        {
          Serial.print("%42*\n");
          Serial.flush();
        }      
}

void lerRfid()//funcao para leitura do cartao RFID e repasse do codigo via porta serial padrao 9600
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
                
                String mensagem = "@";
		for (byte i = 0; i < mfrc522.uid.size; i++) {
				 //Serial.println(String(i)+" "+String(mfrc522.uid.uidByte[i]));
				 mensagem += String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
				 mensagem += String(mfrc522.uid.uidByte[i]);
		} 
                mensagem += "#\n";
		Serial.print(mensagem);
                Serial.flush();
		
		// Halt PICC
		mfrc522.PICC_HaltA();

		// Stop encryption on PCD
		mfrc522.PCD_StopCrypto1();
}

void loop() 
{
	lerRfid();
}
