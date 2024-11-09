todo=[]
updattodo=[]

class task:
    def add():
        title=input("Enter the title:")
        todo.append(title)
        print(title ,"added successfully...")
    def display(a):
         for i in range(len(a)):
            print(i+1+")",a[i])
        
    def updatetask():
            task.display(todo)
            sno=int(input("Enter the completed task ID no: "))
            
            updattodo.append(todo[sno-1])
            print("Task updated successfully..\n")
            todo.pop(sno-1)
    def livetask():
        print("Your Pending task.....\n")
        task.display(todo)
    def comtask():
        print("Your completed task....\n")
        task.display(updattodo)
            
    
