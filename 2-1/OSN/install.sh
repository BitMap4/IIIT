#! script to install on wsl if compiler throws error for being unable to identify c++ stuff

docker run -it ubuntu:20.04

apt update
apt upgrade

apt install git

git clone https://github.com/riscv-collab/riscv-gnu-toolchain
cd riscv-gnu-toolchain

.github/setup-apt.sh

./configure --prefix=/opt/riscv
make linux 2>&1 | tee build.log

exit