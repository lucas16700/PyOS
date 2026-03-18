from rply import LexerGenerator
from rich import print
lg = LexerGenerator()
# Tokens principais para MNEMONIC
mnemonic_patterns = r'(?i)(' + '|'.join([
    # RV64I Base (essenciais)
    'lui', 'auipc', 'addi', 'addiw', 'slti', 'sltiu', 'xori', 'ori', 'andi',
    'slli', 'srli', 'srai', 'slliw', 'srliw', 'sraiw',
    'add', 'sub', 'sll', 'slt', 'sltu', 'xor', 'srl', 'sra', 'or', 'and',
    'addw', 'subw', 'sllw', 'srlw', 'sraw',
    'lb', 'lbu', 'lh', 'lhu', 'lw', 'ld', 'lwu',
    'sb', 'sh', 'sw', 'sd',
    'beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu',
    'jal', 'jalr',
    'ecall', 'ebreak',

    # Pseudoinstruções comuns (tratadas como mnemônicos)
    'li', 'la', 'mv', 'not', 'neg', 'negw', 'sext.w', 'seqz', 'snez', 'sltz', 'sgtz',
    'beqz', 'bnez', 'blez', 'bgez', 'bltz', 'bgtz', 'bgt', 'ble', 'bgtu', 'bleu',
    'j', 'jr', 'ret', 'nop',

    # Extensão M (Multiplicação/Divisão) - muito usada em libc
    'mul', 'mulh', 'mulhsu', 'mulhu', 'div', 'divu', 'rem', 'remu',
    'mulw', 'divw', 'divuw', 'remw', 'remuw',

    # Extensão A (Atômicos) - usada em pthread/musl
    'lr.w', 'sc.w', 'amoswap.w', 'amoadd.w', 'amoxor.w', 'amoand.w', 'amoor.w',
    'amomin.w', 'amomax.w', 'amominu.w', 'amomaxu.w',
    'lr.d', 'sc.d', 'amoswap.d', 'amoadd.d', 'amoxor.d', 'amoand.d', 'amoor.d',
    'amomin.d', 'amomax.d', 'amominu.d', 'amomaxu.d',

    # Extensão C (Compressed) - se você quiser suportar no futuro
    'c.li', 'c.addi', 'c.addi16sp', 'c.addi4spn', 'c.lui', 'c.mv', 'c.add',
    'c.nop', 'c.sub', 'c.xor', 'c.or', 'c.and', 'c.slli', 'c.srli', 'c.srai',
    'c.lw', 'c.ld', 'c.sw', 'c.sd', 'c.beqz', 'c.bnez', 'c.j', 'c.jr', 'c.jalr',
    'c.ret', 'c.ebreak'
]) + r')\b'
print(mnemonic_patterns)
lg.ignore(r"[ \t]+")
lg.ignore(r';.*')       # ; até o fim da linha
lg.ignore(r'#.*')       # # até o fim da linha
lg.add('LINE',r"\n+")
lg.add("LINEB",r'\\')
lg.add('STRING', r'"([^"\\]|\\.)*"')
lg.add('IMMEDIATE', r'-?0x[0-9a-fA-F]+|-?\d+')

lg.add('REGISTER', r'(zero|ra|sp|gp|tp|[ast][0-9]+|s[0-9]+|x[0-9]+)')
lg.add('SYMMOD',r'%(hi|lo)')
lg.add('LABEL', r'[a-zA-Z_][a-zA-Z0-9_]*:')
lg.add('SECTION',r'\.(data|rodata|bss|sdata|srodata|sbss|text)')
lg.add('DIRECTIVE', 
r'\.(section|string|zero|space|align|byte|half|word|dword|globl|type|size|ident|file|asciz|ascii|quad|long|short|comm|weak|attribute|option)')
lg.add('MOD',r'@(object|function|progbits)')
lg.add("DYNATT",r'=')
lg.add('COMMA', r',')
lg.add('COLON', r':')
lg.add('LPAREN', r'\(')
lg.add('RPAREN', r'\)')
lg.add('CURRENT_POS', r'\.')
lg.add('MATH',r'[+\-*/]')
lg.add('MNEMONIC', mnemonic_patterns)
lg.add('SYMBOL', r'[a-zA-Z_][a-zA-Z0-9_]*')
# lg.add('DATAPOS',   r'\.')
[
    ['DIRECTIVE', '.section'],
    ['SECTION', '.text'],
    ['DIRECTIVE', '.globl'],
    ['SYMBOL', '_start'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'msgxx'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['IMMEDIATE', '23'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '64'],
    ['MNEMONIC', 'ecall'],
    ['LABEL', '_start:'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'input_buf'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '0'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '63'],
    ['MNEMONIC', 'ecall'],
    ['DIRECTIVE', '.section'],
    ['SECTION', '.data'],
    ['LABEL', 'msgxx:'],
    ['DIRECTIVE', '.string'],
    ['STRING', '"mimime um numero (0-9):"'],
    ['LABEL', 'input_buf:'],
    ['DIRECTIVE', '.byte'],
    ['IMMEDIATE', '0'],
    ['COMMA', ','],
    ['IMMEDIATE', '0'],
    ['LABEL', 'result_buf:'],
    ['DIRECTIVE', '.byte'],
    ['IMMEDIATE', '0'],
    ['DIRECTIVE', '.byte'],
    ['IMMEDIATE', '0'],
    ['DIRECTIVE', '.section'],
    ['SECTION', '.text'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'input_buf'],
    ['MNEMONIC', 'lb'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '0'],
    ['LPAREN', '('],
    ['REGISTER', 'a1'],
    ['RPAREN', ')'],
    ['MNEMONIC', 'addi'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '-48'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['IMMEDIATE', '15'],
    ['MNEMONIC', 'add'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['REGISTER', 'a1'],
    ['MNEMONIC', 'div'],
    ['REGISTER', 't0'],
    ['COMMA', ','],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '10'],
    ['MNEMONIC', 'mul'],
    ['REGISTER', 't2'],
    ['COMMA', ','],
    ['REGISTER', 't0'],
    ['COMMA', ','],
    ['IMMEDIATE', '10'],
    ['MNEMONIC', 'sub'],
    ['REGISTER', 't1'],
    ['COMMA', ','],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['REGISTER', 't2'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['SYMBOL', 'result_buf'],
    ['MNEMONIC', 'addi'],
    ['REGISTER', 't0'],
    ['COMMA', ','],
    ['REGISTER', 't0'],
    ['COMMA', ','],
    ['IMMEDIATE', '48'],
    ['MNEMONIC', 'addi'],
    ['REGISTER', 't1'],
    ['COMMA', ','],
    ['REGISTER', 't1'],
    ['COMMA', ','],
    ['IMMEDIATE', '48'],
    ['MNEMONIC', 'sb'],
    ['REGISTER', 't0'],
    ['COMMA', ','],
    ['IMMEDIATE', '0'],
    ['LPAREN', '('],
    ['REGISTER', 'a2'],
    ['RPAREN', ')'],
    ['MNEMONIC', 'sb'],
    ['REGISTER', 't1'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['LPAREN', '('],
    ['REGISTER', 'a2'],
    ['RPAREN', ')'],
    ['DIRECTIVE', '.section'],
    ['SECTION', '.rodata'],
    ['LABEL', 'msg_prefix:'],
    ['DIRECTIVE', '.string'],
    ['STRING', '"Resultado: "'],
    ['DIRECTIVE', '.section'],
    ['SECTION', '.text'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'msg_prefix'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['IMMEDIATE', '11'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '64'],
    ['MNEMONIC', 'ecall'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'result_buf'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['IMMEDIATE', '2'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '64'],
    ['MNEMONIC', 'ecall'],
    ['MNEMONIC', 'la'],
    ['REGISTER', 'a1'],
    ['COMMA', ','],
    ['SYMBOL', 'newline'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a2'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '1'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '64'],
    ['MNEMONIC', 'ecall'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a0'],
    ['COMMA', ','],
    ['IMMEDIATE', '0'],
    ['MNEMONIC', 'li'],
    ['REGISTER', 'a7'],
    ['COMMA', ','],
    ['IMMEDIATE', '93'],
    ['MNEMONIC', 'ecall'],
    ['DIRECTIVE', '.section'],
    ['SECTION', '.data'],
    ['LABEL', 'output_byte:'],
    ['DIRECTIVE', '.byte'],
    ['IMMEDIATE', '0'],
    ['LABEL', 'newline:'],
    ['DIRECTIVE', '.byte'],
    ['IMMEDIATE', '10']
]
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
