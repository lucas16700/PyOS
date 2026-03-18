double media_mista(int a, double x, int b, double y, int c, double z) {
    return (a + b + c + x + y + z) / 3.0;
}

int main(void) {
    return (int)media_mista(10, 1.5, 20, 2.5, 30, 3.5);
}
