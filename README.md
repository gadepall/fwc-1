# fwc-1

#1.  Install fdroid apk from

https://www.f-droid.org/

#Open fdroid on your mobile and install termux-terminal app from it


#2. ------------------Install Termux----------------------------

#Give termux access to your  user directory in android

termux-setup-storage

#Upgrade packages

apt update && apt upgrade

#Mandatory packages

apt install build-essential openssh

apt install curl git wget subversion 

apt install silversearcher-ag imagemagick proot proot-distro python  bsdtar mutt nmap neovim
#------------------End Install Termux----------------------------

#3. ------------------ Installing ubuntu on termux----------------------------
#Install ubuntu

proot-distro install debian

proot-distro login debian

apt update && apt upgrade

apt install apt-utils build-essential cmake neovim

apt install git  wget  subversion imagemagick  nano  ranger 
#------------------End Installing ubuntu on termux----------------------------

#4. ------------------ Installing python3 on termuxubuntu----------------------------
apt install python3-pip python3-numpy python3-scipy python3-matplotlib python3-mpmath python3-sympy python3-cvxopt
#------------------ End installing python3 on termuxubuntu----------------------------

#5.  Installing neovim and ranger

https://raw.githubusercontent.com/gadepall/fwc-1/main/installation/neovim.txt

#Neovim and Ranger instructions

https://iith-my.sharepoint.com/:x:/g/personal/gadepall_ee_iith_ac_in/EaI2vt4wm7hMmFyQz1AZXr4BWLd1KSZX290xKXfqk-qcgQ?e=KOoUTH

#6.  LaTeX Report for Arduino IDE

sudo apt install texlive-full gnumeric

cd /sdcard/Downloads/

wget https://raw.githubusercontent.com/gadepall/fwc-1/main/files/rncom.sh

bash rncom.sh

#7. Digital Design

#Digital Design Book

https://github.com/gadepall/digital-design/blob/main/main.pdf

git clone https://github.com/gadepall/digital-design

#Spoken Tutorials

#IDE

https://spoken-tutorial.org/watch/Arduino/Seven+Segment+Display/English/

# AVR-Assembly 

https://spoken-tutorial.org/watch/Arduino/Assembly+programming+through+Arduino/English/

#  AVR-GCC

https://spoken-tutorial.org/watch/Arduino/AVR-GCC+programming+through+Arduino/English/


#8.  Matrices  

#Matrix Analysis Book

https://github.com/gadepall/matrix-analysis/blob/main/main.pdf

git clone https://github.com/gadepall/matrix-analysis

#Class 10, Section 5

https://github.com/gadepall/cbse-papers/blob/main/2020/math/10/solutions/main.pdf

svn co https://github.com/gadepall/cbse-papers/trunk/2020/math/10/solutions 10

Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9tzPopYNxV0GEb9cMwr2MJG

https://youtube.com/playlist?list=PLKN4kghPKZ9t37g-oL8l0LAPGMK2bL7B-

#Class 12, Sections 1 and 5

https://github.com/gadepall/cbse-papers/blob/main/2020/math/12/solutions/main.pdf

svn co https://github.com/gadepall/cbse-papers/trunk/2020/math/12/solutions 12

Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9uPnPqucP145qh9l7nGB3pm

#Class 10, Python Coding

Youtube: https://youtube.com/playlist?list=PLKN4kghPKZ9t37g-oL8l0LAPGMK2bL7B-

#Textbook

https://github.com/gadepall/matrix-analysis

9.  C Programming

#Textbook

https://github.com/gadepall/programming/blob/main/main.pdf

#Repository

git clone https://github.com/gadepall/programming

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
--------------------------------------------------------------------------END of Module 1--------------------------------

#Installing wsl for windows users

https://ubuntu.com/wsl

#Access usb over wsl

https://docs.microsoft.com/en-us/windows/wsl/connect-usb
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

