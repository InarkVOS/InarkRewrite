import os
newhost = input("Enter new hostname: ")
print("Updating hostname to " + newhost)
os.remove('conf/hostname')
hostname = open("conf/hostname", "w")
hostname.write(newhost)
hostname.close()
print("Hostname updated to reload the prompt type: rlprompt")