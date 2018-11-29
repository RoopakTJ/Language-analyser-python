# Task 2 : Student Language Analyzer - DataAnalyzer class
# Name : Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467
import os


class DataAnalyzer:

    def __init__(self):
        # Instance variables include a list of dictionaries for both SLI and TD
        self.statistics_SLI = []
        self.statistics_TD = []

    # Overriding the str method to print Instance variables in proper format
    # Returns : A string(containing lists) in proper format to print
    def __str__(self):
        return_string = "--------------------------------SDI Statistics-----------------------------------------------\n"

        # First prints the SLI list and then the TD list
        for each in self.statistics_SLI:
            return_string = return_string + str(each) + "\n"

        return_string = return_string + "\n"
        return_string = return_string + "--------------------------------TD Statistics-----------------------------------------------\n"
        return_string = return_string + "\n"

        for each in self.statistics_TD:
            return_string = return_string + str(each) + "\n"

        return return_string

    # analyse_script function iterates through all the files in the user mentioned folder, extracts repetition, grammatical
    # error, pauses, unique count and retraces from each of the file and saves as a list of dictionaries in Instance variables
    # Arguments : dir_name - Directory name
    def analyse_script(self, dir_name):
        sli_indicator = False
        if dir_name.startswith("SLI"):
            sli_indicator = True

        files = os.listdir(dir_name)

        for cleaned_file in files:

            input_file = list(open(dir_name+"/"+cleaned_file, 'r'))
            # Since while cleansing of data, we have written each CHI line to a separate line so length of input_file string
            # will give the number of statement
            individual_dict = {"number_of_statement": len(input_file)}

            repetition_count = 0
            retracing_count = 0
            grammatical_error_count = 0
            pause_count = 0
            unique_words = set()
            for each in input_file:
                input_split = each.split()
                for item in input_split:
                    if item == "[/]":
                        repetition_count += 1

                    if item == "[//]":
                        retracing_count += 1

                    if item == "m:+ed]":
                        grammatical_error_count += 1

                    if item == "(.)":
                        pause_count += 1

                    if item.isalpha():
                        unique_words.add(item)

            individual_dict["unique_words"] = len(unique_words)
            individual_dict["repetition"] = repetition_count
            individual_dict["retracing"] = retracing_count
            individual_dict["grammatical_errors"] = grammatical_error_count
            individual_dict["pauses"] = pause_count

            if sli_indicator:
                self.statistics_SLI.append(individual_dict)
            else:
                self.statistics_TD.append(individual_dict)

    # getter for instance variable sli_stats
    def get_sli_stats(self):
        return self.statistics_SLI

    # getter for instance variable td_stats
    def get_td_stats(self):
        return self.statistics_TD




