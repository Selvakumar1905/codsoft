tasks = []

while True:
    print("-----TO DO LIST MENU---\n\n1.Add\n2.View\n3.Done\n4.Delete\n5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        tasks.append(input("Enter task: "))
        print("Task added")
    elif choice == "2":
        if not tasks:
            print("No tasks")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, t)
    elif choice == "3":
        n = int(input("Task number done: "))
        if 0 < n <= len(tasks):
            tasks[n-1] += " ✔"
            print("Marked as done")
    elif choice == "4":
        n = int(input("Task number delete: "))
        if 0 < n <= len(tasks):
            tasks.pop(n-1)
            print("Task deleted")
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice")
