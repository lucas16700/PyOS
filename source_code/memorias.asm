; Teste completo de mmap + mprotect + munmap
; Aloca 4096 bytes, escreve, muda proteção, tenta escrever (falha), restaura, escreve novamente, desmapeia

.section .text
.globl _start

_start:
    ; -------------------------------------------------
    ; 1. mmap anônimo de 4096 bytes (1 página)
    li   a0, 0                  ; addr_hint = 0 (kernel escolhe)
    li   a1, 4096               ; length = 4096 bytes
    li   a2, 3                  ; prot = PROT_READ (1) | PROT_WRITE (2)
    li   a3, 34                 ; flags = MAP_PRIVATE (2) | MAP_ANONYMOUS (32)
    li   a4, -1                 ; fd = -1 (anônimo)
    li   a5, 0                  ; offset = 0
    li   a7, 221                ; syscall mmap
    ecall

    bltz a0, mmap_error         ; se < 0 → erro
    mv   s0, a0                 ; s0 = endereço retornado pelo mmap

    ; -------------------------------------------------
    ; 2. Escreve string de teste na região alocada
    la   t0, test_str1          ; t0 = endereço da string "Mmap OK!\n"
    mv   t1, s0                 ; t1 = ponteiro na memória mapeada
    li   t2, 9                  ; tamanho da string + \0

copy_str1:
    lb   t3, 0(t0)
    sb   t3, 0(t1)
    addi t0, t0, 1
    addi t1, t1, 1
    addi t2, t2, -1
    bnez t2, copy_str1

    ; -------------------------------------------------
    ; 3. Imprime a string para confirmar que escrevemos e lemos
    mv   a1, s0
    li   a2, 9
    li   a0, 1
    li   a7, 64                 ; write
    ecall

    ; -------------------------------------------------
    ; 4. Muda proteção para SOMENTE LEITURA (PROT_READ = 1)
    mv   a0, s0
    li   a1, 4096
    li   a2, 1                  ; PROT_READ
    li   a7, 226                ; mprotect
    ecall

    ; -------------------------------------------------
    ; 5. Tenta escrever novamente → deve falhar
    li   t0, 42                 ; valor qualquer
    sb   t0, 0(s0)              ; ← se mprotect estiver correto, deve causar erro/fault

    ; Se chegou aqui, mprotect não funcionou (ou você não simulou o fault)

    ; -------------------------------------------------
    ; 6. Volta proteção para leitura + escrita
    mv   a0, s0
    li   a1, 4096
    li   a2, 3                  ; PROT_READ | PROT_WRITE
    li   a7, 226
    ecall

    ; -------------------------------------------------
    ; 7. Escreve uma segunda string (para confirmar que voltou a funcionar)
    la   t0, test_str2          ; "Write OK!\n"
    mv   t1, s0
    li   t2, 10

copy_str2:
    lb   t3, 0(t0)
    sb   t3, 0(t1)
    addi t0, t0, 1
    addi t1, t1, 1
    addi t2, t2, -1
    bnez t2, copy_str2

    ; Imprime a segunda string
    mv   a1, s0
    li   a2, 10
    li   a0, 1
    li   a7, 64
    ecall

    ; -------------------------------------------------
    ; 8. Desmapeia a região
    mv   a0, s0
    li   a1, 4096
    li   a7, 215                ; munmap
    ecall

    ; -------------------------------------------------
    ; 9. Tenta ler novamente → deve falhar
    lb   t0, 0(s0)              ; ← deve causar erro/fault

    ; Se chegou aqui, munmap não funcionou

    ; Sai normalmente (sucesso total)
    li   a0, 0
    li   a7, 93
    ecall

mmap_error:
    li   a0, 1
    li   a7, 93
    ecall

.section .rodata
test_str1:
    .string "Mmap OK!\n"
test_str2:
    .string "Write OK!\n"