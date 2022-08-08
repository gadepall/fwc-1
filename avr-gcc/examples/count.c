#include <avr/io.h>

extern void init(void);
extern void dispReg(uint8_t);
extern void delay(uint8_t, uint8_t, uint8_t);

int main(void) {
	SREG = 0;
	SPL = (uint8_t)(RAMEND);
	SPH = (uint8_t)(RAMEND>>8);
	init();
	uint8_t a  = 7;
	
	while(1) {
		dispReg(a);
		//delay(0, 0, 20);
		//a++;
		//if(a==10)
			//a=0;
	}

	return 0;
}
