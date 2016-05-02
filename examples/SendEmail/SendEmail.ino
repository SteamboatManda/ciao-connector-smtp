/*
Send Email

Demostrates how to use SMTP Ciao Connector for Arduino Ciao Library.
Reads temperature from analog pin every 30 seconds, if the temperature
execeeds the treshold send an alert email. After 5 mins checks again.

Parts required:
- Arduino Yun / Tian
- TMP36 temperature sensor

authors:
created 12 Apr 2016 - sergio tomasello

*/

#include <Ciao.h>

// named constant for the pin the sensor is connected to
const int sensorPin = A0;
// treshold temperature in Celcius
const float tresholdTemp = 20.0;
// Receveiver subject and body used for send emails
String emailTo = "RECEIVER EMAIL ADDRESS";//<-- SET HERE THE EMAIL ADDRESS OF THE RECEIVER
String emailSubject = "Temp. Alert";
String emailBody = "The Room Temperature is: ";

void setup() {
  Ciao.begin();
}

void loop() {
  // read the value on AnalogIn pin 0
  int sensorVal = analogRead(sensorPin);

  // convert the ADC reading to voltage
  float voltage = (sensorVal / 1024.0) * 5.0;

  // convert the voltage to temperature in degrees C
  float temperature = (voltage - .5) * 100;

  //check if the temperature exceeds the treshold
  if(temperature > tresholdTemp){
    //send an email via ciao smtp connector
    Ciao.write("smtp", emailTo, emailSubject, emailBody + temperature );
    delay(270000);
  }

  delay(30000);
}
