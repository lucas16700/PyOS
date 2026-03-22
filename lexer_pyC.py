from rply import LexerGenerator
from rich import print
# import regex
lg = LexerGenerator()

lg.ignore(r"[ \t]+")
lg.ignore(r'//.*') 
lg.add("RULE",r'#[a-zA-Z_][a-zA-Z0-9_]*')
# Operadores Compostos (Devem vir ANTES dos simples)
lg.add('WALRUS', r':=')        # Para window := gfx.Window
lg.add('ARROW', r'->')         # Para o retorno da função
lg.add('DECORATOR', r'@\[native\]') # Anotação específica

# Keywords
lg.add('CONDITIONAL', r'\b(if|else|elif|while|for|until|unless)\b')

# 2. Booleanos
lg.add('BOOL', r'\b(true|false)\b')

# 3. Tipos Primitivos
lg.add('TYPE', r'\b(int|float|str|dict|list|tuple|bytes|void|fn)\b')

# 4. Matemática (Atenção à ordem: os maiores primeiro)
# O rply tenta dar match na ordem da regex. Colocamos ** e // antes de * e /
lg.add('MATH', r'\*\*|//|[-+/*%]')

# 5. Operadores de Comparação (Adicional útil)
lg.add('COMPARE', r'==|!=|<=|>=|<|>')

# 6. Atribuição e Símbolos (Como antes)
lg.add('WALRUS', r':=')
lg.add('ARROW', r'->')
# lg.add('VOID', r'\bvoid\b')

# Símbolos e Pontuação
lg.add('LBRACE', r"\{")
lg.add('RBRACE', r"\}")
lg.add('LBRACKET', r"\[")
lg.add('RBRACKET', r"\]")
lg.add('LPAREN', r"\(")
lg.add('RPAREN', r"\)")
lg.add('COMMA', r',')
lg.add('DOT', r'\.')
lg.add('COLON', r':')
lg.add('ASSIGN', r'=')

# Valores e Identificadores
lg.add('FLOAT', r'\d+\.\d+')   # Detecta 5.5 antes de detectar o 5
lg.add('INT', r'\d+')
lg.add('STRING', r'"([^"\\]|\\.)*"')
lg.add('STRING', r"'([^'\\]|\\.)*'")
lg.add('FID', r'[a-zA-Z_][a-zA-Z0-9_]*\(')
lg.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')

lg.add('NEWLINE', r'\n+')
lexer = lg.build()
def lexar(lexando,names=False):
    h=identificar(lexando)
    final=[]
    # try:
    erros=0
    while erros<1:
            try:
                erros=0
                item=h.next()
                if not names:
                    final.append(item.gettokentype())
                else:
                    if item.gettokentype()=="NEWLINE":
                        final.append(["NEWLINE",""])
                    final.append([item.gettokentype(),item.getstr()])
                # print(final)
            except:
                erros+=1
                continue
    # except:
    #     print(lexando,"ta ruim")
    #     return None
    return final

def identificar(texto):
    return lexer.lex(texto)
if __name__ =="__main__":
    from sys import argv
    import compiler_pyc
    compiler_pyc.print=print
    with open(argv[-2])as f:
        read=f.read()
    a=lexar(read,True)
    b=compiler_pyc.start(a)
    b.act()
    with open(argv[-1],"w")as f:
        f.write(b.code)