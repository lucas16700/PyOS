mov "dia {} de {} de {}" b
store $0 "10"
store $1 "#agosto"
store $2 "#2025"
mov $6 rax
syscall
mov c b
mov $0 rax
syscall
>snapshot "#inicio"
store $60 $255
store $61 $255
store $62 $255 
mov $7 rax
syscall
mov $0 r4 
mov $0 r5
mov $255 d
mov $1 f
mov $1 h
point "#main"
mov $1 rgx
xcall
mov $4 rgx
xcall
cmp ist $0
jnz $4
>goback "#inicio"
mov $5 rgx
xcall g3
halt
mov $3 rgx
load $60 d
until d $256 d
list b d
load $61 d
until d $256 d
list_append b d 
load $62 d
until d $256 d
list_append b d
until r4 $800 r4
until r5 $600 r5
until f $801 f
until h $601 h
list c r4 r5
xcall c b
mov $0 rgx
xcall
sub f $400 g
add r4 g r4
sub h $300 g
add r5 g r5
add f f f
add h h h
load $60 g0
load $61 g1
load $62 g2
add g0 $2 g0
add g1 $3 g1
add g2 $5 g2
store $60 g0
store $61 g1
store $62 g2
until g0 $10 g0
until g1 $10 g1
until g2 $10 g2

loop_p "#main"