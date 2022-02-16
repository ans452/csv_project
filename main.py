import csv
import os

def create_table(*args):
    error = "Invalid input\n Just follow the example\n create_table(col1_list,col2_list...name_of_fields_list, \"file_name.csv\")"
    #checking starts ==========================================
    if args and len(args) > 2:
        file_name = args[len(args)-1]
        fieldname = args[len(args)-2]
        #fieldname has to have the length of amount of columns
        if len(fieldname) != len(args)-2:
            print(error)
            print("Before the last input, fieldname list is expected")
            print("Its length must correspond to the amount of columns")
        counter = len(args[0])
        for i in range(len(args)-2):
        # Middle arguments have to be a lists
            if not isinstance(args[i], list):
                print(error)
                print("Middle arguments have to be lists")
                return
            # Middle arguments have to have the same length
            if len(args[i]) != counter:
                print(error)
                print("Middle arguments have to have the same length")
                return
            
        # Last argument has to be a string        
        if not isinstance(file_name, str):
            print(error)
            print("Last argument is supposed to be a string")
            return
        # Parsing the arrays into one list
        lines = []
        for i in range(counter):
            lines.append([])
        for i in range(len(args)-2):
            for j in range(len(args[i])):
                lines[j].append(args[i][j])

        #writing a file
        with open(file_name, 'w') as new_table:
            csv_writer = csv.writer(new_table, delimiter = '\t')

            #Write header
            csv_writer.writerow(fieldname)

            for line in lines:
                csv_writer.writerow(line)
        print("Creates successfully")
        return
    #Empty input
    print(error)
    print("Empty input")
    return
                
def main():
    Oms = [18.341, 18.391, 18.441, 18.491, 18.541, 18.591, 18.641, 18.691, 18.741, 18.791, 18.841, 18.891, 18.941]
    t = [0, 48.51, 92.05, 139.76, 180.69, 232.22, 292.34, 346.51, 403.84, 464.01, 521.69, 585.40, 645.56]

    create_table(Oms, t, ['Oms', 't'],'name.csv')

if  __name__ == '__main__':
    main()
