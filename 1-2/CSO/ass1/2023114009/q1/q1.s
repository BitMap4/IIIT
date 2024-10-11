.globl execute # makes the execute function accessible to other files (q1.c in this case)

execute:
    mov (%rdi), %rax # %rdi- the first argument, in this case it has x, which is a pointer to ans; we copy the value pointed by x and store it in %rax
    xor %rsi, %rax # %rsi has the second argument (the current number in the array); we xor the current value with the present value of ans, and it is stored in %rax
    mov %rax, (%rdi) # we store the value result back into the memory location pointed by x
    ret
