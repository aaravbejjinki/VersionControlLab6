#Aarav Bejjinki
#Encoder function to add 3 to each index in password
def encoder(password):
   #intializes variable "str
   str = ""
   #for loop to get each index in password (i)
   for i in password:
       #adds 3 to each index in the original password and ensures that it is the final digit if the value is greater than 10. Places this in the string "str"
       str += str((int(i) + 3) % 10)
   return str


#Main method
def main():
   #Menu
   print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
   choice = 0
   while choice != "3":
       choice = input("Please enter an option:")
       #if the user chooses option 1
       if choice == "1":
           #password is set to the user input.
           password = input("Please enter your password to encode:")
           #calls the encoder function and makes it the new value for "password"
           password = encoder(password)
           #print statement for the password after it has been encoded.
           print("Your password has been encoded and stored!")
       #if the user chooses option 2
       elif choice == "2":
           #Prints the encoded password because you can only choose option 2 after 1. The original would be the decoded version of the encoded password.
           print(f"The encoded password is {password}, and the original password is {decoder(passord)}.")


#Runs the main method
if __name__ == "__main__":
   main()
