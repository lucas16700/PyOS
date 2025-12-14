Sistema Operacional Baseado em python
====
Atualmente roda programas escritos em *asm*

atualmente conta com as seguinte instruções:

- mov

### move valores para registradores diversos sem limitações

``` asm
mov "#string diversa" rax
mov b c
mov $10 a 
```

- add, sub, div, mul (operadores __Matematicos__)

fazem as operações logicas principais

``` asm
mov $0 a
add $5 a b
>"b é o resultado"
sub $2 a c
...
```

- AND, NOT, OR e XOR (operadores __Logicos__)

``` asm 
AND $10 $10 a
> "compara os dois valores e retorna em a"
```

- load , store (memoria)

```asm
store $10 a
> "armazena no endereço 10 o valor de a"
load $10 a
> "substitui valor de a por o que estiver no endereço 10" 
```

- set , ret , call , module (modularidade)

vamos supor que foi criadado uma. função simples , hipotenusa do endereço 10 e 11 como catetos:

``` asm
set $5 "#hipotenusa"
load $10 a
load $11 b
mul a a a_quadrado
mul b b b_quadrado
add 
```