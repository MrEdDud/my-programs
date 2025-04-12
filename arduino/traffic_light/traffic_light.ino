const int ledPin1 = 8;
const int ledPin2 = 9;
const int ledPin3 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin1, HIGH);
  Serial.println("GREEN");
  delay(1000);
  digitalWrite(ledPin1, LOW);
  Serial.println("GREEN OFF");
  delay(1000);
  digitalWrite(ledPin2, HIGH);
  Serial.println("YELLOW");
  delay(1000);
  digitalWrite(ledPin2, LOW);
  Serial.println("YELLOW OFF");
  delay(1000);
  digitalWrite(ledPin3, HIGH);
  Serial.println("RED");
  delay(1000);
  digitalWrite(ledPin3, LOW);
  Serial.println("RED OFF");
  delay(1000);
}
