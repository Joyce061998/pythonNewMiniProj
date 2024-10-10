
palindrome =input("Enter a string:  ") # Step 1: Get user input
palindrome1 = palindrome[::-1]  # Step 2: Reverse the input string using slicing
if palindrome == palindrome1: # Step 3: Check if the original string is equal to the reversed string
    print("The string is a palindrome!") # Step 4a: If they are the same, print that it's a palindrome
else:
    print("The string is not a palindrome.") #Step 4b: If they are different, print that it's not a palindrome