## features of an os
- create a process
- destroy a process
- wait
- suspend (pause a process, like when debugging) (and un-suspending)
- status (task manager, top etc)

os gives us an api so user programs can interact with the os- system calls

---
#### 2 modes of execution
user mode, kernel mode

---
## posix
portable operating systems interface
- standard set of syscalls
- most modern systems are posix compliant (not windows lmao)
![[Pasted image 20240826031434.png]]
---
#### `wait()`
blocks parent until child terminates
	options like `waitpid()` exist

without wait, if child terminates, child becomes a zombie process, and exit status is not collected by the parent because it continues executing its own stuff. so child's resources stay in the memory.
`wait` allows os to reclaim resources of the child before continuing executing its own stuff
for eg- the parent sleeps for 10 seconds so the child's exit status is never read and its entry remains in the process table.

if parent terminates before child, `init` (pid 1) adopts the orphan and reaps it

---
#### `fork()`
with `fork`, parent and child execute the same code

with `exec`, child can run a different program (pid remains the same)
![[Pasted image 20240826032637.png]]
`exec` and `fork` are used together-
`exec` replaces the image of the process with a new one, so we first `fork` the main process, then we `exec` in the child process, so after child terminates, control is returned to the parent (main process)

eg- `wc process_sample3.c > output.txt`
- shell forks a child
- rewires standard output to `output.txt`
- calls `exec` on the child (`wc process_sample3.c)

---
