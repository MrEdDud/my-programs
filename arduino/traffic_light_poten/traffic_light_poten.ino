const int potPin = A0; // Potentiometer connected to A0
const int ledPin1 = 8; // LED connected to digital pin 11
const int ledPin2 = 9; // LED connected to digital pin 11
const int ledPin3 = 10; // LED connected to digital pin 11

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}
void loop() {
  // Read potentiometer value (0-1023)
  // Map to a delay range (100ms to 1000ms)
  int potValue = analogRead(potPin);
  int delayTime = map(potValue, 0, 1023, 100, 1000);
  digitalWrite(ledPin1, HIGH);
  delay(delayTime);
  digitalWrite(ledPin1, LOW);
  delay(delayTime);
  digitalWrite(ledPin2, HIGH);
  delay(delayTime);
  digitalWrite(ledPin2, LOW);
  delay(delayTime);
  digitalWrite(ledPin3, HIGH);
  delay(delayTime);
  digitalWrite(ledPin3, LOW);
  delay(delayTime);
}