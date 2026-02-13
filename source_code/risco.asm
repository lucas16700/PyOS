; Hello World simples em RISC-V RV64
; Usa syscall write (64) e exit (93)

.section .text
.globl _start

_start:
    ; write(1, msg, 14)  ; stdout, mensagem, tamanho
    li   a0, 1           ; a0 = fd = 1 (stdout)
    la   a1, msg         ; a1 = endereço da string
    li   a2, 14          ; a2 = comprimento da string (incluindo \n)
    li   a7, 64          ; a7 = número da syscall write
    ecall                ; executa a syscall

    ; exit(0)
    li   a0, 0           ; a0 = código de saída = 0
    li   a7, 93          ; a7 = número da syscall exit
    ecall                ; sai do programa

.section .rodata        ; ou .data, tanto faz
msg:
    .string "Hello, World!\n"