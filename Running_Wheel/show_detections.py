def show_detections():
    # raw_input returns the empty string for "enter"
    POS = {'yes','y', 'ye', ''}
    NEG = {'no','n'}

    choice = input('Would you like to display detections? ')

    if choice in POS:
       return True
    elif choice in NEG:
       return False
    else:
       print("Please respond with 'yes' or 'no' \n")

       