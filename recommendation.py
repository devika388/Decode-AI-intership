print("======================================")
print("      FOOD RECOMMENDATION SYSTEM")
print("======================================")

print("\nChoose your preferred cuisine:")
print("1. South Indian")
print("2. North Indian")
print("3. Chinese")
print("4. Italian")
print("5. Desserts")

choice = input("\nEnter your choice (1-5): ")

print("\nChoose your spice level:")
print("1. Mild")
print("2. Medium")
print("3. Spicy")

spice = input("Enter your choice (1-3): ")

print("\n========== RECOMMENDATIONS ==========")

if choice == "1":
    print("Cuisine: South Indian")
    if spice == "1":
        print("- Idli")
        print("- Pongal")
        print("- Curd Rice")
    elif spice == "2":
        print("- Masala Dosa")
        print("- Vegetable Uttapam")
        print("- Lemon Rice")
    elif spice == "3":
        print("- Chettinad Chicken")
        print("- Andhra Biryani")
        print("- Spicy Chicken Curry")
    else:
        print("Invalid spice level.")

elif choice == "2":
    print("Cuisine: North Indian")
    if spice == "1":
        print("- Dal Makhani")
        print("- Paneer Butter Masala")
        print("- Jeera Rice")
    elif spice == "2":
        print("- Butter Chicken")
        print("- Chole Bhature")
        print("- Paneer Tikka")
    elif spice == "3":
        print("- Chicken Tikka Masala")
        print("- Mutton Rogan Josh")
        print("- Spicy Kebabs")
    else:
        print("Invalid spice level.")

elif choice == "3":
    print("Cuisine: Chinese")
    if spice == "1":
        print("- Veg Fried Rice")
        print("- Sweet Corn Soup")
        print("- Hakka Noodles")
    elif spice == "2":
        print("- Schezwan Fried Rice")
        print("- Chilli Paneer")
        print("- Manchurian")
    elif spice == "3":
        print("- Spicy Schezwan Noodles")
        print("- Dragon Chicken")
        print("- Hot Garlic Chicken")
    else:
        print("Invalid spice level.")

elif choice == "4":
    print("Cuisine: Italian")
    if spice == "1":
        print("- Alfredo Pasta")
        print("- Margherita Pizza")
        print("- Garlic Bread")
    elif spice == "2":
        print("- Arrabbiata Pasta")
        print("- Veg Pizza")
        print("- Lasagna")
    elif spice == "3":
        print("- Spicy Pepperoni Pizza")
        print("- Spicy Penne Pasta")
        print("- Chilli Cheese Pizza")
    else:
        print("Invalid spice level.")

elif choice == "5":
    print("Dessert Recommendations")
    print("- Chocolate Brownie")
    print("- Ice Cream")
    print("- Gulab Jamun")
    print("- Cheesecake")
    print("- Rasmalai")

else:
    print("Invalid choice. Please run the program again.")

print("\n======================================")
print("Thank you for using the Food Recommendation System!")
print("======================================")