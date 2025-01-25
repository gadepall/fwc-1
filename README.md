This repo is for all modules of the [Certificate Program in Future Wireless Communications](https://fwc.iith.ac.in) (FWC) by Indian Institute of Technology, Hyderabad (IITH).

# fwc-1

## Setup

### Installing Apps

1. Install [F-Droid](https://www.f-droid.org/).
2. Open f-droid on your mobile and install the following apps:
   - Termux
   - Termux:API

### Setting up Termux

1. Give termux access to your user directory in Android.

    ```bash
    termux-setup-storage
    ```

2. Upgrade packages (any **one** command)

    ```bash
    pkg upg
    ```

    ```bash
    apt update && apt upgrade
    ```

3. Install mandatory packages (any **one** command)

    ```bash
    apt install build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

    ```bash
    pkg in build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

### Installing and Setting up Debian on Termux

1. Install debian

    ```bash
    proot-distro install debian
    ```
    ```bash
    proot-distro login debian
    ```

    Inside proot-distro

    ```bash
    apt update && apt upgrade
    ```
    ```bash
    apt install apt-utils build-essential cmake neovim git wget subversion imagemagick nano ranger python3-venv
    ```

2. Installing python3

    ```bash
    apt install python3-pip python3-numpy python3-scipy python3-matplotlib python3-mpmath python3-sympy python3-cvxopt
    ```

3. Installing neovim and ranger

    ```bash
    apt install neovim ranger libxtst-dev libx11-dev python3-pynvim
    ```

    - Refer to this [document](https://raw.githubusercontent.com/gadepall/fwc-1/main/installation/neovim.txt) to setup neovim and ranger.
    - For usage tips refer to this [document](https://iith-my.sharepoint.com/:x:/g/personal/gadepall_ee_iith_ac_in/EaI2vt4wm7hMmFyQz1AZXr4BWLd1KSZX290xKXfqk-qcgQ?e=KOoUTH).

4. Installing LaTeX

   ```bash
   apt install texlive-full gnumeric
   ```

## Latex and Python

### Latex Template

```bash
git clone  https://github.com/gadepall/training/
```
```bash
cd training/math
```
```bash
texfot pdflatex main.tex
```

### Python

```bash
python3 codes/tri_sss.py
```

## Digital Design

### Digital Design Book

The book is present [here](https://github.com/gadepall/digital-design/blob/main/main.pdf).

To obtain the sources:

```bash
git clone https://github.com/gadepall/digital-design
```

### Spoken Tutorials

1. [Seven Segment Display](https://spoken-tutorial.org/watch/Arduino/Seven+Segment+Display/English/)
2. [AVR-Assembly](https://spoken-tutorial.org/watch/Arduino/Assembly+programming+through+Arduino/English/)
3. [AVR-GCC](https://spoken-tutorial.org/watch/Arduino/AVR-GCC+programming+through+Arduino/English/)

### Video Tutorials

The codes used in these videos and relevant references for each video are present at [goats-9/fwc-codes](https://github.com/goats-9/fwc-codes). These have been adapted from [gadepall/digital-design](https://github.com/gadepall/digital-design).

1. [Arduino/PlatformIO](https://www.youtube.com/playlist?list=PLFAML6L4m0jNqTyHS-vdjfL-iLmvrvmX2)
2. [AVR-Assembly](https://www.youtube.com/playlist?list=PLFAML6L4m0jP1pXZbOEx_XRBXMHzHbU-H)
3. [AVR-GCC](https://www.youtube.com/playlist?list=PLFAML6L4m0jNxRPxL8O6QB8A28JAu_eGh)
4. [Vaman-ESP32/PlatformIO](https://www.youtube.com/playlist?list=PLFAML6L4m0jNzB4Hut4SQQFD4axMZrrsc)
5. [Vaman-FPGA](https://www.youtube.com/playlist?list=PLFAML6L4m0jPfbT2symV7FW_E-KGJTldW)
6. [Vaman-ARM](https://www.youtube.com/playlist?list=PLFAML6L4m0jMAHY_B1I1eVhPjCSOE6wIL)

# fwc-2

## Math Computing

### Geometry

#The book is present [here](https://github.com/gadepall/geometry/blob/main/main.pdf).

To obtain the sources:

```bash
git clone https://github.com/gadepall/geometry
```

<!---
## Vaman

### ARM-GCC

The setup manual is present [here](https://github.com/gadepall/vaman/blob/master/arm/setup/main.pdf).

To obtain the relevant sources:

```bash
svn co https://github.com/gadepall/vaman/trunk/arm
```

### FPGA

The setup manual is present [here](https://github.com/gadepall/vaman/blob/master/fpga/setup/main.pdf).

To obtain the relevant sources:

```bash
svn co https://github.com/gadepall/vaman/trunk/fpga
```
--->

## Connecting to Termux via Laptop

### SSH

**NOTE**: Skip this if you are using a bluetooth keyboard

1. Follow instructions in Section 1 of the [manual](https://github.com/gadepall/fwc-1/blob/main/installation/main.pdf).
2. On termux on your phone, enter a simple password

    ```bash
    passwd
    ```

3. This command will give you your username

    ```bash
    whoami
    ```

4. Find your ip address

    ```bash
    ifconfig
    ```

5. Start ssh server on your mobile

    ```bash
    sshd
    ```

6. On your laptop, enter the following at a terminal

    ```bash
    ssh username@ipaddress -p 8022
    ```

7. Enter the password and you are connected to termux through your laptop.

### Scrcpy

Refer to [Genymobile/scrcpy#get-the-app](https://github.com/Genymobile/scrcpy#get-the-app) for instructions.

## Installing WSL for Windows Users (NOT RECOMMENDED)

Installation instructions are present at this [link](https://ubuntu.com/wsl).

To access USB over WSL, refer to this [link](https://docs.microsoft.com/en-us/windows/wsl/connect-usb).


<!---
## Matrices

### Matrix Analysis Book

The book is present [here](https://github.com/gadepall/matrix-analysis/blob/main/main.pdf).

To obtain the sources:

```bash
git clone https://github.com/gadepall/matrix-analysis
```

## CBSE Math Solutions

The book is available [here](https://github.com/gadepall/cbse-math/blob/main/main.pdf).

To clone the sources:

```bash
git clone https://github.com/gadepall/cbse-math
```

### Previous Year Questions

Previous year papers solutions are present at [gadepall/cbse-papers](https://github.com/gadepall/cbse-papers).

To clone the sources:

```bash
git clone https://github.com/gadepall/cbse-papers
```

### Video Explanations

1. [CBSE Class 10](https://youtube.com/playlist?list=PLKN4kghPKZ9tzPopYNxV0GEb9cMwr2MJG)
2. [CBSE Class 10, Using Python](https://youtube.com/playlist?list=PLKN4kghPKZ9t37g-oL8l0LAPGMK2bL7B-)
3. [CBSE Class 12](https://youtube.com/playlist?list=PLKN4kghPKZ9uPnPqucP145qh9l7nGB3pm)

## C Programming

The textbook is present [here](https://github.com/gadepall/programming/blob/main/main.pdf).

To clone the sources:

```bash
git clone https://github.com/gadepall/programming
```
--->
