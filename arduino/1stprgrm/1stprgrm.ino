//1st program  write a program to light the led connector to pin number 13 will on for 4 second and off for 1 second
void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13,HIGH);
  delay(4000);
  digitalWrite(13,HIGH);
  delay(1500);
}
