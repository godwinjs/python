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

#RECORD
import math

print("Math is a {}".format(type(math)), round(math.pi, 3) )
print(dir(math))
print("Math.pi to 4 significant figures {:.4}".format(math.pi))
print(math.log(32, 2))

# Using the array module
import array as arr

# Creating an array of integers
my_array = arr.array('i', [1, 2, 3, 4, 5])
print(type(arr))
#END_RECORD

#RECORD
def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

print(best_items([
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    # Sometimes the racer's name wasn't recorded
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]) )

#END_RECORD

#RECORD
def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

print(best_items([
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell'], 'finish': 3}, 
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell'], 'finish': 1}, 
    {'name': 'Bowser', 'items': ['green shell'], 'finish': 1}, 
    {'name': None, 'items': ['green shell'], 'finish': 2}, 
    {'name': 'Bowser', 'items': ['green shell'], 'finish': 1}, 
    {'name': None, 'items': ['red shell'], 'finish': 1}, 
    {'name': 'Yoshi', 'items': ['banana', 'blue shell', 'banana'], 'finish': 7}, 
    {'name': 'DK', 'items': ['blue shell', 'star'], 'finish': 1}
]) )

#END_RECORD 

#RECORD
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    def format_points(list):
        list_fmt = []

        for item in list:
            if item.isalpha() and not item == "A":
                list_fmt.append('10')
            elif item == "A":
                list_fmt.append("A")
            else:
                list_fmt.append(item)
        return list_fmt
    
    def sum_points(list):
        point = 0

        for item in list:
            if item.isdigit():
                point = point + int(item)
                if (point) > 21 and "A" in list:
                    point = point - 10
            if item == "A":
                if (point + 11) <= 21:
                    point = point + 11
                else:
                    point = point + 1
        return point

            
    hand1_fmt = format_points(hand_1)
    hand2_fmt = format_points(hand_2)
    
    if sum_points(hand2_fmt) > 21:
        return True
    elif sum_points(hand1_fmt) > 21:
        return False
    else:
        return sum_points(hand1_fmt) > sum_points(hand2_fmt)

print(blackjack_hand_greater_than(['K', 'A', '3'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10', '12']))
print(blackjack_hand_greater_than(['K', 'A', '2'], ['3']))
print(blackjack_hand_greater_than(['9'], ['9', 'Q', '8', 'A']))
#END_RECORD

#RECORD
def format_points(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total + 10 <= 21 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    
    if format_points(hand_2) > 21:
        print(format_points(hand_1), format_points(hand_2))
        return True
    elif format_points(hand_1) > 21:
        print(format_points(hand_1), format_points(hand_2))
        return False
    else:
        print(format_points(hand_1), format_points(hand_2))
        return format_points(hand_1) > format_points(hand_2)

print(blackjack_hand_greater_than(['K', 'A', '3'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10', '12']))
print(blackjack_hand_greater_than(['K', 'A', '2'], ['3']))
print(blackjack_hand_greater_than(['9'], ['9', 'Q', '8', 'A']))
#END_RECORD