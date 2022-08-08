//Turns LED on and off using AVR-GCC
#include <avr/io.h>

//Function for enabling pin 13 as output
void init(void);

 int main (void)
{
  while (1) {

	init();
//turn led on    
	PORTB = ((0 <<  PB5));

//turn led off
//    PORTB = ((1 <<  PB5));
  }

  return 0;

}
void init(void)
{
	  /* Arduino boards have a LED at PB5 */
 //set PB5, pin 13 of arduino as output
  DDRB    |= ((1 << DDB5));

}
