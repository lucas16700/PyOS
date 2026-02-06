UI "init" r"800 600" corpo
> aqui ele pega o 'corpo' da nvram diretamente!
set $4 "main"
UI "event_manager"
UI "fill" r"0 0 0"
UI "draw_ui"
UI "update"
CMP x11 $1
jnz $1
call "main"
halt