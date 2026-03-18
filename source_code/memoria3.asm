; Teste simples de mmap anônimo (aloca 32 bytes, escreve, lê e imprime)

.section .text
.globl _start

_start:
    ; mmap(0, 32, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0)
    li a0, 0                # addr_hint = 0 (kernel escolhe)
    li a1, 32               # length = 32 bytes
    li a2, 3                # prot = READ (1) + WRITE (2)
    li a3, 34               # flags = PRIVATE (2) + ANONYMOUS (32)
    li a4, -1               # fd = -1 (anônimo)
    li a5, 0                # offset = 0
    li a7, 221              # syscall mmap
    ecall

    bltz a0, error          ; se <0, erro

    mv s0, a0               ; s0 = endereço retornado

    ; Escreve "Mmap OK!" no endereço alocado
    la t0, test_str
    mv t1, s0
    li t2, 9

copy_mmap:
    lb t3, 0(t0)
    sb t3, 0(t1)
    addi t0, t0, 1
    addi t1, t1, 1
    addi t2, t2, -1
    bnez t2, copy_mmap

    ; Imprime
    mv a1, s0
    li a2, 9
    li a0, 1
    li a7, 64
    ecall

    ; Sai
    li a0, 0
    li a7, 93
    ecall

error:
    li a0, 1
    li a7, 93
    ecall

.section .rodata
test_str:
    .string "Mmap OK!\n"