spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount * 4

if spam_amount > 0:
    print("But I don't want any Spam!!") #indentation indictes that all indented code belongs to the conditional above:

viking_song = "Spam " * spam_amount #operator overloading
print(viking_song)

# Numbers and arithmetic in Python
type(spam_amount) #int
type(19.95) #float

a = 4
b = 2

print(a/b) # true division = 2
print(a//b) # floor division = 
print(a%b) # modulus: Integer remainder after division of a by b
print(a**b) # 4*4 Exponential: a raised to the power of b
print(-a) # Negation: The negative of a

# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction. 9ja BODMAS 😒
#when order isn't what we expected

hat_height_cm = 25
my_height_cm = 190
# how tall am i, in meters, when wearing my hat
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
#correct
total_height_meters = ( hat_height_cm + my_height_cm ) / 100
print("Height in meters =", total_height_meters, "?")

print(min(1, 2, 3))
print(max(1, 2, 3))

#abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
