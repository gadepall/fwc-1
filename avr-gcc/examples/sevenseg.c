//Prints a decimal number 
//on the display
#include <avr/io.h>
#include <util/delay.h>
 
int main (void)
{
	
	
 //set PD2-PD7 as output pins 0xFC=0b11111100 (binary)
  DDRD   |= 0xFC;
  //set PB0 as output pin
  DDRB    |= ((1 << DDB0));
 
  while (1) {
//turn PB0 off
//    PORTB = ((1 <<  PB0));
    PORTB = ((1 <<  PB0));
//turn PD2-PD7 on    
//    PORTD = 0b11100100; 
    PORTD = 0b11100111; 
  }

  /* . */
  return 0;

}
