# pycessor: 一个由Python编写的处理器模拟器

## Initialization

首先，在运行程序之前，需要用户对使用的ISA、指令位数、运行模式、trace模式等进行设置。

## 运行程序

因为RISC-V的编译器的结果是ELF文件，因此，运行环境要求为Ubuntu。
用户将写好的C/C++代码进行编译，得到RISC-V汇编代码，即ELF文件。
运行pycessor后，程序将自动读取ELF中的信息并运行模拟器程序，根据用户的需求，可选择trace的模式。