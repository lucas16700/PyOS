import os
from sys import argv
linha=f'''riscv64-elf-gcc -march=rv64i -mabi=lp64 -S -O0 -I./include  -o source_code/{argv[-1]}.s source_Ccode/{argv[-1]}.c'''
os.system(linha)