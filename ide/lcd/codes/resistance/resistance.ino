//Declarations
int V_out_q=0;
//V_out_q is the quantized voltage
float V_in = 5,V_out;
//V_in = V_cc
float R1=220,R2; 
//R1 is known resistance
//R2 is unknown resistance

void setup()
{
//Get the result onto the serial monitor
  Serial.begin(9600);
}

void loop()
{
//V_0ut_q is an integer between 0 to 1023
V_out_q=analogRead(0);//reading from A0

//V_out is the actual voltage at the junction of R1 and R2
V_out = V_in*V_out_q/1024;

R2 = R1*((V_in)/(V_out)-1.0);
delay(3000);
Serial.println(R2);
}

