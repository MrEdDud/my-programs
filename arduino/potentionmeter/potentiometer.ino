const int potPin = A0; // Potentiometer connected to A0
const int ledPin = 8; // LED connected to digital pin 11
void setup() {
  pinMode(ledPin, OUTPUT);
}
void loop() {
  // Read potentiometer value (0-1023)
  // Map to a delay range (100ms to 1000ms)
  int potValue = analogRead(potPin);
  int delayTime = map(potValue, 0, 1023, 100, 1000);
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin, LOW);
  delay(delayTime);
}
