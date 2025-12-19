dict r4
list r1 $100 $20
dict_vk r4 "#size" r1 
dict r2
dict_vk r2 "#atrr" r4
dict_vk r2 "#value" "#texto"
dict_vk r2 "#type" "#TextBox"
dict r3 
dict_vk r3 "block" r2
list r1 $800 $600
script "#lib/base.jap"
UI "init" r1 r3
point "#main"
UI "event_manager"
UI "draw_ui"
UI "update" 
loop_p "#main"
halt