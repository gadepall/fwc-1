# fwc-1

#Installing wsl for windows users

https://ubuntu.com/wsl

#Access usb over wsl

https://docs.microsoft.com/en-us/windows/wsl/connect-usb

#Base packages

sudo apt update && apt upgrade

sudo apt install build-essential openssh

sudo apt install curl git wget subversion python3  

#1.  Installing neovim and ranger

https://github.com/gadepall/termux/blob/main/neovim/neovim.txt

#Neovim and Ranger instructions

https://docs.google.com/spreadsheets/d/1Yx2RJ2wzbmdDdHaq0Kko0K7FPrdS0m7DWsyzDD_38WA/edit?usp=drivesdk


#2.  Install Platformio 

Section 2 in

https://github.com/gadepall/fwc-1/blob/main/installation/main.pdf

#3.  Arduino IDE

https://github.com/gadepall/fwc-1/tree/main/ide


#4.  LaTeX Report for Arduino IDE

sudo apt install texlive-full gnumeric

cd /sdcard/Downloads/

wget https://raw.githubusercontent.com/gadepall/fwc-1/main/files/rncom.sh

bash rncom.sh

#5. SSH to Termux (Skip this if you are using a bluetooth keyboard)

#Follow instructions in Section 1 of 

https://github.com/gadepall/fwc-1/blob/main/installation/main.pdf

#On termux on your phone

#Enter a simple password

passwd

#This will give you your username

whoami

#Find your ip address

ifconfig 

#Start ssh server on your mobile 

sshd

#On your laptop

ssh username@ipaddress -p8022

#Enter the password and you are connected to termux through your laptop

#------------------End Connecting to termux through ssh----------------------------


#6.  Arduino on Android Phone

https://github.com/gadepall/fwc-1/blob/main/installation/main.pdf

#7.  AVR-Assembly 

svn co https://github.com/gadepall/fwc-1/trunk/assembly

#8.  AVR-GCC

svn co https://github.com/gadepall/fwc-1/trunk/avr-gcc

#9.  Matrices and Optimization Manual

#Installing Python

sudo apt install python3-pip python3-numpy python3-scipy python3-matplotlib python3-mpmath python3-sympy python3-cvxopt

sudo pip3 install cvxpy

#Class 10, Section 5

https://github.com/gadepall/cbse-papers/blob/main/2020/math/10/solutions/main.pdf

svn co https://github.com/gadepall/cbse-papers/trunk/2020/math/10/solutions 10

Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9tzPopYNxV0GEb9cMwr2MJG

#Class 12, Sections 1 and 5

https://github.com/gadepall/cbse-papers/blob/main/2020/math/12/solutions/main.pdf

svn co https://github.com/gadepall/cbse-papers/trunk/2020/math/12/solutions 12

Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9uPnPqucP145qh9l7nGB3pm

#Class 10, Coding
Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9t37g-oL8l0LAPGMK2bL7B-

10.  ARM-GCC

#Setup

https://github.com/gadepall/vaman/blob/master/arm/setup/main.pdf

#Repository

svn co https://github.com/gadepall/vaman/trunk/arm

11.  FPGA

#Setup

https://github.com/gadepall/vaman/blob/master/fpga/setup/main.pdf

#Repository

svn co https://github.com/gadepall/vaman/trunk/fpga

