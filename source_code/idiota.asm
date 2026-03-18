.section .text
.globl _start

_start:
    ; Imprime prompt
    li   a0, 1
    la   a1, prompt
    la   a2, prompt_len
    li   a7, 64
    ecall

    ; Lê 1 byte de stdin
    li   a0, 0
    la   a1, input_buf
    li   a2, 1
    li   a7, 63
    ecall

    ; Carrega o byte lido
    la   a1, input_buf
    lb   a0, 0(a1)          ; a0 = byte lido

    ; Valida se é dígito (48-57)
    li   t0, 48             ; '0'
    li   t1, 57             ; '9'
    blt  a0, t0, erro_input
    bgt  a0, t1, erro_input

    ; Converte ASCII para número
    addi a0, a0, -48        ; a0 = dígito (0-9)

    ; Soma 10
    li   a1, 10
    add  a0, a0, a1         ; a0 = dígito + 10 (10-19)

    ; Calcula dezena e unidade (unsigned)
    li   t1, 10
    divu t0, a0, t1         ; t0 = dezena (1 para 10-19)
    remu t2, a0, t1         ; t2 = unidade (0-9)

    ; Converte para ASCII
    addi t0, t0, 48
    addi t2, t2, 48

    ; Escreve em result_buf
    la   a2, result_buf
    sb   t0, 0(a2)          ; dezena
    sb   t2, 1(a2)          ; unidade

    ; Imprime prefixo "Resultado: "
    li   a0, 1
    la   a1, msg_prefix
    la   a2, msg_prefix_len
    li   a7, 64
    ecall

    ; Imprime os 2 bytes de result_buf
    li   a0, 1
    la   a1, result_buf
    li   a2, 2
    li   a7, 64
    ecall

    ; Imprime newline
    li   a0, 1
    la   a1, newline
    li   a2, 1
    li   a7, 64
    ecall

    ; Sai com 0
    li   a0, 0
    li   a7, 93
    ecall

erro_input:
    ; Imprime mensagem de erro (opcional)
    li   a0, 1
    la   a1, erro_msg
    la   a2, erro_msg_len
    li   a7, 64
    ecall

    li   a0, 1              ; exit code 1 (erro)
    li   a7, 93
    ecall

.section .rodata
prompt:
    .string "Digite um numero (0-9): "
prompt_len = . - prompt

msg_prefix:
    .string "Resultado: "
msg_prefix_len = . - msg_prefix

erro_msg:
    .string "Erro: digite apenas 0-9!\n"
erro_msg_len = . - erro_msg

newline:
    .byte 10

.section .bss
input_buf:
    .space 1
result_buf:
    .space 2