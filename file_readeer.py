def openFile(filename):
    a = []
    with open(filename, 'r', encoding="utf-8") as content:
        for i in content:
            a.append(i)
    return a


def Students_with_grade_6(filename, grade):
    arr = []
    br = 0
    grades_to_display = []
    file_content = openFile(filename)
    file_length = 0
    for i in file_content:
        grades_to_display.append(i)
        file_length += 1
    for i in range(0, file_length, 1):
        if(grades_to_display[i][-2] == grade):
            br += 1
            if(grades_to_display[i][1] == ' '):
                arr.append(grades_to_display[i][2:-2])
            else:
                arr.append(grades_to_display[i][3:-2])
    return [arr, br]


def sredno(filename):
    sredno = 0
    file_content = openFile(filename)
    br = 0
    grades_to_display = []
    file_length = 0
    for i in file_content:
        grades_to_display.append(i)
        file_length += 1
    for i in range(0, file_length, 1):
        sredno += int(grades_to_display[i][-2])
        print(grades_to_display[i][-2])
        br += 1
    return sredno / br


def break_file_into_lines(filename, line_to_be_taken):
    arr = []
    result = dict()
    file_content = openFile(filename)
    for i in file_content:
        arr.append(i)
    for i in range(0, len(arr), 1):
        if((i + 1) == line_to_be_taken):
            result['number'] = arr[i][0:2]
            result['name'] = arr[i][2:-3]
            result['ocenka'] = arr[i][-2]
    return(result)


def file_content_to_class_passable_data(filename):
    data = []
    file_contnent = openFile(filename)
    for i in range(1, 26, 1):
        string = ""
        raw_info_from_line_of_file = (break_file_into_lines(filename, i))
        data.append(raw_info_from_line_of_file)
    return data
