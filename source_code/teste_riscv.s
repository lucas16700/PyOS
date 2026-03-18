	.file	"teste_riscv.c"
	.option nopic
	.attribute arch, "rv64i2p1"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	_start
	.type	_start, @function
_start:
	addi	sp,sp,-32
	sd	ra,24(sp)
	sd	s0,16(sp)
	addi	s0,sp,32
 #APP
# 6 "source_Ccode/teste_riscv.c" 1
	li x0, 100
	mv a5, x0
# 0 "" 2
 #NO_APP
	sd	a5,-24(s0)
	ld	a5,-24(s0)
	andi	a5,a5,0xff
	addiw	a5,a5,48
	andi	a5,a5,0xff
	sb	a5,-25(s0)
	addi	a5,s0,-25
 #APP
# 17 "source_Ccode/teste_riscv.c" 1
	li a7, 64
	li a0, 1
	mv a1, a5
	li a2, 1
	ecall
# 0 "" 2
# 29 "source_Ccode/teste_riscv.c" 1
	li a7, 93
	li a0, 0
	ecall
# 0 "" 2
 #NO_APP
	nop
	ld	ra,24(sp)
	ld	s0,16(sp)
	addi	sp,sp,32
	jr	ra
	.size	_start, .-_start
	.ident	"GCC: (GNU) 15.2.0"
	.section	.note.GNU-stack,"",@progbits
