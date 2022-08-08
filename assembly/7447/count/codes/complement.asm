;program to complement a boolean

 
.include "/home/gadepall/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output

ldi r16,0b00000000	;A=0

rcall comp	;jumpting to comp routine below

;following code is for displaying output
;shifting LSB in r16 to 2nd position
ldi r20, 0b00000010	;counter = 2

rcall loopw		;calling the loopw routine

out PORTD,r16		;writing output to pins 2,3,4,5


Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r16			;left shift
	dec r20			;counter --
	brne	loopw	;if counter != 0
	ret

;comp routine begins
comp:
	mov r0,r16			;using r0 for computations
	ldi r16,0b00000001	;loading 1
	
	eor r16,r0			;A'=A XOR 1
	ret 				;returning from comp


