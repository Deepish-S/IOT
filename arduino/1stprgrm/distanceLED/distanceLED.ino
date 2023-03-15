const int trig = 11;
const int echo = 12; 

const int LED1 = 2;
const int LED2 = 3;
const int LED3 = 4;

int duration = 0;
int distance = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);
  distance = (duration/2) / 28.5;
  Serial.println(distance);

  if (distance <= 5)
  {
    digitalWrite(LED1, HIGH);
  }
  else
  {
     digitalWrite(LED1, LOW);
  }

  if (distance <= 15)
  {
    digitalWrite(LED2, HIGH);
  }
  else
  {
     digitalWrite(LED2, LOW);
  }
  
  if (distance <= 20)
  {
    digitalWrite(LED3, HIGH);
  }
  else
  {
     digitalWrite(LED3, LOW);
  }
}
