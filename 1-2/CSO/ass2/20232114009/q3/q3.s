.globl calculate

calculate: # %rdi : n, %rsi : expr
    mov $0, %r8                     # i = 0
    .L1:
        cmp %r8, %rdi               # if (i < n)
        je .end                     # end
        mov (%rsi, %r8, 8), %r9     # %r9 : expr[i]

        cmp $'+', %r9
        je .addition
        cmp $'-', %r9
        je .subtraction
        cmp $'*', %r9
        je .multiplication
        cmp $'/', %r9
        je .division

        push %r9
        jmp .iter

    .iter:
        add $1, %r8
        jmp .L1

    .addition:
        pop %r10
        pop %r11
        add %r10, %r11
        push %r11
        jmp .iter

    .subtraction:
        pop %r10
        pop %r11
        sub %r10, %r11
        push %r11
        jmp .iter

    .multiplication:
        pop %r10
        pop %r11
        imul %r10, %r11
        push %r11
        jmp .iter
    
    .division:
        pop %r10
        pop %rax
        cqo                         # sign extend %rax to %rdx:%rax
        idiv %r10
        push %rax
        jmp .iter

.end:
    pop %rax
    ret
