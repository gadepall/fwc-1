.include "/home/gadepall/m328Pdef.inc"
ldi r31,0b00100001
out DDRB,r31
ldi r16, 0
out SREG , r16
ldi r16 ,low (RAMEND) 
out SPL , r16
ldi r16 ,high (RAMEND) 
out SPH , r16
ldi r27,0b00000000
ldi r28,0b00000001
comp:
eor r27,r28
out PORTB,r27
call wait
rcall comp

wait:
    push r16
    push r17
    push r18

    ldi r16,0x50
    ldi r17,0x00
    ldi r18,0x00

w0:
    dec r18
    brne w0
    dec r17
    brne w0
    dec r16
    brne w0
    pop r18
    pop r17
    pop r16
    ret
