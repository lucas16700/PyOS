	.file	"abrir.c"
	.option nopic
	.attribute arch, "rv64i2p1"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.section	.rodata
	.align	3
.LC0:
	.string	"teste.txt"
	.text
	.align	2
	.globl	_start
	.type	_start, @function
_start:
	addi	sp,sp,-1072
	sd	ra,1064(sp)
	sd	s0,1056(sp)
	addi	s0,sp,1072
	lui	a5,%hi(.LC0)
	addi	a5,a5,%lo(.LC0)
	sd	a5,-24(s0)
	ld	a5,-24(s0)
 #APP
# 13 "source_code/abrir.c" 1
	la a1, a5
li a2, 0
li a3, 0
li a7, 56
ecall
mv a5, a0

# 0 "" 2
 #NO_APP
	sd	a5,-32(s0)
	ld	a5,-32(s0)
	bge	a5,zero,.L2
 #APP
# 27 "source_code/abrir.c" 1
	li a0, 1; li a7, 93; ecall
# 0 "" 2
 #NO_APP
.L2:
	ld	a5,-32(s0)
	addi	a4,s0,-1064
 #APP
# 33 "source_code/abrir.c" 1
	mv a0, a5
la a1, a4
li a2, 1024
li a7, 63
ecall
mv a5, a0

# 0 "" 2
 #NO_APP
	sd	a5,-40(s0)
	ld	a5,-40(s0)
	ble	a5,zero,.L3
	ld	a5,-40(s0)
	addi	a4,s0,-1064
 #APP
# 47 "source_code/abrir.c" 1
	li a0, 1
la a1, a4
mv a2, a5
li a7, 64
ecall
# 0 "" 2
 #NO_APP
.L3:
	ld	a5,-40(s0)
	bgt	a5,zero,.L2
	ld	a5,-32(s0)
 #APP
# 61 "source_code/abrir.c" 1
	mv a0, a5
li a7, 57
ecall
# 0 "" 2
# 71 "source_code/abrir.c" 1
	li a0, 0; li a7, 93; ecall
# 0 "" 2
 #NO_APP
	nop
	ld	ra,1064(sp)
	ld	s0,1056(sp)
	addi	sp,sp,1072
	jr	ra
	.size	_start, .-_start
	.ident	"GCC: (GNU) 15.2.0"
	.section	.note.GNU-stack,"",@progbits
