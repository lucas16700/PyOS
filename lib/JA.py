import re,pygame
import pygame
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
def calcular_layout(
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
class Widget:
    "mae do widgets"
    DEFAULT_STYLE = {
        "size": (100, 30),
        "background": (200, 200, 200),
        "color": (0, 0, 0),
        "border radius": 0,
        "font size": 16,
        "font name":"arial",
        "position":[300,400],
        "padding":0
    }

    def __init__(self, style: dict):
        self.style = self.DEFAULT_STYLE | style
        self.surface = None
        self.rect = pygame.Rect((0, 0), self.style["size"])
        self.dirty = True  # controla quando redesenhar

    def render(self):
        """Cada widget sobrescreve isso"""
        raise NotImplementedError

    def update(self):
        "atualiza a surface do widget"
        if self.dirty:
            self.dirty = False
        self.render()
    
    def action(self,type:str,values):
        self.script.act(type)(values)

    def draw(self, screen, pos):
        "desenha em uma tela/surface"
        self.update()
        self.rect.topleft = pos
        screen.blit(self.surface, pos)

    
class UI:
    class Button(Widget):
        "botão simples"
        def __init__(self, value="Button", style=None):
            self.value = value
            super().__init__(style or {})

        def render(self):
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
        def __init__(self, value="", style=None):
            self.value = value
            super().__init__(style or {})

        def render(self):
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
        def __init__(self, value="", style=None):
            self.value = value

            super().__init__(style or {})

        def render(self):
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
            for key in self.value:
                ele:Widget=getattr(UI,self.value[key]["type"])(
                    self.value[key]["value"],
                    self.style|self.value[key]["atrr"]
                )
                ele.update()
                eles[key]=ele
                sizes[key]=ele.surface.get_size()
            layout=calcular_layout(sizes,self.style["size"][0],self.style["padding"],self.style["padding"])
            for key in layout:
                eles[key].draw(self.surface,layout[key])
            #ele.draw(self.surface,ele.style["position"])
        def __repr__(self):
            return f"<UI.TxtBox value={self.value.__repr__()}>"
TOKEN_REGEX = re.compile(
    r'''\s*(
        [-+]?\d+            | # números
        "(?:\\.|[^"])*"     | # strings
        [()]                | # parênteses
        [^\s()]+              # símbolos
    )''',
    re.VERBOSE
)

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

class scripts:
    def __init__(self,code:str):
        with open(code,"r")as f:
            self.ps=parser(f.read())
        self.instru=self.ps.pre()
    def make(self):
        text=self.instru[0]
        print(text)

script_base="""(program
    (target bloco)
    (def hover (a b) 
        (change color (255 255 255))
        return 0
    )
    (event hover set hover)
)
(meta
    (version 0)
    (budleid (10 2 3))
    (name "teste")
)

"""

# teste=scripts(script_base)
# teste.make()
# exit()
corpo_base={
    "body":
    { "bloco":
        {
            "value":
            {
                "buta1":
                {
                    "atrr":{"border radius":15,"size":(100,30),"color":(0,0,0),"background":(255,255,255)},
                    "type":"Button",
                    "value":"mojangao"
                },"buta2":
                {
                    "atrr":{"border radius":15,"size":(50,40),"color":(0,0,0),"background":(255,255,255)},
                    "type":"Button",
                    "value":"EA"
                },"buta3":
                {
                    "atrr":{"border radius":15,"size":(50,10),"color":(0,0,0),"background":(255,255,255)},
                    "type":"Button",
                    "value":"ubsoft"
                },
                "bloco":{
                    "atrr":{"size":(300,130),"border radius":50,"background":(2,50,40)},
                    "type":"Box",
                    "value":
                        {"buta4":
                    {
                        "atrr":{"border radius":15,"size":(70,60),"color":(0,0,0),"background":(255,255,255)},
                        "type":"Button",
                        "value":"nintendo"
                    },"buta5":
                    {
                        "atrr":{"border radius":15,"size":(100,30),"color":(0,0,0),"background":(255,255,255)},
                        "type":"Button",
                        "value":"Rock Star"
                    },"buta6":
                    {
                        "atrr":{"border radius":15,"size":(75,60),"color":(0,0,0),"background":(255,255,255)},
                        "type":"Button",
                        "value":"Steam"
                    },
                    }
                }
            },
            "atrr":{"size":(400,200),"border radius":50,"background":(70,50,80)},
            "type":"Box"
        }
    }
}
elements={}
logo=pygame.image.load("lib/logo.png")

class boot:
    def __init__(self,cpu):
        self.tread=cpu
        self.tread.reg
    def init(self,size,ui):
        pygame.init()
        pygame.font.init()
        self.window=pygame.display.set_mode(size)
        self.elements={}
        body=ui
        print(body)
        for key in body:
            self.elements[key]=getattr(UI,body[key]["type"])(body[key]["value"],body[key]["atrr"])
            self.elements[key].update()
        x=size[0]/2-400
        y=size[1]/2-400
        self.window.blit(logo,(x,y))
    def update(self):
        pygame.display.update()
    def event_manager(self):
        events=[]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return ["quit"]
            events.append(event)
    def draw_ui(self):
        for key in self.elements:
            self.elements[key].draw(self.window,self.elements[key].style["position"])
    def ui_patch(self,key,value):
        self.elements[key]=getattr(UI,value["body"][key]["type"])(value["body"][key]["value"],value["body"][key]["atrr"])
        self.elements[key].update()
    def ui_pop(self,key):
        self.elements.pop(key)
    
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
