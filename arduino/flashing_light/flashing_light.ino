const int ledPin1 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin1, HIGH);
  Serial.println("The LED is on!");
  delay(1000);
  digitalWrite(ledPin1, LOW);
  Serial.println("The LED is off!");
  delay(1000);
}
