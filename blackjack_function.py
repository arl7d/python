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
    def conv(holder):
        print(holder)
        a_flag = 0
        for i in range(len(holder)):
            if holder[i] == 'J' or holder[i] == 'Q' or holder[i] == 'K':
                holder[i] = 10
            elif holder[i] == 'A':
                holder[i] = 1
                a_flag = 1
            else:
                holder[i]=int(holder[i])

        total = 0
        for ele in range(len(holder)):
            total = total + holder[ele]

        if total < 12 and a_flag == 1:
            total = total + 10
        elif total > 21:
            total = 0         
        print(total)
        return total
    
    return conv(hand_1) > conv(hand_2)
