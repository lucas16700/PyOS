typedef struct {
    long long x;
    long long y;
    long long z;
    long long w;
} Quadro;

Quadro soma_quadro(Quadro a, Quadro b) {
    Quadro r;
    r.x = a.x + b.x;
    r.y = a.y + b.y;
    r.z = a.z + b.z;
    r.w = a.w + b.w;
    return r;
}

int main(void) {
    Quadro p = {1,2,3,4};
    Quadro q = {10,20,30,40};
    Quadro res = soma_quadro(p, q);
    return res.x + res.y;   // só para evitar otimização total
}