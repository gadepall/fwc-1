;turning led on/off
#define __SFR_OFFSET 0
#include <avr/io.h>

.global disp_led

.section .text

disp_led:
	PUSH R24
	;shifting LSB in r24 to 6th position
	LDI R20, 0b00000101	;counter = 5
	RCALL looplsl		;calling the looplsl routine
	OUT PORTB,R24		;writing output to pin 13 (PB5)
	POP R24
	RET

;loop for bit shift to left
looplsl:	
	LSL R24			;left shift
	DEC r20			;counter --
	BRNE	looplsl	;if counter != 0
	RET
