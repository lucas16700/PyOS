.section .text
.globl _start

_start:
    # Print prompt
    li   a0, 1          # stdout
    la   a1, prompt
    li   a2, 23
    li   a7, 64
    ecall

    # Read 1 byte from stdin
    li   a0, 0          # stdin
    la   a1, input_buf
    li   a2, 1
    li   a7, 63
    ecall

    # Converter ASCII → int, somar 10
    lb   a0, 0(a1)      # carrega o byte lido ('0'-'9')
    addi a0, a0, -48    # → número 0-9
    addi a0, a0, 10     # soma 10 → 10-19

    # Converter resultado para ASCII (simples para <20)
    li   t0, 10
    divu t1, a0, t0     # t1 = dezena (1)
    remu t2, a0, t0     # t2 = unidade (0-9)

    addi t1, t1, 48     # '0' + dezena → '1'
    addi t2, t2, 48     # '0' + unidade → '0'-'9'

    # Escreve no buffer de output
    sb   t1, 0(result_buf)     # primeiro dígito
    sb   t2, 1(result_buf)   # segundo dígito

    # Print "Resultado: "
    li   a0, 1
    la   a1, prefix
    li   a2, 11
    li   a7, 64
    ecall

    # Print o número (2 bytes)
    li   a0, 1
    la   a1, result_buf
    li   a2, 2
    li   a7, 64
    ecall

    # Print newline
    li   a0, 1
    la   a1, newline
    li   a2, 1
    li   a7, 64
    ecall

    # Exit
    li   a0, 0
    li   a7, 93
    ecall

.section .rodata
prompt:     .string "Digite um numero (0-9):"
prompt_len = . - prompt


prefix:     .string "Resultado: "
prefix_len = . - prefix

newline:    .byte 10

.section .data
input_buf:  .byte 0
result_buf: .byte 0, 0          # espaço para dois dígitos