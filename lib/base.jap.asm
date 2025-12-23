mov "#block" a
widget set a
set $2 "#hover" int x int y
UI "change_style" "#block" "#color"
ret ['RETURN', 0]
UI_event set "#hover" "#hover"
set $2 "#quit" int a
halt
ret ['RETURN', 0]
halt
UI_event set "#!event.quit" "#quit"