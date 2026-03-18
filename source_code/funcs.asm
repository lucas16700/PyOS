; ================================================
; Teste completo de Stack no RISC-V RV64
; ================================================
.section .rodata        ; ou .data, tanto faz
msg:
    .string "Hello, World!\n"
msg_len = .-msg
buffer:
    .byte 0,0,0,0
.section .text
.globl _start

_start:
    li   a0, 6          ; primeiro número
    li   a1, 7          ; segundo número
    jal  ra, soma       ; chama soma(6, 7) → deve retornar 42
    
    li   a0, 1           ; a0 = fd = 1 (stdout)
    la   a1, msg         ; a1 = endereço da string
    la   a2, msg_len     ; a2 = comprimento da string (incluindo \n)
    li   a7, 64          ; a7 = número da syscall write
    ecall                ; executa a syscall
    ; Se chegou aqui, o retorno funcionou
    mv   a0, a0         ; resultado final em a0
    li   a7, 93
    ecall               ; sai com código 42 (se tudo ok)

; ================================================
; Função soma(a0, a1) = a0 * a1
; ================================================
soma:
    addi sp, sp, -32     ; aloca 32 bytes (alinhado 16)
    sd   ra, 24(sp)      ; salva ra (endereço de retorno)
    sd   s0, 16(sp)      ; salva s0 (registrador salvo)
    sd   s1, 8(sp)       ; salva s1

    mv   s0, a0          ; salva a0 em s0 (valor 6)
    mv   s1, a1          ; salva a1 em s1 (valor 7)

    jal  ra, multiplica  ; chama função filha

    ld   s1, 8(sp)       ; restaura s1
    ld   s0, 16(sp)      ; restaura s0
    ld   ra, 24(sp)      ; restaura ra
    addi sp, sp, 32      ; libera stack
    ret

; ================================================
; Função multiplica(a0, a1) = a0 * a1
; ================================================
multiplica:
    addi sp, sp, -16     ; aloca 16 bytes
    sd   ra, 8(sp)       ; salva ra

    mul  a0, a0, a1      ; a0 = a0 * a1  (6 * 7 = 42)

    ld   ra, 8(sp)
    addi sp, sp, 16
    ret