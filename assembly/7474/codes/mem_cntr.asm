.include "/home/gadepall/m328Pdef.inc"
ldi r16,0
out SREG,r16
ldi r16 ,low(RAMEND)
out SPL,r16
ldi r16,high(RAMEND)
out SPH,r16
ldi r16,0b00111100
out DDRD,r16
ldi xl,0x00
ldi xh,0x01
ldi r16,0b00000000
st x,r16
ldi r17,0x09
loop_cnt:
inc r16
inc xl
st x,r16
dec r17
brne loop_cnt
Start:
ldi r17,0x0A
clr xl
loop_inc:
ldi r16,0b00000010

ld r0,x
loopw:
lsl r0
dec r16
brne loopw
out PORTD,r0
call wait
inc xl
dec r17
brne loop_inc
rjmp Start
wait:
push r16
push r17
push r18
ldi r16,0x20
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




