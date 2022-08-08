//Turns LED on and off 
//through an assembly routine
#include <avr/io.h>

//Function declared in initasm.S
extern void init(void);
//Function declared in displedasm.S
extern void disp_led(uint8_t);
 int main (void)
{
  while (1) {
	  init();
	//turn led on/off    	  
	  disp_led(0);//0 or 1 argument
  }
  return 0;

}
