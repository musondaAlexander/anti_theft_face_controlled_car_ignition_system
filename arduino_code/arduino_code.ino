//This code is meant to test the input coming from the seria monitor using python.
//It can also be tested using the Inbuilt Serial Monitor of the Arduino.
String myCmd;

void setup() {
  Serial.begin(9600);
}

void  loop() {
  while (Serial.available()==0){
    pinMode(13, OUTPUT);
  }
  myCmd = Serial.readStringUntil('\r'); 
  if(myCmd == "accessGranted"){
    digitalWrite(13,HIGH);
  }
   else if(myCmd == "accessDenied"){
    digitalWrite(13,LOW);
  }

}