""" This program simulates a printer """
formats = {
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
            'paper': 1,
        },
        'price': 25
    }
}

resources = {
    'ink': 500,
    'paper': 100,
    'profit': 0
}

selection = " "
while selection:
    
    report_status = input("Do you want to check the available resources, enter report: ")
    print("This is the available resources " + str(resources))
    format_choice = input("In which format would you like to print, either greyscale or coloured:")
    if format_choice.lower() == 'greyscale' or 'coloured':
        num = input("How many pages would you like to print:")
        if len(num) > 0 :
            print("Please wait a moment while we check if the available resources is enough to print the project")
        else:
            print("The number of pages should be greater than zero")
            num = input("How many pages would you like to print:")
    else:
        print ("Please enter either of greyscale or coloured")
        format_choice = input("In which format would you like to print, either greyscale or coloured:")

    """ To check if the available resources is enough to print the project """
    print("Calculating the ink required to print the project.......")
    required_ink = formats[format_choice]['materials']['ink']*int(num)
    print("The amount of ink needed to print the project is " + str(required_ink) + " ml")
    if required_ink > resources['ink']:
        print("Sorry there is not enough ink ")

    print("Calculating the papers required to print the project......")
    required_paper = formats[format_choice]['materials']['paper']*int(num)
    print("The amount of papers needed to print the project is " + str(required_paper) + " pages")
    if required_paper > resources['paper']:
        print("Sorry there is not enough paper")

    """ To calculate the process Price for printing the project """
    process_price = formats[format_choice]['price'] * int(num)
    print ("The price for printing the project is "  + str(process_price)+ " Naira")

    print("There are only 4 currencies accepted by us, Biyar = 5, Faiba = 10, Muri = 20, Wazobia = 50")
    print("Keep entering currencies to pay, enter stop to indicate you have paid finish")
    paid_up = " "
    Total_payment = 0
    while paid_up:
        payment_prompt = input("Please enter your payment in the accepted currencies ")
        if payment_prompt.lower() == 'biyar':
            payment_prompt = 5
        elif payment_prompt.lower() == 'faiba':
            payment_prompt = 10
        elif payment_prompt.lower() == 'muri':
            payment_prompt = 20 
        elif payment_prompt.lower() == 'wazobia':
            payment_prompt = 50
        else:
            print("That is not an accepted currency")
        print ("Do you want stop the payment?")
        paid_up = input ("Yes to stop, no to continue: ")
        if paid_up.lower() == 'yes':
            paid_up = False

        Total_payment = Total_payment + payment_prompt
    print ("The total amount you have paid is " + str(Total_payment) + "naira")

    if Total_payment < process_price:
        print("Sorry thats not enough money. Money Refunded!")
    elif Total_payment == process_price:
        print("There is no change")
    else:
        change = Total_payment - process_price
        print("Here is your change " + str(change))

    if required_ink <= resources['ink']:
        if required_paper <= resources['paper']:
            if Total_payment >= process_price:
                print("Here is your project, Thank you for using our services!")
                resources['ink'] = resources['ink']-required_ink
                resources['paper'] = resources['paper']-required_paper
                resources['profit'] = resources['profit'] + process_price

    selection : input("Do you have additional projects to print, enter off to stop, and any other word to continue ")
    if selection == 'off':
        selection = False
        print("Switched Off, Goodbye!!!")





