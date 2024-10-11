.globl binary_s

binary_s:                   # %rdi : elmt, %rsi : result, %rdx : arr
    mov $0, %r8             # l=0
    mov $31, %r9            # r=31
    mov $0, %r10            # no of iterations

    .while:
        mov %r9, %r11
        sub $1, %r11
        # while (l < r-1)
        cmp %r8, %r11
        jle .end_while

        add $1, %r10        # i++

        mov %r8, %rax
        add %r9, %rax
        sar $1, %rax        # m = (l+r)/2

        mov (%rdx, %rax, 8), %rcx
        cmp %rcx, %rdi      # if (arr[m] < elmt)
        jg .if1
        jmp .else1
        .if1:
            mov %rax, %r8  # l = m
            jmp .while
        .else1:
            mov %rax, %r9  # r = m
            jmp .while
        
    .end_while:
        cmp %rdi, (%rdx, %r8, 8)
        je .if2                     # if (arr[l] == elmt)
        add $1, %r8
        cmp %rdi, (%rdx, %r8, 8)
        je .if2                   # elif (arr[l+1] == elmt)
        jmp .else2

        .if2:
            mov %r8, (%rsi)         # result[0] = l or l+1
            jmp .end
        .else2:
            movq $-1, (%rsi)        # else result[0] = -1
            jmp .end

    .end:
        mov %r10, 8(%rsi)           # result[1] = i
        ret