.globl execute

execute: # %rdi : n, %rsi : expr
    mov $0, %r8                     # i = 0
    mov $0, %r12                    # number of scores in stack
    .L1:
        cmp %r8, %rdi               # if (i < n)
        je .end                     # end
        mov (%rsi, %r8, 8), %r9     # %r9 : expr[i]

        cmp $'+', %r9
        je .addition
        cmp $'D', %r9
        je .double
        cmp $'C', %r9
        je .invalidate

        push %r9
        add $1, %r12
        jmp .iter

    .iter:
        add $1, %r8
        jmp .L1

    .addition:
        pop %r10
        pop %r11
        add %r10, %r11
        push %r11
        sub $1, %r12
        jmp .iter

    .double:
        pop %r10
        add %r10, %r10
        push %r10
        jmp .iter

    .invalidate:
        pop %r10
        sub $1, %r12
        jmp .iter

.end:
    # sum of scores in stack
    mov $0, %rax
    .L2:
        cmp $0, %r12
        je .return
        pop %r9
        add %r9, %rax
        sub $1, %r12
        jmp .L2
    .return:
        ret
