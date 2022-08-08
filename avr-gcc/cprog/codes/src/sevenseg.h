void sevenseg(int dec)
{
switch(dec)
{
case 0:
    PORTB = ((1 <<  0));
    PORTD = 0b00000000; 
    break;
case 1:
    PORTB = ((1 <<  0));
    PORTD = 0b11100100; 
    break;
case 2:
    PORTB = ((0 <<  0));
    PORTD = 0b10010000; 
    break;
case 3:
	PORTB = ((0 <<  0));
	PORTD = 0b11000000; 
	break;
case 4:
	PORTB = ((0 <<  0));
	PORTD = 0b01100100; 
	break;
case 5:
	PORTB = ((0 <<  0));
	PORTD = 0b01001000; 
	break;
case 6:
	PORTB = ((0 <<  0));
	PORTD = 0b00001000; 
	break;
case 7:
	PORTB = ((1 <<  0));
	PORTD = 0b11100000; 
	break;
case 8:
	PORTB = ((0 <<  0));
	PORTD = 0b00000000; 
	break;
case 9:
	PORTB = ((0 <<  0));
	PORTD = 0b01000000; 
	break;
default:
	PORTB = ((0 <<  0));
	PORTD = 0b00011000; 
	break;
}
}
