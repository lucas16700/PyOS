riscv64-elf-gcc \                                                                                                              
  -march=rv64i \
  -mabi=lp64 \
  -S \
  -O0 -I./include \
  -o source_code/abrir2.s \
  source_Ccode/nome