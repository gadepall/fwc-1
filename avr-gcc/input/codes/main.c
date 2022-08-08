//Takes a number as input and prints the next number as output

#include <avr/io.h>

#include <util/delay.h>

#include <stdbool.h>




int main (void)

{

 bool A,B,C,D;

 bool a=0,b=0,c=0,d=0;

        DDRD = 0b00111100;

 DDRB = 0b00100000;

 PORTD = 0b11000000;

 PORTB = 0b00000011;

        while(1){




  PORTB = ((1 <<  PB5));

  _delay_ms (200L);

  D=(!d);

  C=((c&&(!d))||((!a)&&(!c)&&(d)));

  B=((b && (!d))  (b && (!c))  ((!b) && c && d));

  A=((a && (!d)) || (b && c && d));

                PORTD = (D << 2);

                PORTD |= (C << 3);

                PORTD |= (B << 4);

                PORTD |= (A << 5);

                d = (PIND & (1 << PIND6)) == (1 << PIND6);

                c = (PIND & (1 << PIND7)) == (1 << PIND7);

                b = (PINB & (1 << PINB0)) == (1 << PINB0);

                a = (PINB & (1 << PINB1)) == (1 << PINB1);

  PORTB = ((0 <<  PB5));

   _delay_ms (200L);

 }

        return 0;

}