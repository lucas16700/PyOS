; Teste de lbu, lh, lhu
.section .data
test_data:
    .byte 0xFF, 0x80, 0x01, 0x00   ; -1, -128, 1, 0 (para signed)
    .byte 0x7F, 0xFF, 0x80, 0x00   ; 127, -1, -128, 0 (para halfword)

.section .text
.globl _start

_start:
    la   a0, test_data          ; a0 = endereço base

    ; lbu (unsigned byte)
    lbu  t0, 0(a0)              ; t0 = 255 (0xFF sem sinal)
    lbu  t1, 1(a0)              ; t1 = 128 (0x80 sem sinal)

    ; lh (signed halfword)
    lh   t2, 2(a0)              ; t2 = 1 (0x0001 com sinal)
    lh   t3, 4(a0)              ; t3 = 127 (0x007F com sinal)
    lh   t4, 6(a0)              ; t4 = -1 (0xFF80 com sinal → -128 + 127? wait, veja abaixo)

    ; lhu (unsigned halfword)
    lhu  t5, 2(a0)              ; t5 = 1 (0x0001 sem sinal)
    lhu  t6, 6(a0)              ; t6 = 65408 (0xFF80 sem sinal)

    ; Para debug: imprime um byte de teste (ex.: t0 = 255)
    la   a1, result_buffer
    addi t0, t0, 48             ; transforma 255 em ASCII (simples, para teste)
    sb   t0, 0(a1)
    li   a2, 1
    li   a0, 1
    li   a7, 64
    ecall

    ; Sai (pode usar t0 como código de saída para debug)
    mv   a0, t0
    li   a7, 93
    ecall

.section .bss
result_buffer:
    .space 4