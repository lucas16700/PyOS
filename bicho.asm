
mov 9 rgx
xcall
mov 6 rgx
mov 8 rgx
xcall $255 $255 $255
mov 6 rgx
xcall $10 $10 "#snake"
xcall $10 $10 "#maca"

>"inicia a malandragem"
point "#main"
mov 1 rgx
xcall
mov 4 rgx
xcall
CMP ist $0
jnz $1
halt
mov 8 rgx
xcall $255 $255 $255
mov 7 rgx
xcall "#snake" $400 $300
mov $0 rgx 
xcall
loop_p "#main"