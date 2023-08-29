

def write_rcnn(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()
        print("file: ", lines)
        i = 0
        for line in lines:
            print("line: ", i, line)
            #i += 1
            #print(line)
            # Split the line based on blank spaces
            parts = line.split()
            #print(len(parts))
            # Do something with the parsed parts
            if(len(parts) > 2):
                j = i
                lines.pop(j)
                # Insert the new line at the specified position
                p = 1
                while p < len(parts):
                    new_line = parts[0] + "," + parts[p]
                    lines.insert(j, new_line + "\n")
                    p += 1
                    if(p != len(parts)):
                        j += 1
            i += 1
            print("line: ", i)
    



    # Write the modified content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)

    #print("New line inserted at position:", insert_position)


    file.close()

    return











file_path_train = "data_train.txt"
file_path_test = "data_test.txt"
write_rcnn(file_path_train)
write_rcnn(file_path_test)