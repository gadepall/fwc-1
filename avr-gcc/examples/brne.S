;Decade counter using common anode
;7-segment display & 7447 IC. Connect pins
;A-D of IC to digital pins 2-5 of arduino
#define __SFR_OFFSET 0
#include <avr/io.h>

.global init
.global dispReg
.global delay

.section .text

init:
	ldi r16, 0xfc
	out DDRD, r16
	ldi r16, 0x01
	out DDRB, r16

dispReg:
	PUSH R24
	call display
	;call delay
	POP R24
	;PUSH R24
	;swap r24
	;call display
	;call delay
	;POP R24
	ret

display:
	andi r24, 0x0f

	cpi r24, 0x00
	breq lo0
	cpi r24, 0x01
	breq lo1
	cpi r24, 0x02
	breq lo2
	cpi r24, 0x03
	breq lo3
	cpi r24, 0x04
	breq lo4
	cpi r24, 0x05
	breq lo5
	cpi r24, 0x06
	breq lo6
	cpi r24, 0x07
	breq lo7
	cpi r24, 0x08
	breq lo8
	cpi r24, 0x09
	breq lo9
	cpi r24, 0x0a
	breq loa
	cpi r24, 0x0b
	breq lob
	cpi r24, 0x0c
	breq loc
	cpi r24, 0x0d
	breq lod
	cpi r24, 0x0e
	breq loe
	cpi r24, 0x0f
	breq lof

	ret

lo0: call l0
	ret
lo1: call l1
	ret
lo2: call l2
	ret
lo3: call l3
	ret
lo4: call l4
	ret
lo5: call l5
	ret
lo6: call l6
	ret
lo7: call l7
	ret
lo8: call l8
	ret
lo9: call l9
	ret
loa: call la
	ret
lob: call lb
	ret
loc: call lc
	ret
lod: call lde
	ret
loe: call le
	ret
lof: call lf
	ret

l0:
	push r16
	ldi r16, 0b00000000
	out PORTD, r16
	ldi r16, 0b00000001
	out PORTB, r16
	pop r16
	ret

l1:
	push r16
	ldi r16, 0b11100111
	out PORTD, r16
	ldi r16, 0b00000001
	out PORTB, r16
	pop r16
	ret

l2:
	push r16
	ldi r16, 0b10010000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

l3:
	push r16
	ldi r16, 0b11000000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

l4:
	push r16
	ldi r16, 0b01100100
	out PORTD, r16
	ldi r16, 0b11000000
	out PORTB, r16
	pop r16
	ret

l5:
	push r16
	ldi r16, 0b01001000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

l6:
	push r16
	ldi r16, 0b00001000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

l7:
	push r16
	ldi r16, 0b11100000
	out PORTD, r16
	ldi r16, 0b00000001
	out PORTB, r16
	pop r16
	ret

l8:
	push r16
	ldi r16, 0b00000000
	out PORTD, r16
	ldi r16, 0b11000000
	out PORTB, r16
	pop r16
	ret

l9:
	push r16
	ldi r16, 0b01000000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

la:
	push r16
	ldi r16, 0b00100000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

lb:
	push r16
	ldi r16, 0b00001100
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

lc:
	push r16
	ldi r16, 0b00011000
	out PORTD, r16
	ldi r16, 0b00000001
	out PORTB, r16
	pop r16
	ret

lde:
	push r16
	ldi r16, 0b10000100
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

le:
	push r16
	ldi r16, 0b00011000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

lf:
	push r16
	ldi r16, 0b00111000
	out PORTD, r16
	ldi r16, 0b00000000
	out PORTB, r16
	pop r16
	ret

delay:
	DEC R24
	BRNE delay
	DEC R22
	BRNE delay
	DEC R20
	BRNE delay
	RET
