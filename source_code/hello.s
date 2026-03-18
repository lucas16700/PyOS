	.file	"hello.c"
	.option nopic
	.attribute arch, "rv64i2p1"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.globl	mensagem
	.section	.rodata
	.align	3
	.type	mensagem, @object
	.size	mensagem, 18
mensagem:
	.string	"Teste de Emulador"
	.globl	tamanho_msg
	.section	.srodata,"a"
	.align	3
	.type	tamanho_msg, @object
	.size	tamanho_msg, 8
tamanho_msg:
	.dword	18
	.globl	ponteiro_offset
	.section	.sdata,"aw"
	.align	3
	.type	ponteiro_offset, @object
	.size	ponteiro_offset, 8
ponteiro_offset:
	.dword	mensagem+5
	.globl	buffer_global
	.bss
	.align	3
	.type	buffer_global, @object
	.size	buffer_global, 1024
buffer_global:
	.zero	1024
	.globl	final_buffer
	.section	.srodata
	.align	3
	.type	final_buffer, @object
	.size	final_buffer, 8
final_buffer:
	.dword	buffer_global+1024
	.text
	.align	2
	.globl	_start
	.type	_start, @function
_start:
	addi	sp,sp,-32
	sd	ra,24(sp)
	sd	s0,16(sp)
	addi	s0,sp,32
	lui	a5,%hi(ponteiro_offset)
	ld	a5,%lo(ponteiro_offset)(a5)
	lbu	a5,0(a5)
	sb	a5,-17(s0)
	li	a5,18
	sd	a5,-32(s0)
	ld	a5,-32(s0)
	beq	a5,zero,.L2
	li	a5,84
	sb	a5,-17(s0)
.L2:
	j	.L2
	.size	_start, .-_start
	.ident	"GCC: (GNU) 15.2.0"
	.section	.note.GNU-stack,"",@progbits
