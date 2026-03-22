.data
.space 4
:texto:
.str "hello world"
texto.len = . - texto
:pro_loop:
.str "loop de ola!"
pro_loop.len = . - pro_loop
.code
:main:
mov r0 1
mov r1 texto
mov r2 texto.len
store 0 10

call print

:loop:
mov r0 1
mov r1 pro_loop
mov r2 pro_loop.len
store 0 10

call print
go p31 loop
halt
:print:
pycall r0 1 r1 r2
pycall r0 1 0 1
ret