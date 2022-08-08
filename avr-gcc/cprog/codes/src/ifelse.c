//Prints the number 0 or 8 using 
//the if-else condition
#include <avr/io.h>
#include <util/delay.h>
 
int main (void)
{
	int dec = 0;
	
 //set PD2-PD7 as output pins 
  DDRD   |= 0xFC;
  //set PB0 as output pin
  DDRB    |= ((1 << DDB0));
 
  while (1) {

	if(dec == 8)
	//turn PB0 on
		PORTB = ((0 <<  0));
	//turn PB0 off
    else if(dec == 0)
		PORTB = ((1 <<  0));
//turn PD2-PD7 on    
    PORTD = 0b00000000; 
  }

  /* . */
  return 0;

}
