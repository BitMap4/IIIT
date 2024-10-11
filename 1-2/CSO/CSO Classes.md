# Class 1
2/1/24 Tuesday
```tikz 
\usepackage{tikz-cd} 
\begin{document} 
\begin{tikzcd}
	Input \ar[r] & Program (Code) \ar[d, Leftrightarrow]  \ar[r] & Output \\
	& Data & 
\end{tikzcd}
\end{document} 
```
- __Input__:
	Processes- Transactions, services
	Sensors- Cameras, Mic, Weather
	Other - Software/hardware systems
- __Processing__:
	Servers, distributed
	Mobiles, small devices
	Real-time, batch, offline
	   $\hookrightarrow$ like a step counter watch- gets a lot of data from accelerometer, thousands of times/sec, decides if step or not, throws away raw data
- __Data__:
	  Files, memory, distributed
- __Output__:
	Screen, speaker

```tikz 
\usepackage{tikz-cd} 
\begin{document} 
\begin{tikzcd}
	CLA \ar[dr]         &                                           & Exit\ Code\\
	stdin \ar[r, thick] & Command \ar[r, thick]\ar[ur]\ar[d, thick] & stdout   \\
			            & stderr                                    &
\end{tikzcd}
\end{document} 
```
- By default, both of these pipes- `stdout` and `stderr` , are connected to the screen.

___
# Class 2


___
# Class 3
9/1/24 Tuesday

## Cache memory
- Disk drive is usually 1000 times larger than main memory but the processor takes 10,000,000 times longer to read a word from disk than from memory.
- Similarly, register stores only a few hundred bytes of info - however processor can read data 100 times faster than from memory.
- So people came up with cache memory.
- As semiconductor tech advances, processor speed keeps increasing and chip sizes keep decreasing.
- Every approx 2y, processor speed doubles.
- So processor-memory gap continues to increase, hence cache memory becomes important.

(long rant about how chip design has advanced so much)

- <Memory hierarchy pyramid\> 
	L0: Registers                                      - CPU registers hold words retrieved from L1 cache
	L1: L1 cache( sram)                           - L1 cache holds cache lines retrieved from L2
	L2: L2 cache (sram)                           - L2 holds lines from L3
	L3: l3 c sram                                      - L3 hols from main memory
	L4: Main memory (dram) - Main memory - holds data blocks retrieved from local disks
	L5: Local secondary storage (local disk)  - Local disks hold files retrieved from remote servers
	L6: Remote sec storg (eg. web servers)
- Cache miss: ?
- L1 will be in all systems. L2 is where it starts getting optional. L3 is present in mroe sophisticated machines.

(missed a lot of stuff)

__Processes__:
- A process is the OS's abstraction for a running program
- Provides the illusion that it is the only process running on the system because other processes cant interfere with the working of this process. Only 1 process runs at a time, and every few micro or nano seconds, the processor keeps switching between processes, so to the user, it looks like all the processes are running at the same time. The processor is a sequential machine. This is achieved via *context switching*.
- State of a process is called *context* (includes values of the PC, register files and contents in the main memory).
- *Context switching*: OS saves context of current process, restores the context of new process and passes control to the new process.
__Threads__:
- ??
__Virtual Memory__:
- provides each process the illusion that it has exclusive use of main memory
- each process has same uniform view of memory called virtual address space.


___
# Class 4
12/1/24
- amdahl's law
### Ch 2 of book started
- 