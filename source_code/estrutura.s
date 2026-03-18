	.file	"estrutura.c"
	.option nopic
	.attribute arch, "rv64i2p1"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	soma_quadro
	.type	soma_quadro, @function
soma_quadro:
	addi	sp,sp,-80
	sd	ra,72(sp)
	sd	s0,64(sp)
	sd	s1,56(sp)
	sd	s2,48(sp)
	addi	s0,sp,80
	sd	a0,-72(s0)
	mv	s2,a1
	mv	s1,a2
	ld	a4,0(s2)
	ld	a5,0(s1)
	add	a5,a4,a5
	sd	a5,-64(s0)
	ld	a4,8(s2)
	ld	a5,8(s1)
	add	a5,a4,a5
	sd	a5,-56(s0)
	ld	a4,16(s2)
	ld	a5,16(s1)
	add	a5,a4,a5
	sd	a5,-48(s0)
	ld	a4,24(s2)
	ld	a5,24(s1)
	add	a5,a4,a5
	sd	a5,-40(s0)
	ld	a5,-72(s0)
	ld	a2,-64(s0)
	ld	a3,-56(s0)
	ld	a4,-48(s0)
	sd	a2,0(a5)
	sd	a3,8(a5)
	sd	a4,16(a5)
	ld	a4,-40(s0)
	sd	a4,24(a5)
	ld	a0,-72(s0)
	ld	ra,72(sp)
	ld	s0,64(sp)
	ld	s1,56(sp)
	ld	s2,48(sp)
	addi	sp,sp,80
	jr	ra
	.size	soma_quadro, .-soma_quadro
	.section	.rodata
	.align	3
.LC0:
	.dword	1
	.dword	2
	.dword	3
	.dword	4
	.align	3
.LC1:
	.dword	10
	.dword	20
	.dword	30
	.dword	40
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	addi	sp,sp,-176
	sd	ra,168(sp)
	sd	s0,160(sp)
	addi	s0,sp,176
	lui	a5,%hi(.LC0)
	addi	a5,a5,%lo(.LC0)
	ld	a2,0(a5)
	ld	a3,8(a5)
	ld	a4,16(a5)
	sd	a2,-48(s0)
	sd	a3,-40(s0)
	sd	a4,-32(s0)
	ld	a5,24(a5)
	sd	a5,-24(s0)
	lui	a5,%hi(.LC1)
	addi	a5,a5,%lo(.LC1)
	ld	a2,0(a5)
	ld	a3,8(a5)
	ld	a4,16(a5)
	sd	a2,-80(s0)
	sd	a3,-72(s0)
	sd	a4,-64(s0)
	ld	a5,24(a5)
	sd	a5,-56(s0)
	addi	a0,s0,-112
	ld	a3,-48(s0)
	ld	a4,-40(s0)
	ld	a5,-32(s0)
	sd	a3,-144(s0)
	sd	a4,-136(s0)
	sd	a5,-128(s0)
	ld	a5,-24(s0)
	sd	a5,-120(s0)
	ld	a3,-80(s0)
	ld	a4,-72(s0)
	ld	a5,-64(s0)
	sd	a3,-176(s0)
	sd	a4,-168(s0)
	sd	a5,-160(s0)
	ld	a5,-56(s0)
	sd	a5,-152(s0)
	addi	a4,s0,-176
	addi	a5,s0,-144
	mv	a2,a4
	mv	a1,a5
	call	soma_quadro
	ld	a5,-112(s0)
	sext.w	a4,a5
	ld	a5,-104(s0)
	sext.w	a5,a5
	addw	a5,a4,a5
	sext.w	a5,a5
	mv	a0,a5
	ld	ra,168(sp)
	ld	s0,160(sp)
	addi	sp,sp,176
	jr	ra
	.size	main, .-main
	.ident	"GCC: (GNU) 15.2.0"
	.section	.note.GNU-stack,"",@progbits
