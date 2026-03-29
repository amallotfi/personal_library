library =[]
wishlist = []
donation=[]
choice_book = input("Enter the name of a book you own: \n").lower()
library.append(choice_book)
add_book = input("Enter the name of another book you own (or press Enter to skip): \n").lower()
if add_book:
    library.append(add_book)
    print(f"Your library: {library}")
else:
    print(f"Your library: {library}")    
wish_book = input("Enter the name of a book you wish to read: \n").lower()
wishlist.append(wish_book)
add_wish= input("Enter the name of another book you wish to have (or press Enter to skip): \n").lower()
if add_wish:
    wishlist.append(add_wish)
    print(f"Your wishlist: {wishlist}")
  

aquired =input("Enter the name of a book you've aquired from your wishlist (or press Enter to skip): \n").lower()
if aquired:
    wishlist.remove(aquired)
    library.append(aquired)
    print(f"Updated Library: {library}")
    print(f"Updated wishlist: {wishlist}")


donate_book = input("Enter the name of a book from your library you wish to donate (or press Enter to skip): \n").lower()
if donate_book:
    donation.append(donate_book)
    library.remove(donate_book)
    print(f"Your Donation book {donation}")

print("-"*50)
    
print(f"Great choices! Your final collection now features: \n{library},\nyour current wishlist is {wishlist}. \nand you've kindly donated {donation}. \nkeep up the great reading habit!")

print("-"*50)
