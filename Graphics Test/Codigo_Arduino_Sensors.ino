const char* sensor1 = "*1B1";
float valor_s1 = 0;
float valor_s2 = 0;
float valor_s3 = 0;
float valor_s4 = 0;
String leituraSerial = "";
String sensor = "";
String sensor_s1 = "";
String sensor_s2 = "";
String sensor_s3 = "";
String sensor_s4 = "";

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available() > 0){
    
    leituraSerial = Serial.readStringUntil('\n');
    leituraSerial.trim(); 
    if(leituraSerial == sensor1){
      valor_s1 = random(2600, 2800)/100.0;
      sensor_s1 = (valor_s1);
      valor_s2 = random(300, 500)/100.0;
      sensor_s2 = (valor_s2);
      valor_s3 = random(90, 200)/100.0;
      sensor_s3 = (valor_s3);
      valor_s4 = random(90, 200)/100.0;
      sensor_s4 = (valor_s4);
      
      sensor = (sensor_s1 + "," + sensor_s2 + "," + sensor_s3 + "," + sensor_s4);
      Serial.println(sensor);
    }
    else{
      Serial.println("1.23");
    }
  }
}  
