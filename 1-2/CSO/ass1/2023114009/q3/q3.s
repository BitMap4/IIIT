.globl check

check: # %rdi has the pointer to string and %rsi has the length of the string
    mov $0, %rcx # counter from the start                                   int i = 0;
    mov %rsi, %rax
    shr $1, %rax # length/2
    sub $1, %rsi # counter fromt he end (n-1)
    jz true # if length is 1, then it is a palindrome                       if (--n == 0) return 1;

loop: #                                                                     while (1) {
    mov (%rdi, %rcx, 8), %r8 # load the character from the start                // str[i]
    mov (%rdi, %rsi, 8), %r9 # load the character from the end                  // str[n-1-i]
    cmp %r8, %r9 #                                                              if (str[i] != str[n-1-i]) return 0; 
    jnz false # if characters are not equal, then it is not a palindrome
    add $1, %rcx #                                                              i++;
    sub $1, %rsi # move the counters
    cmp %rcx, %rax #                                                             if (i == n/2) return 1;
    jz true # end if both counters meet
    jmp loop #                                                              }

true:
    mov $1, %rax
    ret

false:
    mov $0, %rax
    ret

