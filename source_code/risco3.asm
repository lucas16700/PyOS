; Desafio para testar mistura de .text e .data
; Lê um número do input (syscall read=63), soma 10, imprime resultado via write=64
; Mistura seções para testar resolução de labels e coleta de dados
; Entrada simulada: assume 1 byte (número ASCII '0'-'9')
; Resultado: "Resultado: X\n" onde X = input +10

.section .text
.globl _start

li   a0, 1           ; a0 = fd = 1 (stdout)
la   a1, msgxx         ; a1 = endereço da string
li   a2, 23          ; a2 = comprimento da string (incluindo \n)
li   a7, 64          ; a7 = número da syscall write
ecall                ; executa a syscall
_start:
; Prepara buffer para input (endereço de input_buf)
la a1, input_buf
li a2, 1          ; Lê 1 byte
li a0, 0          ; fd=0 (stdin)
li a7, 63         ; syscall read
ecall

.section .data
msgxx:
    .string "mimime um numero (0-9):"

input_buf: 
    .byte 0, 0 ; Buffer para input (1 byte)
result_buf: 
    .byte 0
    .byte 0

.section .text
; Converte input ASCII para número (ex.: '5' = 53 - 48 = 5)
la a1, input_buf
lb a0, 0(a1)      ; Carrega byte lido
addi a0, a0, -48  ; ASCII '0' = 48, subtrai para número
li a1, 15         ; Soma 10
add a0, a0, a1
div t0, a0, 10
mul t2, t0, 10
sub t1, a0, t2
la a2, result_buf
addi t0, t0, 48
addi t1, t1, 48
sb t0, 0(a2)
sb t1, 1(a2)


.section .rodata
msg_prefix: .string "Resultado: " ; Prefixo da mensagem

.section .text
; Converte número de volta para ASCII e imprime

la a1, msg_prefix ; Endereço do prefixo
li a2, 11         ; Tamanho prefixo
li a0, 1          ; fd=1 (stdout)
li a7, 64         ; write
ecall

la a1, result_buf ; Endereço do prefixo
li a2, 2         ; Tamanho prefixo
li a0, 1          ; fd=1 (stdout)
li a7, 64         ; write
ecall

la a1, newline
li a2, 1
li a0, 1
li a7, 64
ecall

li a0, 0
li a7, 93         ; exit
ecall

.section .data
output_byte: .byte 0 ; Byte temporário para output
newline: .byte 10    ; \n