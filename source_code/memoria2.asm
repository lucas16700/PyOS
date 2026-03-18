; Aloca mais 128 bytes de heap usando brk (syscall 214)
; Supõe que você já tem o heap funcionando e quer estender

.section .text
.globl _start

_start:
    ; 1. Pega o endereço atual do fim do heap (brk(0))
    li   a0, 0          ; argumento 0 = retorna heap_end atual
    li   a7, 214        ; syscall brk
    ecall
    mv   s0, a0         ; s0 = heap_end atual (ex.: 0x...137 bytes)

    ; 2. Calcula novo endereço desejado: heap_end atual + 128
    addi a0, s0, 128    ; a0 = novo heap_end desejado

    ; 3. Chama brk com o novo endereço
    li   a7, 214
    ecall
    ; Após isso, a0 deve conter o novo heap_end (se sucesso)
    ; Se a0 != novo valor desejado → erro (heap não estendido)

    ; 4. Teste: escreve um byte no novo espaço (para confirmar)
    la   t0, test_msg   ; t0 = endereço da string de teste
    mv   t1, s0         ; t1 = início do espaço novo (heap_end antigo)
    lb   t2, 0(t0)      ; t2 = primeiro byte da string (ex.: 'N')
    sb   t2, 0(t1)      ; escreve no início do novo heap

    ; 5. Imprime uma mensagem de sucesso (opcional)
    la   a1, success_msg
    li   a2, 21         ; tamanho da string
    li   a0, 1          ; stdout
    li   a7, 64         ; write
    ecall

    ; Sai
    li   a0, 0
    li   a7, 93         ; exit
    ecall

.section .rodata
test_msg:
    .string "Novo heap OK!\n"
success_msg:
    .string "Alocados +128 bytes!\n"