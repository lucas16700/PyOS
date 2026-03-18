.data
:parada:
.string "sistema"
.byte 10
parada_len = . - parada

.code
mov r0 1
mov r1 parada
mov r2 parada_len
pycall r0 1 r1 r2
halt