from rply import LexerGenerator
from rich import print
import regex

lg = LexerGenerator()
# Tokens principais para MNEMONIC
mnemonic_patterns = r'(?i)(' + '|'.join([
    #simples
    'mov', "load","store","pss"
    #matematica
    "add","sub","div","sqr","root","until",
    #logica
    "AND","OR","XOR","NOT"
    #aritimetica binaria
    "SHL","SHR",
    #branches e jumps
    "point",
    "loop_p","loop",
    "jc","jcdl",
    "go","cgo",
    #system
    "halt",
    "ret",
    "pycall"
]) + r')\b'
print(mnemonic_patterns)
lg.ignore(r"[ \t]+")
lg.ignore(r';.*')       # ; até o fim da linha
lg.ignore(r'#.*')       # # até o fim da linha
lg.add('LINE',r"\n+")
lg.add("LINEB",r'\\')
lg.add('STRING', r'"([^"\\]|\\.)*"')
lg.add('IMMEDIATE', r'-?0x[0-9a-fA-F]+|-?\d+')

lg.add('REGISTER', r'(zero|r[0-9]+|p[0-9]+|m[0-9]|t[0-9])')
lg.add('SYMMOD',r'%(hi|lo)')
lg.add('LABEL', r':[a-zA-Z_][a-zA-Z0-9_]*:')
lg.add('SECTION',r'\.(code|data|high)')
lg.add('DIRECTIVE', 
r'\.(string|array|zero|space|align|byte|half|word|dword|globl|type|size|ident|file|asciz|ascii|quad|long|short|comm|weak|attribute)')
lg.add('MOD',r'@(code|data|high)')
lg.add("DYNATT",r'=')
lg.add('COMMA', r',')
lg.add('COLON', r':')
lg.add('LPAREN', r'\(')
lg.add('RPAREN', r'\)')
lg.add("LBRACE", r"\{")
lg.add("RBRACE", r"\}")
lg.add("LBRACKET", r"\[")
lg.add("RBRACKET", r"\]")
lg.add('CURRENT_POS', r'\.')
lg.add('MATH',r'[+\-*/]')
lg.add('MNEMONIC', mnemonic_patterns)
lg.add('SYMBOL', r'[a-zA-Z_][a-zA-Z0-9_]*')
# lg.add('DATAPOS',   r'\.')
lg.add('NONUSED',r'.([^"\\]|\\.)*')

lexer = lg.build()
with open("source_code/hello.s")as f:
    codigo=f.read()

def lexar(lexando,names=False):
    h=identificar(lexando)
    final=[]
    try:
        for item in h:
            try:
                if not names:
                    final.append(item.gettokentype())
                else:
                    if item.gettokentype()=="LINE":
                        final.append(["LINE",""])
                    final.append([item.gettokentype(),item.getstr()])
            except:
                continue
    except:
        print(lexando,"ta ruim")
        return None
    return final

def identificar(texto):
    return lexer.lex(texto)
