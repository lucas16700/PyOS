from make_build import app
target="source_code/programa.asm"
layout={
    "main":{
        "type":"Box",
        "value":"",
        "style":{
            "size":[200,140],
            "position":[20,50]
        },
        "child":{
            "texto":{
                "type":"TextBox",
                "value":"programa iniciado",
                "style":{
                    "color":[255,255,255],
                    "background":[255,255,255,255],
                },
                'events':{
                    'hover_leave':{
                        "script": (("change_style" ,"background", [100, 100, 100, 255]),
                                   ("change_style" ,"color", [0, 0, 0, 255])),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": (("change_style" ,"background", [255, 255, 255, 255]),
                                   ("change_style" ,"color", [0, 0, 0, 255])),
                        "JIT": True
                    }
                }
            }
        }
    }
}
schema={
    "graphics":
        [
            {
            "path":"lib/logo.png",
            "name":"logo.rgb",
            "encoding":"rgb"
            }
        ]
    ,
    "main":target,
    "nvram":{
        "corpo":layout
    },
    "modules":{}
}
programa=app("pyos64","teste_de_app",9)
programa.build(schema)
programa.run()