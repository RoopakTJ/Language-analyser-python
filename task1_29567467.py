# Task 1 : Student Language Analyzer
# Name : Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467

import os


# file_wrangler function does the cleansing of data for analysis. All the files to be cleaned needs to be placed
# in respective directory by the User (SLI or TD)
# Arguments : List of file names for which cleansing has to be done
# Return : Once the function is executed, corresponding directories for SLI and TD will generated with cleaned
#          files with the same name inside it. New directory names will be SLI_cleaned and TD_cleaned
def file_wrangling(input_files):
    # Flag for SL files for writing it to the proper folder
    sl_indicator = False
    file1 = None

    for file in input_files:
        # Filtering out unwanted files before processing
        if file == '.DS_Store':
            continue
        if file.startswith("SL"):
            sl_indicator = True
        if sl_indicator:
            try:
                file1 = (open("SLI/"+file, "r"))
            except:
                print("Program follows linux file path")
            # Creates a new directory if not already exists
            if not os.path.isdir("SLI_cleaned"):
                os.mkdir("SLI_cleaned")
        if file.startswith("TD"):
            try:
                file1 = (open("TD/"+file, "r"))
            except:
                print("Program follows Mac linux path")
            # Creates a new directory if not already exists
            if not os.path.isdir("TD_cleaned"):
                os.mkdir("TD_cleaned")

        # Code to extract the line starting with *CHI starts -----------------------------
        saved_line = ""
        incomplete_line = False
        first_filter = []
        list2 = []

        for line in file1:
            # includes multiple line check.
            if incomplete_line:
                if line[len(line)-2] != "." and line[len(line)-2] != "!" and line[len(line)-2] != "?":
                    if line.endswith("[+ bch]\n"):
                        first_filter.append(saved_line + line)
                        incomplete_line = False
                    else:
                        incomplete_line = True
                        saved_line = saved_line + " " + line.rstrip()
                else:
                    first_filter.append(saved_line + " " + line)
                    incomplete_line = False
                    saved_line = ""

            if line.startswith("*CHI"):

                if line[len(line)-2] == "." or line[len(line)-2] == "!" or line[len(line)-2] == "?":
                    first_filter.append(line)

                if line[len(line)-2] != "." and line[len(line)-2] != "!" and line[len(line)-2] != "?":
                    if line.endswith("[+ bch]\n"):
                        first_filter.append(line)
                    else:
                        incomplete_line = True
                        saved_line = line.rstrip()

        # Removing the substring "*CHI :" from each of the line
        for each in first_filter:
            each_new = each[6:]
            current_index = first_filter.index(each)
            first_filter[current_index] = each_new

        file1.close()

        for each in first_filter:

            list1 = each.split()
            # Each word in each line to considered to check any pattern match. Finally the new string is replaced with
            # the existing string in the same index location
            for word in list1:
                current_index = list1.index(word)
                item = word
                remove = False

                if item.startswith("[") and item.endswith("]") and item != "[//]" and item != "[/]" and item != "[*]":
                    remove = True

                elif "[" in item and item != "[//]" and item != "[/]" and item != "[*]":
                    index = item.index("[")
                    item = item[:index]

                elif "]" in item and "m:+ed" in item:
                    remove = False

                elif "]" in item and item != "[//]" and item != "[/]" and item != "[*]":
                    index = item.index("]")
                    item = item[index+1:]

                if item.startswith("<") and item.endswith(">"):
                    item = item[1:-1]
                elif item.startswith("<"):
                    item = item[1:]
                elif item.endswith(">"):
                    item = item[:-1]

                if ">" in item:
                    item = item.replace(">","")

                if "<" in item:
                    item = item.replace("<","")

                if item.startswith("&") or item.startswith("+"):
                    remove = True

                if item.startswith("(") and item.endswith(")") and item != "(.)":
                    item = item[1:-1]

                if "(" in item and item != "(.)":
                    item = item.replace("(", "")

                if ")" in item and item != "(.)":
                    item = item.replace(")", "")

                if item == "[+" and not remove:
                    remove = True

                if item == "bch]" and not remove:
                    remove = True

                if remove:
                    list1.remove(word)
                else:
                    list1[current_index] = item

            statement = " ".join(list1)
            list2.append(statement)
        # File is written to the corresponding folder considering the sli_flag
        if sl_indicator:
            output = open("SLI_Cleaned/"+file, "w")
        else:
            output = open("TD_Cleaned/"+file, "w")

        for each in list2:
            output.write(each+"\n")
        output.close()










