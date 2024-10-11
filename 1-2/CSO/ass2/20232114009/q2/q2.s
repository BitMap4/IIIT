.globl choose

choose: # %rdi : n, %rsi : r
    mov %rdi, %rax      # d = n                 %rax : d
    sub %rsi, %rax      # d = n-r
    cmp %rsi, %rdi      # if (d < r)
    jl .L1
    .L2:
    cmp $0, %rsi        # if (r == 0)
    je .L3
    mov %rdi, %r9       # ans = n               %r9 : ans
    sub $1, %rdi        # n--
    sub $1, %rsi        # r--
    push %r9            # save ans
    call choose         #                       %rax : C(n-1, r-1)
    pop %r9             # restore ans
    imul %r9, %rax      # ans *= C(n-1, r-1)    %rax : ans
    xor %rdx, %rdx
    add $1, %rsi        # r++
    idiv %rsi           # ans /= r              %rdx:%rax -> %rsi*%rax + %rdx
    ret                 # return ans

.L3:
    mov $1, %rax
    ret                 # return 1

.L1:
    mov %rax, %rsi      # r = d
    jmp .L2
