//Turns LED on and off 
//through an assembly routine
#include <avr/io.h>

//Function declared in initasm.S
extern void init(void);

 int main (void)
{
  while (1) {
	  init();
//turn led on    
//PORTB = ((0 <<  PB5));

//turn led off
    PORTB = ((1 <<  PB5));
  }
  return 0;

}
