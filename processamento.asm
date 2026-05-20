; processamento.asm - Versão otimizada em baixo nível
section .text
global _start

_start:
    mov ecx, 1000    ;
    xor eax, eax     

loop_soma:
    add eax, ecx     
    dec ecx          
    jnz loop_soma    

    ; Neste ponto, a CPU usou apenas 3 instruções por iteração.
    ; Isso reduz drasticamente o consumo de energia por instrução [2].