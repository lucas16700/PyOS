; Teste de heap dinâmico com brk (syscall 214)
; Aloca 16 bytes extras, escreve string no heap, copia de volta e imprime

.section .text
.globl _start

_start:
    ; 1. Pega endereço atual do heap (brk(0))
    li a0, 0
    li a7, 214
    ecall
    mv s0, a0           ; s0 = heap_end atual

    ; 2. Pede mais 16 bytes
    addi a0, s0, 16     ; novo endereço desejado
    li a7, 214
    ecall
    mv s1, a0           ; s1 = novo heap_end

    ; 3. Escreve string "Alocado!" no heap (s0 é o início)
    la t0, source_msg   ; t0 = endereço da string original
    mv t1, s0           ; t1 = ponteiro no heap

    li t2, 9            ; contador (tamanho da string + \0)

copy_to_heap:
    lb t3, 0(t0)        ; lê byte da fonte
    sb t3, 0(t1)        ; escreve no heap
    addi t0, t0, 1
    addi t1, t1, 1
    addi t2, t2, -1
    bnez t2, copy_to_heap

    ; 4. Copia de volta para buffer estático (teste de leitura do heap)
    la t0, s0           ; t0 = início do heap
    la t1, copy_buffer  ; t1 = buffer estático
    li t2, 9

copy_back:
    lb t3, 0(t0)
    sb t3, 0(t1)
    addi t0, t0, 1
    addi t1, t1, 1
    addi t2, t2, -1
    bnez t2, copy_back

    ; 5. Imprime o buffer copiado
    la a1, copy_buffer
    li a2, 9
    li a0, 1
    li a7, 64
    ecall

    ; Sai
    li a0, 0
    li a7, 93
    ecall

.section .rodata
source_msg:
    .string "Alocado!"

.section .bss
copy_buffer:
    .space 10           ; reserva 10 bytes para cópia