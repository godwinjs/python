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
print(abs(32)) #32
print(abs(-32)) #32

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

#
print(int(min(10.23, 10.54, 10.66, 10.74, 10.99, 10.55)))

#RECORD
# Initialize the list to store the total scores for each student
total_scores = []

# Number of students
num_students = int(input("Enter the number of students: "))

# Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Collect scores for each student
for i in range(num_students):
    print(f"\nEntering scores for Student {i + 1}")
    total_score = 0
    for j in range(num_subjects):
        score = float(input(f"Enter score for subject {j + 1}: "))
        total_score += score
    total_scores.append(total_score)

# Calculate and print the average score for each student
print("\nAverage scores for each student:")
for i in range(num_students):
    average_score = total_scores[i] / num_subjects
    print(f"Student {i + 1}: {average_score:.2f}")

#END_RECORD

#RECORD
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    boolean = False
    # return [num for num in nums if (num % 7) == 0]
    if len(nums) == 0:
        return boolean

    for num in nums:
        if num % 7 == 0:
            boolean = True
            break
        else:
            boolean = False
        print(num)
    return boolean
#END_RECORD
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums])
        
        

print(has_lucky_number([3, 14]))
#RECORD

#RECORD
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [n > thresh for n in L]
#END_RECORD

#RECORD
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
#END_RECORD

#RECORD
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """

    if len(doc_list) <= 0:
        return []
    index_list = [ phrase.lower().find(keyword) for phrase in doc_list]
    found_index = [ i for i in range(len(index_list)) if index_list[i] >= 0]
    doc_index = [ index for index in found_index if keyword in [ ''.join(char for char in word if char.isalnum()) for word in doc_list[index].lower().split() ] ]
    # print(keyword, doc_list[1].lower().split(), keyword in doc_list[1].lower().split())
    # print(index_list, found_index, doc_index)
    
    return doc_index

print( word_search(['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?'], "car") )
print( word_search(["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"], "casino") )

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

def multi_word_search_long(doc_list, keyword):
    indices = { word: [] for word in keyword }

    print(indices)

    for i, doc in enumerate(doc_list):
        word = doc.split()
        formated_arr = [ word.lower().rstrip(',?!.') for word in word ]

        for key_w in keyword:
            # indices.append(i)
            if key_w in formated_arr:
                indices[key_w].append(i)
    print(indices)
multi_word_search_long(['They Learn Python Challenge Casino and car', 'They bought a car, and a horse', 'Casinoville?'], ["car", "casino"])
#END_RECORD

