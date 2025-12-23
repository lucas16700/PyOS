UI "load_ui" "#corpo_base.json" corpo
load_script "#lib/base.jap"
run_script
UI "init" "r#800 600" corpo
point "#main"
UI "event_manager"
UI "draw_ui"
UI "update" 
loop_p "#main"
halt