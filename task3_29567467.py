# Task 3 : Student Language Analyzer - Visualiser class
# Name : Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467

# Imports
import task1_29567467 as t1
import properties_29567467
import os
import pandas as pd
import matplotlib.pyplot as pt
from task2_29567467 import DataAnalyzer
from prettytable import PrettyTable


# Class used to visualise the data or statistics between SLI and TD using different plots
class Visualise:

    # For each object created, data-cleaning and data-analysis will be done as a part of the initialization.
    # Data frame tables for SLI and TD will be generated as a part of initialization
    # Arguments : None
    def __init__(self):
        # Using os module to list all the files in the folder and passing the list to file_wrangling function from t1.
        # SLI_cleaned and TD_cleaned folder will be auto-generated with all the cleaned files
        input_files1 = os.listdir("TD")
        t1.file_wrangling(input_files1)
        input_files2 = os.listdir("SLI")
        t1.file_wrangling(input_files2)

        d = DataAnalyzer()
        d.analyse_script("SLI_cleaned")
        d.analyse_script("TD_cleaned")

        # Instance variable sli and td will be initialized with list of dictionaries for each file
        self.sli = d.get_sli_stats()
        self.td = d.get_td_stats()
        self.average_dict = []

        # Generating pandas dataframe from the list of dictionaries
        self.sli_table = pd.DataFrame(self.sli)
        self.td_table = pd.DataFrame(self.td)

    # Print function will be used to print the values in both SLI and TD tables in tabular form.
    # This method is also an option in visualise_statistics function of the same class
    # Argument : None
    def print(self):
        # Creating an instance from PrettyTable class and setting the rows and columns
        x = PrettyTable()
        print("------------------ SLI Data For Visualisation -------------------")
        x.title = "SLI table data for Visualization"
        x.field_names = ["number_of_statement", "unique_words", "repetition", "retracing", "grammatical_errors",
                         "pauses"]
        for each in self.sli:
            row_list = [each["number_of_statement"], each["unique_words"], each["repetition"], each["retracing"],
                        each["grammatical_errors"], each["pauses"]]
            x.add_row(row_list)
        print(x)
        print()

        y = PrettyTable()
        print("------------------ TD Data For Visualisation -------------------")
        y.field_names = ["number_of_statement", "unique_words", "repetition", "retracing", "grammatical_errors",
                         "pauses"]
        for each in self.td:
            row_list = [each["number_of_statement"], each["unique_words"], each["repetition"], each["retracing"],
                        each["grammatical_errors"], each["pauses"]]
            y.add_row(row_list)
        print(y)
        print()

    # computer_averages will calculate mean value from each of the columns of the dataframes and store them in a separate
    # Data Frame
    # Argument : None
    # Return : Dataframe initialised with a list of dictionaries (including mean values of SLI and TD)
    def computer_averages(self):
        # dataframe["Column_name"].mean() function will return mean values from the column
        avg_sli = {"number_of_statement": self.sli_table["number_of_statement"].mean(),
                   "unique_words": self.sli_table["unique_words"].mean(),
                   "repetition": self.sli_table["repetition"].mean(), "retracing": self.sli_table["retracing"].mean(),
                   "grammatical_errors": self.sli_table["grammatical_errors"].mean(),
                   "pauses": self.sli_table["pauses"].mean(), "type": "SLI"}

        avg_td = {"number_of_statement": self.td_table["number_of_statement"].mean(),
                  "unique_words": self.td_table["unique_words"].mean(),
                  "repetition": self.td_table["repetition"].mean(), "retracing": self.td_table["retracing"].mean(),
                  "grammatical_errors": self.td_table["grammatical_errors"].mean(),
                  "pauses": self.td_table["pauses"].mean(), "type": "TD"}

        self.average_dict.append(avg_sli)
        self.average_dict.append(avg_td)
        return pd.DataFrame(self.average_dict)

    # visualise_statistics function is used to visualise the statistics to get some insights. This function follows a menu-
    # driven approach, taking input from the user on the type of visualisation they want to have.
    # Argument : None
    # Return : Plot and print functions
    def visualise_statistics(self):
        # Computes the average in the beginning
        average_table = Visualise.computer_averages(self)

        # User input
        plot = input(
            "Please enter the Visualisation you want to see \n 1. Mean Comparison between SLI and TD children \n"
            " 2. Mean statistics of SLI \n 3. Mean statistics of TD \n 4. Patterns in SLI (Simple plot for all SLI children) \n"
            " 5. Patterns for TD (Simple plot for all TD children) \n 6. Plot comparison for a single character \n"
            " 7. Table representation of SLI and TD")

        # First second and third option uses dataframe plots and rest uses pyplots from matplotlibs
        if plot == "1":
            average_table.plot(x="type", y=["repetition", "pauses", "number_of_statement", "unique_words", "retracing",
                                            "grammatical_errors"], kind="bar", figsize = (20, 8))
            pt.grid()
            pt.xlabel("Type of Disorder", fontdict=properties_29567467.axesfont)
            pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
            pt.title("Mean comparison between statistics of SLI and TD", fontdict=properties_29567467.titlefont)
            pt.show()

        elif plot == "2":
            # In order to get the SLI data from dataframe, we use head(1)
            average_table.head(1).plot("type",
                                       y=["repetition", "pauses", "number_of_statement", "unique_words", "retracing",
                                          "grammatical_errors"], kind="bar", figsize = (20, 8))
            pt.grid()
            pt.xlabel("Type of Disorder", fontdict=properties_29567467.axesfont)
            pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
            pt.title("Mean comparison between statistics of SLI", fontdict=properties_29567467.titlefont)
            pt.show()

        elif plot == "3":
            # In order to get the TD data from dataframe, we use tail(1)
            average_table.tail(1).plot("type",
                                       y=["repetition", "pauses", "number_of_statement", "unique_words", "retracing",
                                          "grammatical_errors"], kind="bar", figsize = (20, 8))
            pt.xlabel("Type of Disorder", fontdict=properties_29567467.axesfont)
            pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
            pt.title("Mean comparison between statistics of TD", fontdict=properties_29567467.titlefont)
            pt.grid()
            pt.show()

        elif plot == "4":
            # Using the sli_table dataframe to plot for each of the child characteristics
            pt.figure(figsize=(20,8))
            pt.plot(self.sli_table.number_of_statement, label="Number of Statement")
            pt.plot(self.sli_table.repetition, label="Repetition")
            pt.plot(self.sli_table.retracing, label="Retracing")
            pt.plot(self.sli_table.grammatical_errors, label="Grammatical Errors")
            pt.plot(self.sli_table.pauses, label="Pauses")
            pt.plot(self.sli_table.unique_words, label="Unique words")
            pt.title("Pattern change for characters of different SLI children", fontdict=properties_29567467.titlefont)
            pt.xlabel("Index of children", fontdict=properties_29567467.axesfont)
            pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
            pt.legend()
            pt.grid()
            pt.show()

        elif plot == "5":
            # Using the td_table dataframe to plot for each of the child characteristics
            pt.figure(figsize=(20,8))
            pt.plot(self.td_table.number_of_statement, label="Number of Statement")
            pt.plot(self.td_table.repetition, label="Repetition")
            pt.plot(self.td_table.retracing, label="Retracing")
            pt.plot(self.td_table.grammatical_errors, label="Grammatical Errors")
            pt.plot(self.td_table.pauses, label="Pauses")
            pt.plot(self.td_table.unique_words, label="Unique words")
            pt.title("Pattern change for characters of different TD children", fontdict=properties_29567467.titlefont)
            pt.xlabel("Index of children", fontdict=properties_29567467.axesfont)
            pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
            pt.legend()
            pt.grid()
            pt.show()

        elif plot == "6":
            # User can select the comparison between SLI and TD for each of the characteristics or all at once (Option 7)
            option = input(
                "Which character comparison u want to see \n 1. Number of statement \n 2. repetition \n 3. Retracing \n"
                " 4. Grammatical Errors \n 5. Pauses \n 6. Unique Words \n 7. All in one")

            if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6":
                pt.figure(figsize=(20,8))
                pt.plot(self.sli_table[properties_29567467.character[option]], label="SLI")
                pt.plot(self.td_table[properties_29567467.character[option]], label="TD")
                pt.title("Pattern change comparison for SLI and TD", fontdict=properties_29567467.titlefont)
                pt.xlabel("Index of children", fontdict=properties_29567467.axesfont)
                pt.ylabel("Count in number", fontdict=properties_29567467.axesfont)
                pt.legend()
                pt.grid()
                pt.show()

            # Using subplots to generate all the plots in same figure
            elif option == "7":
                i = 1
                pt.figure(figsize=(20,8))
                for each in range(1, 7):
                    pt.subplot(3, 2, i)
                    pt.plot(self.sli_table[properties_29567467.character[str(each)]], label="SLI")
                    pt.plot(self.td_table[properties_29567467.character[str(each)]], label="TD")
                    pt.title(properties_29567467.character[str(each)], fontdict=properties_29567467.smalltitlefont)
                    pt.ylabel("Count in number", fontdict=properties_29567467.smallfont)
                    pt.legend()
                    pt.grid()
                    i = i + 1
                pt.show()
            else:
                print("Please restart and choose a proper option")
        # Visualisation in tabular form
        elif plot == "7":
            Visualise.print(self)
        # For all other invalid user input, program will terminate with error message
        else:
            print("Please restart and choose a proper option")


# Runs only when this file is executed as main
if __name__ == "__main__":
    v = Visualise()
    v.visualise_statistics()
