const int ledPin1 = 9;
const int ledPin2 = 10;
const int ledPin3 = 11;
const int tempPin = A5;
const int ldrPin = A0;

void setup() {
  Serial.begin(9600);
  
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);

  // Ensure LEDs are OFF at startup
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
}

void loop() {
  int tempValue = analogRead(tempPin);
  int ldrValue = analogRead(ldrPin);

  // Calculate temperature
  float voltage = tempValue * (5.0 / 1023.0);
  float temperatureC = (voltage - 0.5) * 100.0;

  // Display temperature
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.print(" C, ");

  // Display LDR value
  Serial.print("LDR value: ");
  Serial.println(ldrValue);

  // Adjust this threshold based on actual LDR readings
  
  // Turn LEDs ON only when it's dark (LDR value is low)
  if (ldrValue < 20) {  
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin2, HIGH);
    digitalWrite(ledPin3, HIGH);
  } else {  
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
  }

  delay(200);
}
