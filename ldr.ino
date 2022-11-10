const int ledPin = 13;
const int ldrPin = A0;
void setup() {
  Serial.begin(9600);
  pinMode(ldrPin, INPUT);
}

void loop() {
  int ldrStatus = analogRead(ldrPin);
    if (ldrStatus <= 200) {
      Serial.println("0");
    } 
    else {
      Serial.println("1");
    }
}
