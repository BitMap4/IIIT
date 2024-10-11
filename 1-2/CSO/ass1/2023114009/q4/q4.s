.globl sum

sum: # %rdi contains pointer to array and %rsi has length of array
    mov (%rdi), %rax # %rax = lowest element variable
    mov %rax, %rbx # %rbx = largest element variable
    mov $0, %rcx # counter
    cmp $1, %rsi
    jz end # if n == 1, jump to end

loop:
    add $1, %rcx # increment counter
    cmp %rsi, %rcx
    je end # if counter == n, jump to end
    mov (%rdi, %rcx, 8), %rdx # %rdx = next element
    cmp %rdx, %rax
    jg updateLowest # if current < lowest, update lowest element
back:
    cmp %rdx, %rbx
    jl updateLargest # if current > largest, update largest element
    jmp loop

updateLowest:
    mov %rdx, %rax # lowest = current
    jmp back

updateLargest:
    mov %rdx, %rbx # largest = current
    jmp loop

end:
    add %rbx, %rax # sum = lowest + largest
    ret
