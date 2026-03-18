void _start() {
    // 1. Comportamento crítico: Tentaremos carregar 100 em x0 e depois mover x0 para t0.
    // Se o RISC-V funcionar, t0 será 0, ignorando o 100.
    long resultado;
    
    asm volatile (
        "li x0, 100\n\t"   // Tenta escrever 100 no reg zero (será ignorado)
        "mv %0, x0"        // Move o valor de x0 para a variável 'resultado'
        : "=r" (resultado) // Saída
    );

    // 2. Imprimir o resultado via System Call (Linux RISC-V 64)
    // O valor '0' em ASCII é 48.
    char c = (char)(resultado + 48); 
    
    // Syscall write(1, &c, 1)
    asm volatile (
        "li a7, 64\n\t"    // syscall número 64 (write)
        "li a0, 1\n\t"     // file descriptor 1 (stdout)
        "mv a1, %0\n\t"    // endereço do caractere
        "li a2, 1\n\t"     // tamanho 1 byte
        "ecall"            // chama o kernel
        : 
        : "r" (&c)
        : "a7", "a0", "a1", "a2"
    );

    // 3. Syscall exit(0)
    asm volatile (
        "li a7, 93\n\t"    // syscall número 93 (exit)
        "li a0, 0\n\t"     // status 0
        "ecall"
    );
}
