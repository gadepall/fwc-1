//using an array 
//for decade counter
#include <avr/io.h>
#include <util/delay.h>
#include "sevenseg.h"
 
void sevenseg(int);
int main (void)
{

//defining integer array p	
 const int p[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
 int i;

  DDRD   |= 0xFC;
  //set 0 as output pin
  DDRB   |= ((1 << DDB0));
 
  while (1) 
  {
	//loop counting from 0 to 9
  for (i=0; i < 10; i++)
	{

		sevenseg(p[i]);
		_delay_ms (1000L);		
	}
	}
  /* . */
  return 0;

}
