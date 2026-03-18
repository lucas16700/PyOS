/* Teste de Aritmética de Seção Data para Emulador RISC-V */

// String estática - Gerará um label e .string/.ascii
const char mensagem[] = "Teste de Emulador";

// O compilador tentará resolver o tamanho em tempo de compilação
// No Assembly, isso pode virar uma constante ou uma subtração de labels
const unsigned long tamanho_msg = sizeof(mensagem);

// Teste de aritmética de ponteiros na seção data
// O valor de 'ponteiro_offset' deve ser o endereço de mensagem + 5
const char *ponteiro_offset = &mensagem[5];

// Buffer para testar brk/mmap
char buffer_global[1024];
const unsigned long final_buffer = (unsigned long)&buffer_global + 1024;

// Função start para evitar erro de linker e testar execução básica
void main() {
    // Acessa os dados para garantir que não sejam otimizados para fora
    volatile char c = *ponteiro_offset;
    volatile unsigned long t = tamanho_msg;
    
    if (t > 0) {
        c = mensagem[0];
    }

    // Loop infinito ou syscall de exit
    while(1);
}
