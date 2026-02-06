UI "init" "r#800 600" corpo
point "#main"
UI "event_manager"
UI "fill" "r#0 0 0"
UI "draw_ui"
UI "update"
CMP x11 $1
jnz $1
loop_p "#main"
halt