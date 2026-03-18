	.file	"media.c"
	.option nopic
	.attribute arch, "rv64i2p1"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	media_mista
	.type	media_mista, @function
media_mista:
	addi	sp,sp,-64
	sd	ra,56(sp)
	sd	s0,48(sp)
	addi	s0,sp,64
	sd	a1,-32(s0)
	sd	a3,-40(s0)
	sd	a5,-56(s0)
	mv	a5,a0
	sw	a5,-20(s0)
	mv	a5,a2
	sw	a5,-24(s0)
	mv	a5,a4
	sw	a5,-44(s0)
	lw	a5,-20(s0)
	mv	a4,a5
	lw	a5,-24(s0)
	addw	a5,a4,a5
	sext.w	a5,a5
	lw	a4,-44(s0)
	addw	a5,a4,a5
	sext.w	a5,a5
	mv	a0,a5
	call	__floatsidf
	mv	a5,a0
	ld	a1,-32(s0)
	mv	a0,a5
	call	__adddf3
	mv	a5,a0
	ld	a1,-40(s0)
	mv	a0,a5
	call	__adddf3
	mv	a5,a0
	ld	a1,-56(s0)
	mv	a0,a5
	call	__adddf3
	mv	a5,a0
	mv	a4,a5
	lui	a5,%hi(.LC0)
	ld	a1,%lo(.LC0)(a5)
	mv	a0,a4
	call	__divdf3
	mv	a5,a0
	mv	a0,a5
	ld	ra,56(sp)
	ld	s0,48(sp)
	addi	sp,sp,64
	jr	ra
	.size	media_mista, .-media_mista
	.align	2
	.globl	main
	.type	main, @function
main:
	addi	sp,sp,-16
	sd	ra,8(sp)
	sd	s0,0(sp)
	addi	s0,sp,16
	lui	a5,%hi(.LC1)
	ld	a4,%lo(.LC1)(a5)
	lui	a5,%hi(.LC2)
	ld	a3,%lo(.LC2)(a5)
	lui	a5,%hi(.LC3)
	ld	a1,%lo(.LC3)(a5)
	mv	a5,a4
	li	a4,30
	li	a2,20
	li	a0,10
	call	media_mista
	mv	a5,a0
	mv	a0,a5
	call	__fixdfsi
	mv	a5,a0
	sext.w	a5,a5
	mv	a0,a5
	ld	ra,8(sp)
	ld	s0,0(sp)
	addi	sp,sp,16
	jr	ra
	.size	main, .-main
	.section	.rodata
	.align	3
.LC0:
	.word	0
	.word	1074266112
	.align	3
.LC1:
	.word	0
	.word	1074528256
	.align	3
.LC2:
	.word	0
	.word	1074003968
	.align	3
.LC3:
	.word	0
	.word	1073217536
	.globl	__fixdfsi
	.globl	__divdf3
	.globl	__adddf3
	.globl	__floatsidf
	.ident	"GCC: (GNU) 15.2.0"
	.section	.note.GNU-stack,"",@progbits
