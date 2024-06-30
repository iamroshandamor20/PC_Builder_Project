#Global data set for pre built pc.
pc_product = {
    "10000": {
        "processor": "Intel 11th Gen Silver or Celeron",
        "ram": "8 GB DDR3(4GBx2)",
        "motherboard": "Zebronics H55",
        "storage1": "120 GB SATA SSD",
        "cabinet": "Zebronics Smash with PSU",
        "os": "Windows 10 Pro"
    },
    "15000": {
        "processor": "Intel 5th Gen 560",
        "ram": "8 GB DDR3(4GBx2)",
        "motherboard": "Zebronics H65",
        "storage1": "240 GB SATA SSD",
        "cabinet": "Zebronics Smash with PSU",
        "os": "Windows 10 Pro"
    },
    "25000": {
        "processor": "AMD ryzen 3 3nd Gen",
        "ram": "8 GB DDR4(4GBx2)",
        "motherboard": "MSI elite n54",
        "storage": "120 GB NVME SSD",
        "cabinet": "Elite Smash with PSU",
        "os": "Windows 10 Pro"
    },
    "30000": {
        "processor": "Intel i3 10th Gen",
        "ram": "8 GB DDR4(8GBx1)",
        "motherboard": "Gigabyte B460M",
        "storage": "256 GB NVME SSD",
        "cabinet": "Cooler Master Q300L",
        "os": "Windows 10 Pro"
    },
    "40000": {
        "processor": "AMD Ryzen 5 3600",
        "ram": "16 GB DDR4(8GBx2)",
        "motherboard": "ASUS TUF B450-PLUS",
        "storage": "512 GB NVME SSD",
        "cabinet": "Corsair Carbide SPEC-05",
        "os": "Windows 10 Pro"
    },
    "50000": {
        "processor": "Intel i5 10th Gen",
        "ram": "16 GB DDR4(8GBx2)",
        "motherboard": "MSI B460M-A PRO",
        "storage": "512 GB NVME SSD + 1TB HDD",
        "cabinet": "NZXT H510",
        "os": "Windows 10 Pro"
    },
    "60000": {
        "processor": "AMD Ryzen 5 5600X",
        "ram": "16 GB DDR4(8GBx2)",
        "motherboard": "MSI B550 TOMAHAWK",
        "storage": "1TB NVME SSD",
        "cabinet": "Phanteks Eclipse P400A",
        "os": "Windows 10 Pro"
    },
    "70000": {
        "processor": "Intel i7 10th Gen",
        "ram": "32 GB DDR4(16GBx2)",
        "motherboard": "ASUS PRIME Z490-P",
        "storage": "1TB NVME SSD",
        "cabinet": "Cooler Master MasterBox MB520",
        "os": "Windows 10 Pro"
    },
    "85000": {
        "processor": "AMD Ryzen 7 5800X",
        "ram": "32 GB DDR4(16GBx2)",
        "motherboard": "ASUS ROG STRIX B550-F",
        "storage": "1TB NVME SSD + 2TB HDD",
        "cabinet": "Corsair iCUE 465X RGB",
        "os": "Windows 10 Pro"
    },
    "100000": {
        "processor": "Intel i9 11th Gen",
        "ram": "64 GB DDR4(16GBx4)",
        "motherboard": "MSI Z590-A PRO",
        "storage": "2TB NVME SSD + 2TB HDD",
        "cabinet": "NZXT H710i",
        "os": "Windows 10 Pro"
    }
}
    

# Defined Functions For Pre Built PC
def prebuiltpc():
    print("\t\t\t Choose Your PC Now")
    print(" \t\tEnter Your Minimum Budget :")
    minbudget = int(input("\t\t\t"))
    print("\t\t Enter Your Maximum Budget :")
    maxbudget = int(input("\t\t\t"))

# Function for choosing Mother boareds
def motherboard():
    print("\t\t ** Choose Mother Boared **")

# Function to choose Processor
def processor():
    print("\t\t ** Choose Processor **")

# Funtion for Custum Build PC
def custumbuildpc():
    print("\t\t\t Choose Your Custum PC")
    print()
    print()
    pc_condition = int(input("\t Type (1) For AMD PC Build \t\t Type (2) For Intel PC Build\n\t"))
    if pc_condition == 1:
        print("\t\t\t Type (1) To Start Choosing Your Part")
        startcondition = int(input("\t\t\t"))
        if startcondition == 1:
            processorselected = processor()
            motherboaredselected = motherboard()

    elif pc_condition == 2:
        print("\t\t\t Type (1) To Start Choosing Your Part")
        startcondition = int(input("\t\t\t"))
        if startcondition == 1:
            processorselected = processor()
            motherboaredselected = motherboard()

    else:
        print("Wrong Options !!!!!!!!!")

# Funtion to Filter
def filterpc():
    print("\t\t Apply Filters") 

# Funtion to Sort          
def sortingpc():
    print("\t\t Apply Sorting")

# Main Part to start Project
print()
print("\t\t \t*** REDEX PC ***")
print("\t\t*** Buy and Make Your Own PC's ***")
print("_________________________________________________________________")
print(" Type (1) For Pre Built PC \t Type (2) For Coustum PC Build")
pc_choose = int(input("\t\t\t   : "))
if pc_choose == 1:
    print("\t\t\t\t\t **** Pre Built PC ****")
    prebuiltpc()

elif pc_choose == 2:
    print("\t\t\t\t **** Custum PC Build **** ")
    custumbuildpc()

else:
    print("\t\t\t\t\t\t **** wrong option ****")

