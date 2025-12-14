mov $1 a
mov "#hello world" b
syscall
mov $10 a
mov $800 b
mov $600 c
syscall
mov $120 r0
mov $11 a
syscall
mov $12 a
syscall
jmp $-5
halt