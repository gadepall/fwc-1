//Declarations
int A=0,B=0,C=0,D=0,a,b,c,d,e,f,g,W,X,Y,Z,i,j,thisPin;
int ledPins[]={2,3,4,5,6,7,8,9,10};
int pinCount=9;
int r0; 
unsigned int initialtime, elapsed;
void showit(int x);

void setup()
{
//Declaring output pins
for( thisPin=0;thisPin < pinCount; thisPin++)
{
pinMode(ledPins[thisPin], OUTPUT);
}
}
void loop()
{ 
//Decade Counting
for( r0=0;r0<=9;r0++)
{ 
initialtime=millis();
//Counting 1000 milliseconds
for(elapsed=0;elapsed<=1000;elapsed=millis()-initialtime)
{
//Keep display on
digitalWrite(9,HIGH);

//Write number to display
showit(r0);

}//end counting 10 sec
} //end counting 1 sec
}// end void 

//Display logic
void showit(int x)
{
int D,C,B,A;

//Decimal to Binary conversion
A=x%2;
x=x/2;
B=x%2;
x=x/2;
C=x%2;
x=x/2;
D=x%2;

//BCD to seven segement decoder
a=(!D&&!C&&!B&&A)||(!D&&C&&!B&&!A);
b=(!D&&C&&!B&&A)||(!D&&C&&B&&!A);
c=(!D&&!C&&B&&!A);
d=(!D&&!C&&!B&&A)||(!D&&C&&!B&&!A)||(!D&&C&&B&&A);
e=(!D&&!C&&!B&&A)||(!D&&!C&&B&&A)||(!D&&C&&!B&&!A)||(!D&&C&&!B&&A)||(!D&&C&&B&&A)||(D&&!C&&!B&&A);
f=(!D&&!C&&!B&&A)||(!D&&!C&&B&&!A)||(!D&&!C&&B&&A)||(!D&&C&&B&&A);
g=(!D&&!C&&!B&&!A)||(!D&&!C&&!B&&A)||(!D&&C&&B&&A);

//Writing to display
digitalWrite(2,a);
digitalWrite(3,b);
digitalWrite(4,c);
digitalWrite(5,d);
digitalWrite(6,e);
digitalWrite(7,f);
digitalWrite(8,g);
}

