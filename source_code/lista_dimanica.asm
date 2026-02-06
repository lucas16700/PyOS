list b $1
mov $8 r1
mov $2 c
list_append b c
inc c 
loop r1 $2
syscall 
list_get b $1 c
push b
mov c b
syscall
pop b
list_get_bl b $2 $5 c
push b
mov c b
syscall

halt