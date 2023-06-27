#include <Servo.h>

Servo leadWheels;

//Pinout
int servo = 8;
int enMoving = 3;
int moveForward = 6;
int moveBackward = 7;

void move()
{
  analogWrite(enMoving, 255);
  digitalWrite(moveForward, HIGH);
  
  return;
}

void turn(String data)
{
  int angle = data.toInt();
  if(angle > 90)
  {
    angle = angle*1.6;
  }else if (angle < 90)
  {
    angle = angle*0.4;
  }
  leadWheels.write(angle);
  delay(250);
  
  Serial.print(angle);
}

void stop()
{
  analogWrite(enMoving, 0);
  digitalWrite(moveForward, LOW);
  
  return;
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);

  pinMode(servo, OUTPUT);
  pinMode(enMoving, OUTPUT);
  pinMode(moveForward, OUTPUT);
  pinMode(moveBackward, OUTPUT);
  leadWheels.attach(servo);
  
  Serial.println("Booting...");
  
}

void loop()
{
  if(Serial.available())
  {
    String data = Serial.readStringUntil(' ');
    if(data == "1")
    {
      move();
      while(true)
      {
        data = Serial.readString();
        
        int angle = data.toInt();
        if(angle > 90)
        {
          angle = angle*1.6;
        }else if (angle < 90)
        {
          angle = angle*0.4;
        }
        leadWheels.write(angle);
        delay(150);
      }
    }
  }
}
