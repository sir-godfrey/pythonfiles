#This program simulates a printing machine 
class PrinterSim: #creating a class called printer simulator
    formats= {
        'coloured': {
            'materials': {
                'ink': 7,
                'paper': 1,
            },
            'price': 35
        },
        'greyscale': {
            'materials': {
                'ink': 5,
                'paper': 1
            },
            'price': 25
        }
    }
    resources = {
        'ink': 500,
        'paper': 100,
        'profit': 0
    }
    def init(self):
        self.format_choice = ""
        self.num_of_pages = " "
        self.printpay = " "
        self.payment_prompt = " "
        self.report_off_action = " "
        self.required_ink = 0
        self.required_paper= 0
        self.process_price = 0
        self.total_payment = 0
        self.printaccount = 0
        self.change = 0

   
        
    def report_status(self):
        print("Welcome to Printer Software Corporation")
        print("Would you like to get the resources report or off the printer ")
        self.report_off_action = input("Enter report for resources report or off to switch off the printer=> ")
        while self.report_off_action == 'report' or self.report_off_action == 'off':
            if self.report_off_action.lower() == 'report':
                print (self.resources)
                break
            elif self.report_off_action.lower() == 'off':
                exit()
            else:
                print("Enter either report to get resource status or off to switch off, enter again ")
                self.report_off_action = input("Enter report for resources report or off to switch off the printer=> ")
                continue


    def format_chooser(self): #this is a method prompts the user to choose a format for printing the project
        self.format_choice = " "
        while self.format_choice:
            self.format_choice = input("In which format would you like to print greyscale or coloured? " )
            if self.format_choice == 'coloured' or self.format_choice == 'greyscale':
                self.num_of_pages = input("How many pages would you be printing? => ")
                if len(self.num_of_pages) >= 0:
                    print("Please wait a moment while we calculate if the available resources would be enough to print")
                else:
                    print("The number of pages to be printed should be a positive number")
                    self.num_of_pages = input("You can re enter the number of pages you would be printing")
                break
            else:
                print (self.format_choice + " is not an accepted format, the accepted formats are greyscale or coloured, please enter the value again")
                
    def resources_checker(self):
        #this method checks if the available resources is enough to print the project
        self.required_ink = self.formats[str(self.format_choice)]['materials']['ink'] * int(self.num_of_pages) 
        print("The amount of ink required for the project is " + str(self.required_ink) + " ml")
        if self.required_ink > self.resources['ink']:
            print("Sorry, there is not enough ink to successfully print the project")
            
            
        self.required_paper = self.formats[self.format_choice]['materials']['paper'] * int(self.num_of_pages) 
        print("The amount of paper required for the project is " + str(self.required_paper) + " pages")
        if self.required_paper > self.resources['paper']:
            print("Sorry, there is not enough paper to successfully print the project")
            
    def process_price_printing(self):#this method calculates the price the user would pay to print the project
        self.process_price = self.formats[self.format_choice]['price'] * int(self.num_of_pages)
        print("The price for printing this project is ₦" + str(self.process_price))
        self.payment_prompt = input("Would you like to pay now?, enter yes to proceed to payment portal ")
        if self.payment_prompt.lower() == 'yes':
            print("There are only four(4) accepted currencies to be used on this printer and they are represented by their street names")
            print("Biyar represents ₦5, Faiba represents ₦10, Muri represents ₦20 and Wazobia represents ₦50 ")
            print("Please enter the street names of the currency you want to pay in the appropriate order and enter stop when you want to close to payment portal")
            self.printpay = ""
            self.total_payment = 0
            while self.printpay != "stop":
                self.printpay = input("Please enter the currencies in the accepted format or enter stop to close payment portal ")
                if self.printpay.lower() == 'biyar':
                    self.printaccount = 5
                elif self.printpay.lower() == 'faiba':
                    self.printaccount = 10
                elif self.printpay.lower() == 'muri':
                    self.printaccount = 20
                elif self.printpay.lower() == 'wazobia':
                    self.printaccount = 50
                elif self.printpay.lower() == 'stop':
                    self.printaccount = 0
                    print("Thank You for paying")                    
                else:
                    self.printaccount = 0
                    print(self.printpay + " is not an accepted entry. do re enter")
                self.total_payment = self.total_payment + self.printaccount
            print("The total amount you paid is ₦" + str(self.total_payment))
        
        
    def change_calculator(self):
        if self.total_payment < self.process_price:
            print("Sorry, the total amount you entered is not enough to print the project, Your money has been refunded!")
        elif self.total_payment == self.process_price:
            print("You dont have any change")
        else:
            self.change = self.total_payment - self.process_price
            print("Here is your change of ₦" + str(self.change))
    
    def printing_works(self):
        if self.required_ink <= self.resources['ink']:
            if self.required_paper <= self.resources['paper']:
                if self.total_payment >= self.process_price:
                    print("Your project has been printed, thank you for using our services!!!")
                    self.resources['ink'] = self.resources['ink'] - self.required_ink
                    self.resources['paper'] = self.resources['paper']- self.required_paper
                    self.resources['profit'] = self.resources['profit']+ self.process_price
    
# if __name__ == "__main__":         
def printer(): # a function to print the problem
    obj = PrinterSim() #assigning the class to a variable obj
    state = True     
    while state:
        obj.report_status()
        obj.format_chooser()
        obj.resources_checker()
        obj.process_price_printing()
        obj.change_calculator()
        obj.printing_works()
       
        print("Do you have another project to print. enter yes to print or no to off")
        start_now = input("enter yes or no:")
        if start_now == 'yes':
          state =True 
        else:
          state = False
          print("Goodbye!!! Switching off.....") 

printer() 

         

