#Installing neovim

#Debian
sudo apt install neovim ranger libxtst-dev libx11-dev python3-pynvim
pip3 install ueberzug


#Installing vim-plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

curl -fLo ~/.config/nvim/init.vim --create-dirs https://raw.githubusercontent.com/gadepall/termux/main/neovim/init.vim

#Enter plugin
nvim ~/.config/nvim/init.vim       
:PlugInstall
:qa!

#Beginners may ignore the following

#For installing a plugin
#call plug#begin('~/.config/nvim/plugged') 
#Plug 'lervag/vimtex' 
#call plug#end()

nvim

:UpdateRemotePlugins
:q!
#To remove a plugin
#call plug#begin('~/.config/nvim/plugged') 
#Plug 'lervag/vimtex' 
#call plug#end()
:w
:!source ~/.config/nvim/init.vim
:PlugClean

Enter y

#Arch
sudo pacman -Sy ranger python-pynvim ueberzug
#All other instructions remain the same

