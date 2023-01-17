from Class import Student
from file_readeer import openFile, Students_with_grade_6, sredno, file_content_to_class_passable_data


def main():
    print("Students with 6 -> 1, number of people with 4 -> 2, average grade -> 3, hard or easy -> 4,create a class for every student -> 5")
    a = int(input())
    if(a == 1):
        names = Students_with_grade_6("source.txt", "6")
        for i in names[0]:
            print(i)
    elif(a == 2):
        br = Students_with_grade_6("source.txt", "4")
        print(f'Num of students with 4 are {br[1]}')
    elif(a == 3):
        sredno_arit = sredno("source.txt")
        print(sredno_arit)
    elif(a == 4):
        if(sredno("source.txt") > 4.5):
            print("lesno e")
        else:
            print("trudno e")
    else:
        classes_list = []
        data = file_content_to_class_passable_data("source.txt")
        for i in range(0, len(data), 1):
            classes_list.append(
                Student(data[i]["name"], data[i]["ocenka"], data[i]["number"]))
        for i in classes_list:
            print(i)
        print("to change grade select type the number of the studentq if you dont want to change press 27")
        choice = int(input())
        if(choice != 27):
            print("new_grade")
            num = int(input())
            classes_list[choice - 1].change_grade(num)
            print(classes_list[choice - 1])


main()
