import FCFS
import SSTF
import SCAN
import CSCAN
import LOOK
import CLOOK


# INPUTS: 98 183 37 122 14 124 65 67
# HEAD: 53
def start():
    print("\n")
    print("----------DISK SCHEDULING----------")
    print("[1] FIRST COME FIRST SERVE (FCFS)")
    print("[2] SHORTEST SEEK TIME FIRST (SSTF)")
    print("[3] SCAN")
    print("[4] CIRCULAR SCAN (CSCAN)")
    print("[5] LOOK")
    print("[6] CIRCULAR LOCK (CLOOK)")
    print("[7] Exit")
    print("----------------------------------")
    choice = input("Enter choice: ")
    choices(choice)


def choices(choice):
    if choice == "1":
        print("\n")
        print("FIRST COME FIRST SERVE (FCFS)")
        FCFS.run()
        start()
    elif choice == "2":
        print("\n")
        print("SHORTEST SEEK TIME FIRST (SSTF)")
        SSTF.run()
        start()
    elif choice == "3":
        print("\n")
        print("(SCAN)")
        SCAN.run()
        start()
    elif choice == "4":
        print("\n")
        print("CIRCULAR SCAN (CSCAN)")
        CSCAN.run()
        start()
    elif choice == "5":
        print("\n")
        print("(LOOK)")
        LOOK.run()
        start()
    elif choice == "6":
        print("\n")
        print("CIRCULAR LOCK (CLOOK)")
        CLOOK.run()
        start()
    elif choice == "7":
        import sys
        sys.exit("Program terminated.")
    else:
        print("Invalid input.")


start()
