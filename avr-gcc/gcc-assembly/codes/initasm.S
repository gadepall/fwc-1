;enable pin 13 of Arduino as output
#define __SFR_OFFSET 0
#include <avr/io.h>

.global init

.section .text

init:
	LDI R16,0b00100000
	OUT DDRB,R16

