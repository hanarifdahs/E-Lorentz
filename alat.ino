
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <Keypad.h>
#include <WiFi.h>
#include <PubSubClient.h>



const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {23, 19, 18, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {4, 13, 15}; //connect to the column pinouts of the keypad

const char* ssid = "Djajadirejas";
const char* password = "rusman12";
//const char* mqtt_server = "192.168.43.106";
//const char* mqtt_server = "localhost";
const char* mqtt_server = "broker.hivemq.com";
unsigned long m;

WiFiClient espClient;
PubSubClient client(espClient);

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
LiquidCrystal_I2C lcd(0x27,16,2);

void setup()
{
  Serial.begin(115200);
  delay(200);
  
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Selamat Datang");
  lcd.setCursor(0,1);
  lcd.print("Di E-Lorentz");

  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, 1883);
  
}

void reconnect() {
  if (!client.connected()) {
    while (!client.connected()) {
      Serial.print("MQTT connecting ...");
      String clientId = "ClientESP32";
      if (client.connect(clientId.c_str())) {
        Serial.println("connected");
//        client.subscribe("fisika/alat");
      } else {
        Serial.print("failed, status code =");
        Serial.print(client.state());
        Serial.println("try again in 5 seconds");
        delay(5000);
      }
    }
  }
  client.loop();  
}


void loop()
{
  String mlength = "";
  char key;
  
  lcd.clear();
  lcd.print("Panjang (cm):");
  lcd.setCursor(0,1);
  while(1) {
    reconnect();
    key = keypad.getKey();  
    if (key) {
      if ( key == '*' || key == '#' ) break;
      else {
        lcd.print(key);
        mlength += key;
      }
    }
  }
  int mpanjang = mlength.toInt();
  float panjang = mpanjang/100.0;
  Serial.print("Panjang (cm): ");
  Serial.println(panjang, 4);  

  lcd.clear();
  lcd.print("Arus (mA):");
  lcd.setCursor(0,1);
  mlength = "";
  while(1) {
    reconnect();
    key = keypad.getKey();  
    if (key) {
      if ( key == '*' || key == '#' ) break;
      else {
        lcd.print(key);
        mlength += key;
      }
    }
  }
  int marus = mlength.toInt();
  float arus = marus/1000.0;
  Serial.print("Arus (mA): ");
  Serial.println(arus, 4);  
  
  int sensor = analogRead(34);
  float volt = sensor * (3.3 / 4095.0) ;
  float tesla = sensor * (3.3 / (4095.0 * 31.25)); 
  
  lcd.clear();
  lcd.print("Gaya Magnetik:");
  lcd.setCursor(0,1);
  lcd.print(tesla);
  lcd.print(" T");
  Serial.print("Gaya Magnetik (T): ");
  Serial.println(tesla);

  // 100 mT = 1V
  // 1 T = 31,25 V

  float lorentz = (float) panjang * (float) arus * tesla;
  Serial.print("Gaya Lorentz: ");
  Serial.println(lorentz,5);
  
  delay(500);
  
  lcd.print(" N");
  String payload = String(lorentz,5);
  client.publish("fisika/alat", (char*) payload.c_str() );
  unsigned long m = millis();
  while ( millis() - m < 5000 ) {
    reconnect();
  }  
}
