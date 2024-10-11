.globl prod

prod: # rdi = arr, rsi = n, rdx = new
    mov (%rdi), %rbx # putting first element of array in %rbx; %rbx = product of all elements
    mov $1, %rcx # counter
    mov $0, %r8 # number of 0s in arr
    cmp $0, %rbx
    je zero # if first element is 0, increment number of 0s
    jmp mult

zero:
    add $1, %r8 # increment number of 0s
    add $1, %rcx # increment counter
    jmp mult

mult:
    cmp %rcx, %rsi
    je cont # if counter == n, jump to end
    cmp $0, (%rdi, %rcx, 8)
    je zero # if arr[counter] is 0, jump to zero()
    imul (%rdi, %rcx, 8), %rbx # multiply %rbx with arr[counter]
    add $1, %rcx # increment counter
    jmp mult

cont:
    mov $0, %rcx # counter
    cmp $1, %r8
    jg allZero # if number of 0s > 1, all elements of new[] will be 0
    je allZeroExceptOne # if number of 0s == 1, all elements of new[] will be 0 except the one which is 0
    jmp allDiv

allDiv:
    cmp %rcx, %rsi
    je end # if counter == n, jump to end
    mov %rbx, (%rdx, %rcx, 8) # new[counter] = product
    mov %rbx, %rax # putting product in %rax
    push %rdx # saving %rdx
    cqo # sign-extend %rax to %rdx:%rax
    idivq (%rdi, %rcx, 8) # divide product by arr[counter] (stored in %rdx:%rax)
    pop %rdx # restoring %rdx
    mov %rax, (%rdx, %rcx, 8) # new[counter] = product / arr[counter]
    add $1, %rcx # increment counter
    jmp allDiv

allZero:
    cmp %rcx, %rsi
    je end # if counter == n, jump to end
    mov $0, (%rdx, %rcx, 8) # new[counter] = 0
    add $1, %rcx # increment counter
    jmp allZero

allZeroExceptOne:
    cmp %rcx, %rsi
    je end # if counter == n, jump to end
    cmp $0, (%rdi, %rcx, 8)
    je one # if arr[counter] is 0, insert product in new[]
    mov $0, (%rdx, %rcx, 8) # new[counter] = 0
    add $1, %rcx # increment counter
    jmp allZeroExceptOne

one:
    mov %rbx, (%rdx, %rcx, 8) # new[counter] = product
    add $1, %rcx # increment counter
    jmp allZeroExceptOne

end:
    ret
