;7447 decoder i/o


.include "/home/gadepall/m328Pdef.inc"

	ldi r17, 0b11000011 ; identifying input pins 10,11,12,13
	out DDRB,r17		; declaring pins as input
	ldi r17, 0b11111111 ;
	out PORTB,r17		; activating internal pullup for pins 10,11,12,13  
	in r17,PINB
	
	ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
	out DDRD,r16		;declaring pins as output
	out PORTD,r17		;writing output to pins 2,3,4,5
	
Start:
	rjmp Start
	

