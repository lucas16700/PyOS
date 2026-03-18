#include <fcntl.h>
#include <unistd.h>

void _start() {
    char buffer[100];
    
    // 1. Abrir (Retorna FD em a0)
    int fd = open("teste.txt", O_RDONLY);
    
    // 2. Ler (Usa o FD de a0)
    if (fd >= 0) {
        read(fd, buffer, 100);
        
        // 3. Fechar
        close(fd);
    }

    // Loop infinito para o seu emulador não dar segfault no fim
    while(1);
}
