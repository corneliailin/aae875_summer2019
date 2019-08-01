################################# NY HOSPITALS #################################
#
# Title:
# Files: paths.py, datacleaning.py, inputdata.py, [add more here]
#
# Author:
# Email:
#
############################### OUTSIDE HELP CREDITS ###########################
#
# Persons: Cornelia Ilin
# Online sources:
#
############################### 80 COLUMNS WIDE ################################


#import modules here

'''
#
# The main.py script holds the user input and response formation for a data analyst 
# chatboot that collects user input and responds appropriately. 
#
'''

def welcome_prompt():
    '''
    # prints the welcome prompt.
    # @param: none.
    '''
    pass


def greetings(user_name):
    '''
    # Freddie gets the user name and asks what he can do.
    # @ param: user_name.
    '''
    pass


def os_and_drive_letter():
    '''
    # sets OS and drive letter. The user is prompted to enter the computer's
    # operating system. Example: Windows, Mac.
    # @param: none.
    ''' 
    pass


def input_path():
    '''
    # sets the input path and saves its value globally
    # The user is prompted to enter the input path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Input"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Input will be entered
    # in the command line.
    # @param: none.
    '''
    pass


def output_path():
    '''
    # sets the output path and saves its value globally.
    # The user is prompted to enter the output path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Output"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Output will be entered
    # in the command line.
    # @param: none.
    '''
    pass
    

def input_data():
    '''
    # inputs the raw data. The user is prompted to enter the name of the data
    # files (in csv format). For example: SPARCS2014.csv, SPARCS2015.csv,
    # SCARCS2016.csv
    # inputs the data structure. The user is prompted to enter the desired data
    # structure. Available options are: list(csv), array (numpy), dataframe(pandas)
    # @param: none
    '''
    pass
    
def data_cleaning():
	'''
	# your comments here
	'''
    pass    

def summary_stats():
	'''
	# your comments here
	'''
    pass 
    
def linear_model():
	'''
	# your comments here
	'''
    pass 
        

    
######## runs main script ########
##################################

def main():
    # print welcome prompts
    welcome_prompt()

    # print greetings; get user name
    user_input = input(">: ")
    user_input = "CI"
    greetings(user_input)
    
    # set OS and drive letter
    os_and_drive_letter()

    # set input path
    input_path()
    
    # set output path
    output_path()
    
    # input the data
    input_data()


if __name__ == "__main__":
    main()

    

    
    