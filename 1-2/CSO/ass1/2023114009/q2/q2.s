.globl rot

rot:
    mov (%rdi), %rax # copy the first element (%rdi points to it) of the array in %rax
    sub $1, %rsi # decrement the size variable by 1
    jz end # if the size variable has the value 0 now, jump to the end
    mov $0, %r9 # set the counter to 0

shift:
    mov 8(%rdi, %r9, 8), %rdx # copy the next element of the array in %rdx, using %r9 as a counter
    mov %rdx, (%rdi, %r9, 8) # move it 1 to the left
    inc %r9 # increment the counter
    cmp %r9, %rsi # compare the counter with the size
    jne shift # if they are not equal, jump back to the start of the loop

end:
    mov %rax, (%rdi, %rsi, 8) # copy the first element that we saved earlier to the end of the array
    ret
