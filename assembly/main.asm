section .data
	hello: db "hello world!", 10	; string to print
	helloLen: equ $-hello			; string length

section .text
	global _start					;entry point for linker

	_start:
		mov	rax,1					;
		mov	rdi,1					;
		mov	rsi,hello				;
		mov rdx,helloLen			;
		syscall						;

		mov rax,60					;
		mov rdi,0					;
		syscall						;
