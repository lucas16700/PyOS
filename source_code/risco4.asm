; Teste completo com soma e print do número (até 4 dígitos)
.section .text
.globl _start

_start:
    ; Simula input + soma
    li a0, 120          ; número digitado = 120
    li a1, 10
    add a0, a0, a1      ; soma = 130

    ; Prepara ponteiro para o final do buffer (escrevemos de trás pra frente)
    la t0, result_buffer       # t0 = início do buffer
    addi t1, t0, 5             # t1 = final do buffer (5 bytes: 4 dígitos + \n)

    li t2, 10                  # divisor

    ; Loop: extrai dígitos da direita para esquerda
convert_loop:
    beqz a0, convert_done  # se a0 == 0, termina

    remu t3, a0, t2        # t3 = resto (dígito)
    addi t3, t3, 48        # ASCII '0'-'9'
    sb t3, -1(t1)          # escreve no buffer (de trás pra frente)
    addi t1, t1, -1        # move ponteiro para esquerda

    divu a0, a0, t2        # remove dígito (a0 = a0 / 10)
    j convert_loop

convert_done:
    ; Se não escreveu nada (número era 0), coloca '0'
    bne t1, t0, add_newline
    li t3, 48
    sb t3, -1(t1)
    addi t1, t1, -1

add_newline:
    ; Adiciona \n no início do texto
    li t3, 10
    sb t3, -1(t1)
    addi t1, t1, -1

    ; Calcula tamanho: distância do início até o último byte escrito + 1
    sub t4, t0, t1          # t4 = bytes escritos (positivo)
    addi t4, t4, 1          # inclui o último byte

    ; Imprime
    addi a1, t1, 1          # a1 = primeiro caractere (depois do \n)
    mv a2, t4               # tamanho
    li a0, 1                # stdout
    li a7, 64
    ecall

    ; Sai
    li a0, 0
    li a7, 93
    ecall

.section .bss
result_buffer:
    .space 6                # 4 dígitos + \n + reserva