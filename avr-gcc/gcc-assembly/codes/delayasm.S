;Delay routine for blinking LED
#define __SFR_OFFSET 0
#include <avr/io.h>

.global delay

.section .text

delay:
	DEC R24
	BRNE delay
	DEC R22
	BRNE delay
	DEC R20
	BRNE delay
	RET
