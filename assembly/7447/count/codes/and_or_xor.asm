;logical AND, OR and XOR operations
;output displayed using 7447 IC

.include "/home/gadepall/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output



ldi r16,0b00000000	;initializing W
ldi r17,0b00000001	;initializing X
;logical AND
;and r16,r17		;W AND X
;logical OR
;or r16,r17			;W OR X
;logical XOR
eor r16,r17			;X XOR X

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
