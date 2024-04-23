from tkinter import *
root = Tk()

lpp = input("Choose your primal problem objective :-\n* Maximize\n* Minimize \n").lower()
no_decision_variables = int(input("Enter the number of decision variables = "))
decision_variables = []
constraints = []
inequality = []
rowno1 = []
RHS = []

non_negativity_constraint = []

def printLPP():
    rowno = 0
    Label(root, text='Step 1 :- ').grid(row=rowno)
    rowno += 1
    print("{} Z = ".format(lpp), end=" ")
    text_to_display = "{} Z = ".format(lpp)
    for i in range(len(decision_variables)):
        print(f"{decision_variables[i]}x{i+1}", end="")
        text_to_display += " "+ f"{decision_variables[i]}x{i+1}"
        if i < len(decision_variables) - 1 and decision_variables[i] >= 0:
            print(" + ", end="")
            text_to_display += " " + " + "
    print()
    Label(root, text=text_to_display).grid(row= rowno)
    rowno += 1
    Label(root, text="Subject to").grid(row= rowno)
    rowno += 1
    print("Subject to")
    
    for i in range(len(constraints)):
        text_to_display = ""
        for j in range(len(constraints[i])):
            print(f"{constraints[i][j]}x{i+1}", end=" ")
            text_to_display += " " + f"{constraints[i][j]}x{i+1} "
            if j < len(constraints[i]) - 1:
                print(" + ", end="")
                text_to_display += " + "

        if lpp == "minimize": 
            print(f">= {RHS[i]}")
            text_to_display += f">= {RHS[i]} "
        else:
            print(f"<= {RHS[i]}")
            text_to_display += f"<= {RHS[i]} "
        
        Label(root, text=text_to_display).grid(row= rowno)
        rowno += 1
    
    rowno1.append(rowno)
    
            
            
def printDual():
    rowno = rowno1[0]
    Label(root, text='-------------------------------------------').grid(row=rowno)
    rowno += 1
    Label(root, text='Step 2 :- ').grid(row=rowno)
    rowno += 1
    
    if (lpp == "maximize"):
        print("Minimize W = ", end=" ")
        text_to_display = "Minimize W = "
        
    elif (lpp == "minimize"):
        print("Maximize W = ", end=" ")
        text_to_display = "Maximize W = "
        
    for i in range(len(RHS)):
        print(f"{RHS[i]}y{i+1}", end=" ")
        text_to_display += " " + f"{RHS[i]}y{i+1} "
        if i < len(RHS) - 1:
            print(" + ", end="")
            text_to_display += " + "
    print()
    Label(root, text=text_to_display).grid(row= rowno)
    rowno += 1    
    print("Subject to")
    Label(root, text="Subject to").grid(row= rowno)
    rowno += 1    
    
    for i in range(len(result)):
        text_to_display = ""
        for j in range(len(result[i])):
            print(f"{result[i][j]}y{j+1}", end=" ")
            text_to_display += f"{result[i][j]}y{j+1} "
            if j < len(result[i]) - 1:
                print(" + ", end="")
                text_to_display += " + "
                
        if lpp == "minimize": 
            print(f"<= {decision_variables[i]}")
            text_to_display += f"<= {decision_variables[i]} "
        else:
            print(f">= {decision_variables[i]}")
            text_to_display += f">= {decision_variables[i]} "
            
        Label(root, text=text_to_display).grid(row= rowno)
        rowno += 1 
        

for i in range(no_decision_variables):
    temp = int(input("Enter coefficient of x{} = ".format(i+1)))
    decision_variables.append(temp)
    
print(decision_variables)

no_constraints = int(input("Enter the number of constraints = "))

for i in range(no_constraints):
    print("Constraint {} :=".format(i+1))
    temp_list = []
    
    for j in range(no_decision_variables):
        temp = int(input("Enter coefficient of x{} = ".format(j+1)))
        temp_list.append(temp)

    temp = input("Enter the inequality type (<=, >=, =) := ")
    inequality.append(temp)
        
    temp = int(input("Enter RHS value of the constraint : = "))
    
    if (inequality[i] == ">=" and lpp == "maximize") or (inequality[i] == "<=" and lpp == "minimize"):
        constraints.append([j * -1 for j in temp_list])
        RHS.append(temp*-1)        
    elif inequality[i] == "=":
        constraints.append(temp_list)
        constraints.append([j * -1 for j in temp_list])
        RHS.append(temp)
        RHS.append(temp*-1)
    else:
        constraints.append(temp_list)
        RHS.append(temp)    
        
result = [[constraints[j][i] for j in range(len(constraints))] for i in range(len(constraints[0]))]
    
printLPP()
printDual()

mainloop()