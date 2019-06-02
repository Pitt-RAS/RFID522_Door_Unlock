int inByte = 0;         // incoming serial byte

void setup() {
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  establishContact();  // send a byte to establish contact until receiver responds
}

void loop() {
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    Serial.println("YAYYY");
  }
}

void establishContact() {
  int i = 20;
  while (i>0) {
    Serial.println("YAYAYAYYA");   // send an initial string
    delay(500);
    i--;
  }
}
