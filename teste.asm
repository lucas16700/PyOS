set $4 #printax 
load $100 b
mov $0 rax
mov $2 r1
syscall
ret
set $4 #printay 
load $101 b
mov $0 rax
mov $2 r1
syscall
ret
halt