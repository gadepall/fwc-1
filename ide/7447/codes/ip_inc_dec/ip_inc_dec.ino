//Declaring all variables as integers
int Z,Y,X,W;

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int D, int C, int B, int A)
{
  digitalWrite(2, A); //LSB
  digitalWrite(3, B); 
  digitalWrite(4, C); 
  digitalWrite(5, D); //MSB

}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, INPUT);  
    pinMode(7, INPUT);
    pinMode(8, INPUT);
    pinMode(9, INPUT);
    
}

// the loop function runs over and over again forever
void loop() {
  
W = digitalRead(6);//LSB  
X = digitalRead(7);  
Y = digitalRead(8);  
Z = digitalRead(9);//MSB  
  
disp_7447(Z,Y,X,W);  
}
