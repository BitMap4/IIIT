some key registers:
- program counter
- stack pointer
- program status word- status of the current state of cpu and program (program bits)

## what constitutes a process?
- memory
- instruction pointer, program counter
- stack poiinter
- persistent storage (i/o info)
- unique id (pid)
- memory image (static and dynamic)
  ![[Pasted image 20240826021649.png]]
- cpu context (registers): PC, SP, current operands
- file descriptors

## creating a process by os
- creati9on of program heap
- basic file setup- STDIN, STDOUT, STDERR
- initialise cpu regs
- start program
## state of process
- running
- ready - ready to run
- blocked - not ready to run, something else is running (i/o)
- think of i/o call (?)
![[Pasted image 20240826030152.png]]
example:
![[Pasted image 20240826030255.png]]
## how to store metadata?
- process list
- each element of list is a process control block (pcb)
- each pcb has:
  - pid
  - state
  - address space (regs)
