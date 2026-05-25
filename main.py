import os
FilePaths = ["/usr/bin/install_yandex", "/usr/bin/shotcut", "/usr/bin/gimp-3", "/usr/bin'audacticy", "/usr/bin/gnome-mines", "/usr/bin/gimp-3.2", "/usr/bin/gnome-maps", "/usr/bin/gnome-music", "/usr/bin/gimp-console" ]
def ApplicationRemover(paths):
    for file in paths:
        try:
            print(os.system(f'rm -rf "{file}"'))
        except:
            print('Error')
            
def whoami():
    os.system("whoami")
def cmatrix():
    os.system("dnf install cmatrix")
    os.system("cmatrix")
def disksSpace():
    os.system("df -h")

print("""(0) Remove Applications
(0) whoami
(2) Cool cmatrix")
(3) how many disks space left
Enter option -> """)
option = int(input())

if option == 0:
    ApplicationRemover(FilePaths)
elif option == 1:
    whoami()
elif option == 2:
    cmatrix()
elif option == 3:
    disksSpace()
