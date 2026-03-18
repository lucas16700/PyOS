.section .data
test_bytes: .byte 0xFF, 0x80, 0x01, 0x00   # -1, -128, 1, 0 (signed)

.section .text
.globl _start

_start:
    la a0, test_bytes

    lb  t0, 0(a0)     # t0 = -1   (com sinal)
    lbu t1, 0(a0)     # t1 = 255  (sem sinal)
    lh  t2, 2(a0)     # t2 = 1
    lhu t3, 2(a0)     # t3 = 1
    
    # sb 10, 1, 0
    li a7, 64
    li a2, 1
    li a0, 1
    ecall

    # Para debug: sai com t0 + t1 + t2 + t3
    add a0, t0, t1
    add a0, a0, t2
    add a0, a0, t3
    li a7, 93
    ecall