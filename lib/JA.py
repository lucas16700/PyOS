import re,pygame,json,asyncio
from rich import print
def primo(x):
    a=[2]
    for i in range(2,x+1):
        prim=True
        for v in a:
            if i%v==0:
                # print(i,v,i%v)
                prim=False
                break
        if prim:
            a.append(i)
    return a
async def calcular_layout(
    items,
    container_width,
    start_x=0,
    start_y=0,
    spacing_x=0,
    spacing_y=0
):
    """
    Calcula posições (x, y) para itens de tamanhos variados
    em um fluxo horizontal com quebra de linha.

    items: lista de dicts com 'width' e 'height'
    container_width: largura máxima do bloco
    spacing_x: espaço horizontal entre itens
    spacing_y: espaço vertical entre linhas
    """

    x = start_x
    y = start_y
    line_height = 0

    layout = {}

    for key in items:
        w = items[key][0]
        h = items[key][1]

        # Se não couber na linha atual, quebra linha
        if x + w > container_width:
            x = start_x
            y += line_height + spacing_y
            line_height = 0

        # Salva posição do item
        layout[key]=[x,y]

        # Atualiza cursor horizontal
        x += w + spacing_x

        # Atualiza altura da linha
        line_height = max(line_height, h)

    return layout
class layout:
    def __init__(self,values:dict):
        self.values=values.copy()
        self.old=True
    def turn(self):
        self.old=False
    def copy(self):
        return layout(self.values.copy())
    def __dict__(self):
        return self.values
    def __repr__(self):
        return str(self.values)
    def __getitem__(self,__key):
        return self.values[__key]
    def __setitem__(self,__key,__value):
        # print(self)
        self.values[__key]=__value
        self.old=True
class Events:
    def __init__(self,widget:"Widget"):
        self.obj=widget
        self.job:dict=JIT(widget.__events__).results
    def __getitem__(self,__values):
        __value,selfu=__values
        if __value in self.job.keys():
            self.job.get(__value)(selfu)
class pre_build:
    def change_style(self,__key,__value):
        self.style[__key]=__value
        # print(f"changed {__value}")
    def change_type(self,__type):
        getattr(UI,__type).__init__(self,self.value,self.style,self.child)
def prebuild(fn):
    def binder(*args, **kwargs):
        # aqui args/kwargs são os dados do script
        def executor(obj):
            # aqui obj será seu widget real
            return fn(obj, *args, **kwargs)
        return executor
    return binder
class JIT:
    def __init__(self,code:list):
        temp={}
        # print("code",code)
        for key in code:
            temps=code[key]["JIT"]
            if temps:
                temp[key]=self.compile(code[key]["script"])
            
        self.results={temper:temp[temper] for temper in temp}
    
    auto={
        "change_style":prebuild(pre_build.change_style)
    }
    def compile(self,lines:list):
        parans=[]
        for line in lines:
            intru=line[0]
            parans.append(self.auto[intru](*line[1:]))
        return parans

DEFAULT_EVENTS = {
        "hover_enter": {
            "script": ("change_style" ,"background", (100, 100, 100, 200)),
            "JIT": True
        },
        "hover": {
            "script": None,
            "JIT": False
        },
        "hover_leave": {
            "script": ("change_style" ,"background", (255, 255, 255, 100)),
            "JIT": True
        },
        "click_in": {
            "script": ("change_style" ,"background", (0, 255, 0, 100)),
            "JIT": True
        },
        "click_out": {
            "script": ("change_style" ,"background", (255, 0, 0, 100)),
            "JIT": True
        },
        "focus": {
            "script": None,
            "JIT": False
        },
        "blur": {
            "script": None,
            "JIT": False
        }
    }
    
class Widget:
    "mae do widgets"
    DEFAULT_STYLE = {
        "size": (100, 30),
        "background": (200, 200, 200),
        "color": (0, 0, 0),
        "border radius": 0,
        "font size": 16,
        "font name":"arial",
        "position":(0,0),
        "padding":0,
    }
    
    def __init__(self, style: dict,events: dict=DEFAULT_EVENTS,childs:None|dict["Widget"]=None):
        self.style = layout(self.DEFAULT_STYLE | style).copy()
        # print("eventos",events)
        self.__events__ = DEFAULT_EVENTS| events
        self.events=Events(self)
        self.tags={
            "hover":False
        }
        self.dad=""
        self.surface = None
        self.rect = pygame.Rect((0, 0), self.style["size"])
        self.dirty = True  # controla quando redesenhar
        self.child=childs
        self.events_allow=False
    def render(self):
        """Cada widget sobrescreve isso"""
        raise NotImplementedError
    async def event_act(self,event):
        if self.child:
                for key in self.child:
                    
                    h=asyncio.create_task(self.child[key].event_act(event))
                    await h
        if event.type==pygame.MOUSEMOTION:
            
            
            
        
                # self.elements:dict[Widget|UI.Box]
            
            target:Widget=self
            surf:pygame.Surface=target.surface
            topl=target.style["position"].copy()
            trect=surf.get_rect(topleft=topl)
            if trect.collidepoint(event.pos) and not target.tags["hover"]:
                self.tags["hover"]=True
                event_final="hover_enter"
            elif trect.collidepoint(event.pos) and target.tags["hover"]:
                self.tags["hover"]=True
                event_final="hover"
            elif not trect.collidepoint(event.pos) and target.tags["hover"]:
                self.tags["hover"]=False
                event_final="hover_leave"
            else:
                return
        
            self.events[event_final,self]
            x=asyncio.create_task(self.render())
            await x
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            
            
        
                # self.elements:dict[Widget|UI.Box]
            
            target:Widget=self
            surf:pygame.Surface=target.surface
            topl=target.style["position"].copy()
            trect=surf.get_rect(topleft=topl)
            if target.tags["hover"]:
                event_final="click_in"
            elif not target.tags["hover"]:
                self.tags["hover"]=False
                event_final="click_out"
            
            # print(event_final)
            self.events[event_final,self]
            x=asyncio.create_task(self.render())
            await x
    async def update(self):
        "atualiza a surface do widget"
        self.events_allow=True
        if self.style.old:
            rende=asyncio.create_task(self.render())
            await rende
            self.style.turn()
            # print("updated")
    async def draw(self, screen:pygame.Surface, pos):
        "desenha em uma tela/surface"
        h=asyncio.create_task(self.update())
        await h
        self.rect.topleft = pos
        screen.blit(self.surface, pos)
        if self.child:

            for key in self.child:
                # print(f"key {key}",self.child[key].style["position"])
                x=asyncio.create_task(self.child[key].draw(screen,self.child[key].style["position"]))
                await x
    def make(self,childs):
        # print(childs)
        nwid={}
        for key in childs:
            tip=childs[key].pop("type")
            nwid[key]=getattr(UI,tip)(**childs[key])
        return nwid
    
class UI:
    class Button(Widget):
        "botão simples"
        def __init__(self, value="Button", style=None,child=None,events: dict=DEFAULT_EVENTS):
            self.value = value
            super().__init__(style or {},events)

        async def render(self):
            size = self.style["size"]
            bg = self.style["background"]
            color = self.style["color"]
            ff = self.style["font name"]

            self.surface = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(
                self.surface,
                bg,
                self.surface.get_rect(),
                border_radius=self.style["border radius"]
            )

            font = pygame.font.SysFont(ff, self.style["font size"])
            txt = font.render(self.value, True, color)
            txt_rect = txt.get_rect(center=self.surface.get_rect().center)
            self.surface.blit(txt, txt_rect)
        def __repr__(self):
            return f"<UI.Button value={self.value.__repr__()}>"
    class TextBox(Widget):
        "Caixa de texto simples"
        def __init__(self, value="", style=None,child=None,events: dict=DEFAULT_EVENTS):
            self.value = value
            super().__init__(style or {},events)

        async def render(self):
            self.surface = pygame.Surface(self.style["size"])
            self.surface.fill(self.style["background"])
            ff = self.style["font name"]
            font = pygame.font.SysFont(ff, self.style["font size"])
            txt = font.render(self.value, True, self.style["color"])
            txt_rect = txt.get_rect(center=self.surface.get_rect().center)
            
            self.surface.blit(txt, txt_rect)
        def __repr__(self):
            return f"<UI.TxtBox value={self.value.__repr__()}>"
    class Box(Widget):
        "Caixa de texto simples"
        def __init__(self, value="", style=None,child={},events: dict=DEFAULT_EVENTS):
            self.value = value
            fc=self.make(child)
            for i in fc:
                fc[i].dad+="box"
            super().__init__(style or {},childs=fc,events=events)
            
                # print(key,self.child[key].style["position"])
            # print([{key:self.child[key].style["position"]} for key in self.child_layout])

        async def render(self):
            size = self.style["size"]
            bg = self.style["background"]
            color = self.style["color"]
            ff = self.style["font name"]

            self.surface = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(
                self.surface,
                bg,
                self.surface.get_rect(),
                border_radius=self.style["border radius"]
            )
            eles={}
            sizes={}
            self.child_layout={}
            for key in self.child:
                ele:Widget=self.child[key]
                x=asyncio.create_task(ele.update())
                await x
                eles[key]=ele
                sizes[key]=ele.surface.get_size()
            self.child_layout=await calcular_layout(sizes,self.style["size"][0],self.style["padding"],self.style["padding"])
            for key in self.child_layout:
                h=asyncio.create_task(self.child[key].update())
                await x
                # print(key,self.child_layout[key],self.child[key].style["position"])
                cp=self.style["position"].copy()
                cp[0]+=self.child_layout[key][0]
                cp[1]+=self.child_layout[key][1]
                self.child[key].style["position"]=cp
            # print(self.child)
            # for key in self.child:
            #     ele:Widget=self.child[key]
            #     ele.update()
            #     eles[key]=ele
            #     sizes[key]=ele.surface.get_size()
            # self.child_layout=calcular_layout(sizes,self.style["size"][0],self.style["padding"],self.style["padding"])
            # print(30*"#")
            # for key in layout:
                
            #     self.child[key].style["position"][0]=self.style["position"][0]+layout[key][0]
            #     self.child[key].style["position"][1]=self.style["position"][1]+layout[key][1]
            # print(30*"#")
                # eles[key].draw(self.surface,layout[key])
        def __repr__(self):
            return f"<UI.Box value={self.value.__repr__()}>"
TOKEN_REGEX = re.compile(
    r'''\s*(
        [-+]?\d+            | # números
        "(?:\\.|[^"])*"     | # strings
        [()]                | # parênteses
        [^\s()]+              # símbolos
    )''',
    re.VERBOSE
)
def replacer(arg:str):
    if type(arg)==str:
        if "!key." in arg:
            arg=arg.removeprefix("!key.")
            return f'${getattr(pygame,"K_"+arg)}'
        elif "!event." in arg:
            # print("arg",arg)
            arg=arg.removeprefix("!event.")
            return f'${getattr(pygame,arg.upper())}'
    return arg
class parser:
    def __init__(self,code):
        self.code=code
    def pre(self):
        self.__tokenize__()
        return self.__parse__()
    def __tokenize__(self):
        self.token= TOKEN_REGEX.findall(self.code)

    def __parse__(self):
        self.token
        def parse_expr():
            token = self.token.pop(0)

            if token == '(':
                lst = []
                while self.token[0] != ')':
                    lst.append(parse_expr())
                self.token.pop(0)  # remove ')'
                return lst

            elif token.startswith('"'):
                return token[1:-1]  # string sem aspas

            elif token.isdigit():
                return int(token)

            else:
                return token  # símbolo

        ast = []
        while self.token:
            ast.append(parse_expr())
        return ast
class __parser__:
    def __init__(self,code:list[list|str|int]):
        self.code=[]
        for xcode in code:
            tempv=[replacer(fin) for fin in xcode[1:]]
            self.code.append(getattr(self,xcode[0].upper())(tempv))
        self.name="undefined"
        # print("code full:\n","\n".join(self.code),"\nend of full code")
    def recall(self,code):
        temp=[]
        for xcode in code:
            tempv=[replacer(fin) for fin in xcode[1:]]
            temp.append(getattr(self,xcode[0].upper())(tempv))
        return "\n".join(temp)
    def name_set(self,name):
        self.name=name
    def __str__(self):
        # print(self.code)
        return "\n".join(self.code)
    def __dict__(self):
        return {"code":{self.code}}
    def TARGET(self,values):
        self.target=values[1]
        return ""
        # return f'mov "#{values[1]}" a\nwidget {values[0]} a'
    def CHANGE(self,values):
        # print("change used here")
        return f'UI "change_style" "#{self.target}" "#{values[0]}"'
    def EVENT(self,values):
        return f'UI_event {values[1]} "{values[2]}" "${values[0]}"'
    def HALT(self,values):
        return "halt"
    def DEF(self,values):
        name,var,code,retur=values
        # print("code is :",code)
        final_f=self.recall(code)+"\n"
        # print("final_f",final_f)
        sizes=final_f.count("\n")+1
        starter=f'set ${sizes}'+f' "#{name}" '+" ".join(var)+"\n"
        ender=f"ret {retur[1]}"
        return starter+final_f+ender
class scripts:
    def __init__(self,code:str):
        with open(code,"r")as f:
            self.ps=parser(f.read())
        self.instru=self.ps.pre()
    def make(self):
        text=self.instru[0]
        name=self.instru[0].pop(0)
        self.codes=__parser__(text)
        self.codes.name_set(name)
    def __str__(self):
        return str(self.codes)
script_base="""(program
    (target bloco)
    (def hover (a b) 
        (change color (255 255 255))
        (return 0)
    )
    (event hover set hover)
)
(meta
    (version 0)
    (budleid (10 2 3))
    (name "teste")
)

"""
if __name__=="mojang":
    from pyos import pyos64
# teste=scripts(script_base)
# teste.make()
# exit()
# corpo_base={ "bloco":
#         {"value":"",
#             "child":
#             {
#                 "buta1":
#                 {
#                     "style":{"border radius":15,"size":(100,30),"color":(0,0,0),"background":(255,255,255)},
#                     "type":"Button",
#                     "value":"mojangao"
#                 },"buta2":
#                 {
#                     "style":{"border radius":15,"size":(50,40),"color":(0,0,0),"background":(255,255,255)},
#                     "type":"Button",
#                     "value":"EA"
#                 },"buta3":
#                 {
#                     "style":{"border radius":15,"size":(50,10),"color":(0,0,0),"background":(255,255,255)},
#                     "type":"Button",
#                     "value":"ubsoft"
#                 },
#                 "blocos":{
#                     "style":{"size":(300,130),"border radius":50,"background":(2,50,40),"position":(0,0)},
#                     "type":"Box",
#                     "value":"",
#                     "child":
#                         {"buta4":
#                     {
#                         "style":{"border radius":15,"size":(70,60),"color":(0,0,0),"background":(255,255,255)},
#                         "type":"Button",
#                         "value":"nintendo"
#                     },"buta5":
#                     {
#                         "style":{"border radius":15,"size":(100,30),"color":(0,0,0),"background":(255,255,255)},
#                         "type":"Button",
#                         "value":"Rock Star"
#                     },"buta6":
#                     {
#                         "style":{"border radius":15,"size":(75,60),"color":(0,0,0),"background":(255,255,255)},
#                         "type":"Button",
#                         "value":"Steam"
#                     },
#                     }
#                 }
#             },
#             "style":{"size":(400,200),"border radius":50,"background":(70,50,80,.5),"position":(300,300)},
#             "type":"Box"
#         }
#     }
corpo_base={
    'corpo': {
        'value': '',
        'style': {
            'size': [400, 200], 
            'border radius': 50, 
            'background': [255, 0, 0, 100], 
            'position': [300, 300]},
        'type': 'Box',
        'events':{
            'hover_leave':{
                "script": ("change_style" ,"background", [255, 0, 0, 100]),
                "JIT": True
            },
            'hover_enter':{
                "script": ("change_style" ,"background", [255, 0, 0, 255]),
                "JIT": True
            }
            }
        ,'child': {
            'butao1': {
                'events':{
                    'hover_leave':{
                        "script": ("change_style" ,"background", [0, 0, 255, 100]),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": ("change_style" ,"background", [0, 0, 255, 200]),
                        "JIT": True
                    }
                    },
                'style': 
                {'border radius': 15, 
                'size': [100, 30], 
                'color': [0, 0, 0], 
                'background': [255, 255, 255]}, 
                'type': 'Button', 
                'value': 'pressione'
                },
            'blocos': {
                'events':{
                    'hover_leave':{
                        "script": ("change_style" ,"background", [0, 255, 0, 100]),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": ("change_style" ,"background", [0, 255, 0, 200]),
                        "JIT": True
                    }
                    },
                'style': 
                {'size': [300, 130], 
                'border radius': 50, 
                'background': [2, 50, 40], 
                'position': [0, 0]},
                'type': 'Box',
                'value': '',
                'child': {
                    'butao1': {'events':{
                    'hover_leave':{
                        "script": ("change_style" ,"background", [0, 0, 255, 100]),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": ("change_style" ,"background", [0, 0, 255, 200]),
                        "JIT": True
                    }
                    },
                        'style': 
                        {'border radius': 15, 
                        'size': [70, 60], 
                        'color': [0, 0, 0], 
                        'background': [255, 255, 255]}, 'type': 'Button', 
                        'value': 'pressione'}
                }
            }
        }
    }
}
elements={}
logo=pygame.image.load("lib/logo.png")
with open("corpo_base.json","w")as f:
    json.dump(corpo_base,f)
class boot:
    def __init__(self,cpu):
        self.tread:pyos64=cpu
        self.tread.reg
        self.event_funcs={}
    async def init(self,size,ui):
        pygame.init()
        pygame.font.init()
        self.clock=pygame.time.Clock()
        self.clock.tick()
        print("ja api inited")
        print(size)
        self.window=pygame.display.set_mode(size)
        self.elements={}
        body=ui
        print(body)
        self.tread.reg["x11"]=1
        print("x11  ==",self.tread.reg["x11"])
        for key in body:
            tip=body[key].pop("type")
            self.elements[key]=getattr(UI,tip)(**body[key])
            x=asyncio.create_task(self.elements[key].update())
            await x
        x=size[0]/2-400
        y=size[1]/2-400
        self.window.blit(logo,(x,y))
    async def update(self):
        pygame.display.update()
    async def load_script(self,funcs):
        print(funcs)
        for key in funcs:
            self.event_funcs[key]=funcs[key]
        # print("script loaded",self.event_funcs)
    async def load_ui(self,file,output):
        with open(file,"r")as f:
            meta=json.load(f)
        # print("output ",output)
        self.tread.reg[output]=meta
    async def event_manager(self):
        pygame.display.set_caption(str(self.clock.get_fps()))
        self.clock.tick()
        for event in pygame.event.get():
            await asyncio.sleep(0.01)
            [await self.elements[key].event_act(event) for key in self.elements]
                    # self.elements:dict[Widget|UI.Box]
            if event.type==pygame.QUIT:
                self.tread.reg["x11"]=0
            tp= self.event_funcs.get(event.type,"")
            if tp != "":
                self.tread.call([tp])
    async def syscall(self,atrr,values):
        getattr(pygame,atrr)(*values)
    async def fill(self,color):
        self.window.fill(color)
    async def draw_ui(self):
        for key in self.elements:
            x=asyncio.create_task(self.elements[key].draw(self.window,self.elements[key].style["position"]))
            await x
    async def ui_patch(self,key,value:dict):
        tip=value.pop("type")
        self.elements[key]=getattr(UI,tip)(**value)
        self.elements[key].update()
    async def ui_pop(self,key):
        self.elements.pop(key)
    async def sytle_change(self,obj,key,nvalue):
        self.elements[obj].style[key]=nvalue
        self.elements[obj].update()
# teste=boot((1200,800),corpo_base)
# while True:
#     teste.event_manager()

#     teste.draw_ui()

#     teste.update()

if __name__ == "__main__":
    for key in corpo_base["body"]:
        elements[key]=getattr(UI,corpo_base["body"][key]["type"])(corpo_base["body"][key]["value"],corpo_base["body"][key]["atrr"])
        elements[key].update()
    print(elements)
    pygame.init()
    pygame.font.init()
    tela=pygame.display.set_mode((800,600))
    while True :
        for event in pygame.event.get():
            if pygame.QUIT==event.type:
                exit(pygame.quit())
        tela.fill(0) 
        for key in corpo_base["body"]:
            elements[key].update()
            elements[key].draw(tela,(300,260))
        
        
        # print(elements["butao"].style["border radius"],ax)
        pygame.display.flip()
