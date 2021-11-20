#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <Adafruit_NeoPixel.h>

#ifndef STASSID
#define STASSID "b1"
#define STAPSK  "ed174b4c5e"
#endif
#define LED_PIN    14
#define LED_COUNT  200

const char* ssid     = STASSID;
const char* password = STAPSK;

ESP8266WebServer server(80);
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ400);


void handlePlain() {
    if (server.method() == HTTP_POST) {
        server.send(200, "text/plain",  "0");
        String s = server.arg("plain");
        for( int p=0; p<s.length()/6; p++ ) {        

            int g = hex2int( s[p*6+0],s[p*6+1] );
            int r = hex2int( s[p*6+2],s[p*6+3] );
            int b = hex2int( s[p*6+4],s[p*6+5] );
            strip.setPixelColor(p, strip.Color(r,g,b));  
        }
        strip.show(); 
    }
}

int hex2int( int a, int b ) {
    int r = h2i( a )*16 + h2i(b);
    if( r < 0 ){
        r = 0; 
    }
    if( r >255 ){
        r = 255; 
    }
    return r;
}

int h2i ( int a ) {
    int r = a-'0';
    if( r>10 ) {
        r -= 7;
    }
    return r;
}

void setup(void) {
    Serial.begin(115200);
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
    Serial.print("IP address:");
    Serial.println(WiFi.localIP());
    if (MDNS.begin("esp8266")) {
        Serial.println("MDNS responder started");
    }
    server.on("/led/", handlePlain);
    server.begin();
    Serial.println("HTTP server started");
    strip.begin();
    for(int i=0; i<200; i++) { 
        strip.setPixelColor(i, strip.Color(4,0,4));  
    }
    strip.show();  
    for(int i=1; i<200; i++) { 
        strip.setPixelColor(i, strip.Color(100,0,100));  
        strip.setPixelColor(i-1, strip.Color(4,0,4));  
        strip.show(); 
    }
    for(int i=0; i<200; i++) { 
        strip.setPixelColor(i, strip.Color(4,0,4));  
    }
    strip.show();  
  
 }

void loop(void) {
    server.handleClient();
}
