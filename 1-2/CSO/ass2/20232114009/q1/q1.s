.global max_subarray

max_subarray:
    mov %rsp, %r9
    mov $2, %r15   
    cmp $1, %rdi
    je .e

    # Preprocessing loop: for each element in the array, add it with the previous element and store it back.
    .ploop:
        mov %r15, %r14 
        dec %r14 
        mov (%rcx, %r15, 8), %r13 
        mov (%rcx, %r14, 8), %r12 
        add %r12, %r13 
        mov %r13, (%rcx, %r15, 8) 
        inc %r15
        cmp %rdi, %r15
        jle .ploop

    .e:
    mov %rsp, %r8  
    mov $0, %rax 

    mov %rsi, %r15 
    # Main loop: for each element in the array, find the maximum subarray that ends at that element.
    .floop:
        .wloop:
            cmp %rsp, %r8
            je .endwl 
            # If the current element is greater than the sum of the current subarray and the current element, start a new subarray.
            mov %r15, %r14 
            sub %rsi, %r14 
            mov (%rcx, %r14, 8), %r13 
            mov (%rsp), %r12 
            cmp %r12, %r13
            jge .endwl
            add $8, %r8
            jmq .wloop
            .endwl:
            mov %r15, %r14 
            sub %rsi, %r14 
            pushq %r14
            # If the current subarray sum is greater than the maximum found so far, update the maximum.
            mov -8(%r8), %r13 
            mov %r15, %r14
            sub %rdx, %r14 
            cmp %r14, %r13 
            jge .endofif
            sub $8, %r8
            .endofif:
                mov (%rcx, %r15, 8), %r14 
                mov -8(%r8), %r13 
                mov (%rcx, %r13, 8), %r12 
                sub %r12, %r14 
                cmp %r14, %rax 
                cmovl %r14, %rax
        .endfp:
            inc %r15
            cmp %rdi, %r15
            jle .floop

    # Restore the stack pointer and return.
    mov %r9, %rsp
    ret