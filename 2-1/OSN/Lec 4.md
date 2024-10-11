kernel doesnt trust the user stack- it doesnt want to let you jump to random addresses

so it maintains a separate kernel stack

kernel cant rely on  user provided addresses and maintains a table- interrupt secriptor table (idt) (boot time)

idt contains addresses of different kernel functions to run on syscalls or other events

___
## TRAP instruction
- special kind of instruction to switch mode to kernel
- when syscall is made- raise provilege mode, do stuff, returns into the user program with return-from-trap instruction

when trap is executed-
- raise privilege
- switch to kernel stack
- save context on kernel stack
- look up in idt and jump to trap handler function in os code
![[Pasted image 20240826085018.png]]

---
## interrupt and trap
#### interrupt
- signal sent to cpu due to unexpected event from either hardware or software
- i/o interrupt, clock interrupt, console interrupt etc
#### trap
software interrupt caused by syscalls or exceptions (like divide by 0)

___
## LDE protocol

![[Pasted image 20240826085855.png]]
![[Pasted image 20240826085915.png]]

---
# switching processes
## cooperative/non-preemptive approach
- os trusts the processes to behave reasonably (give control back using syscall `yield()`)
- process might misbehave- divide by 0, or accessing restricted memory
  trap to os `->` os will terminate the process
- used in initial versions of macos, old xerox alto system
- infinite loop and process never terminates? reboot lmao
## non-cooperative / preemptive approach
- os has control
- how? use interrupts
- timer interrupt: every x milliseconds, raise an interrupt, hald the process, invoke interrupt handler `->` os gains control
- os starts timer during boot sequence
- during timer interrupt, 2 decisions are possible-
  - continue with current process
  - switch to diff process (os executes context switch)
### context switch
- save a few register values from executing process registers to kernel stack: general purpose regs, PC, kernel stack pointer
- restore values for the next process when return-to-trap
lde protocol:
![[Pasted image 20240826091351.png]]
![[Pasted image 20240826091403.png]]

---
what if an interrupt happens while handling another interrupt?
	disable interrupts during interrupt processing
	sophisticated locking mechanisms to protect concurrent access to internal data structures

---
## policies

> how good is a policy?
	 we have 2 metrics- performance metric (time) and fairness metric

lets start with some assumptions-
- each job runs for the same time
- all jobs arrive at the same time
- all jobs only use the cpu (no i/o)
- the run time of each job is known

### fcfs
how to schedule? lets look at fcfs
lets say all 3 arrived at the same time (w, then t, then s, with negligible time gap)
![[Pasted image 20240826092128.png]]
what if each job no longer runs for the same time?
![[Pasted image 20240826092153.png]]
convoy effect- waiting for a long time in a line when you have a very less amount of work, like waiting in a line in the grocery store when u have 1 item to purchase
### sjf
what if we know the expected time for each process? lets try shortest job first (sjf)
if all 3 arrive at the same time
![[Pasted image 20240826092617.png]]
if w arrives first
![[Pasted image 20240826092636.png]]
### stcf
shortest time to completion
- when new job arrives, check which job completes first![[Pasted image 20240826092749.png]]
