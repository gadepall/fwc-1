//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>

 
int main (void)
{
	
	
  /* Arduino boards have a LED at PB5 */
 //set PB5, pin 13 of arduino as output
  DDRB    |= ((1 << DDB5));
  while (1) {
//turn led off    
    PORTB = ((0 <<  PB5));
	_delay_ms(500);
//turn led on
    PORTB = ((1 <<  PB5));
    _delay_ms(500);
  }

  /* . */
  return 0;

}
