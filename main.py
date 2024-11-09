from task import*
import time
while(True):
    print("--------------------------------")
    print("MENU:\n\t 1.ADD TASK \n\t 2.UPDATE TASK\n\t 3.DISPLAY LIVE TASK\n\t 4.VIEW COMPLETED TASK\n\t 5.EXIT")
    print("--------------------------------")
    choice =int(input("Enter your choice: "))
    if choice==1:
        task.add()
        time.sleep(2)
    elif choice==2:
        task.updatetask()
        time.sleep(2)
    elif choice==3:
        task.livetask()
        time.sleep(2)
    elif choice==4:
        task.comtask()
        time.sleep(2)
    elif choice==5:
        print("exited sucessfully")
        exit()
    else:
        print("Enter valid choice")