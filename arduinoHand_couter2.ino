int leds[] = {9, 10, 11, 12, 13};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    int fingers = Serial.parseInt();

    for (int i = 0; i < 5; i++) {
      digitalWrite(leds[i], i < fingers ? HIGH : LOW);
    }
  }
}
