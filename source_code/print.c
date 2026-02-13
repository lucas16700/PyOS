void _start() {
    int a = 19;
    int b = 23;
    int resultado = a + b;  // 42

    // Sai com código de retorno 42 (seu emulador pode mostrar isso no final)
    asm volatile (
        "mv a0, %0\n"
        "li a7, 93\n"     // syscall exit
        "ecall"
        :
        : "r"(resultado)
        : "a0", "a7"
    );
}