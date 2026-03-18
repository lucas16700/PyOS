# Exemplo de sext.w
rs = 0x00000000FFFFFFFF          # valor que veio de um lw ou operação de 32 bits

# === operação sext.w (exatamente como o RISC-V faz) ===
valor32 = rs & 0xFFFFFFFF
if valor32 & 0x80000000:         # se o bit 31 está ligado (número negativo em 32 bits)
    resultado = valor32 | 0xFFFFFFFF00000000
else:
    resultado = valor32

print(f"Entrada:  0x{rs:016X}")
print(f"sext.w:   0x{resultado:016X}")
# Resultado esperado: 0xFFFFFFFFFFFFFFFF   ← virou -1 correto em 64 bits