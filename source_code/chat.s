;entendi sua abordagem , agora queria uma opinião:
;fazer com que certas chamadas só aceitem objetos High seria uma boa escolha? como por exemplo , carregar um textura e renderizar na tela, teriam * instruções:
externf display, image_raw, render_buffer, update, events, flip, gfx_types, start_display $gfx
mov h1 imagem_bruta
mov h2 dimensoes
call image_raw &h3 ; saida em h3
getattr h5 "QUIT" gfx_types
:main_loop:
call events &h4
getattr h4 "type" h4
jin sair h4 h5
mov h1 h3
gobj h2 "size"
call render_buffer &display
call flip
j main_loop
:sair:
halt