import time
ranks = "__23456789TJQKA"
suits = "HCDS"
straights = [ \
    "65432", \
    "76543", \
    "87654", \
    "98765", \
    "T9876", \
    "JT987", \
    "QJT98", \
    "KQJT9", \
    "AKQJT"
    ]

def rank_order(card):
    return ranks.find(card[0])

def suit_order(card):
    return suits.find(card[-1])

def hand_ranks(hand):
    return "".join([card[0] for card in hand])

def hand_suits(hand):
    return "".join([card[1] for card in hand])

def find_multiples(hand):
    seen = []
    pairs = []
    triples = []
    fours = []
    for card in hand:
        if card[0] in seen:
            if card[0] in triples:
                triples = [rank for rank in triples if rank != card[0]]
                fours.append(card[0])
            elif card[0] in pairs:
                pairs = [rank for rank in pairs if rank != card[0]]
                triples.append(card[0])
            else:
                pairs.append(card[0])
        else:
            seen.append(card[0])
    
    hand = [card for card in hand \
        if (card[0] not in pairs) \
            and (card[0] not in triples) \
            and (card[0] not in fours)]
    # print(pairs, triples, fours, hand)
    return (pairs, triples, fours, hand)

def royal_flush(hand):
    # print("royal_flush", hand_suits(hand))
    result = 0
    if (hand_ranks(hand) == "AKQJT") and (flush(hand) != 0):
        result = 100000000 * suits.index(hand[0][1])
    return result

def straight_flush(hand):
    # print("straight_flush", hand_suits(hand))
    result = 0
    if (straight(hand) != 0) and (flush(hand) != 0):
        result = 100000000 * suits.index(hand[0][1])
    return result

def four_of_a_kind(hand):
    result = 0
    (_, _, fours, hand) = find_multiples(hand)
    if (len(fours) == 1):
        # print("four_of_a_kind", fours[0])
        result += 100000000 * ranks.index(fours[0])
        result += high_card(hand)
    return result

def full_house(hand):
    result = 0
    (pairs, triples, _, hand) = find_multiples(hand)
    if (len(triples) == 1) and (len(pairs) == 1):
        # print("full_house", triples[0], pairs[0])
        result += 100000000 * ranks.index(triples[0])
        result += 1000000 * ranks.index(pairs[0])
    return result

def flush(hand):
    # print("flush", hand_suits(hand))
    result = 0
    if len(set(hand_suits(hand))) == 1:
        result = 100000000 * suits.index(hand[0][1])
    return result

def straight(hand):
    # print("straight", hand_ranks(hand))
    result = 0
    if hand_ranks(hand) in straights:
        result = 100000000 * ranks.index(hand[0][0])
    return result
    
def three_of_a_kind(hand):
    result = 0
    (pairs, triples, _, hand) = find_multiples(hand)
    if (len(triples) == 1) and (len(pairs) == 0):
        # print("three_of_a_kind", triples[0])
        result += 100000000 * ranks.index(triples[0])
        result += high_card(hand)
    return result

def two_pairs(hand):
    result = 0
    (pairs, triples, _, hand) = find_multiples(hand)
    if (len(pairs) == 2) and (len(triples) == 0):
        # print("two_pairs", pairs[0], pairs[1])
        result += 100000000 * ranks.index(pairs[0])
        result += 1000000 * ranks.index(pairs[1])
        result += high_card(hand)
    return result

def one_pair(hand):
    result = 0
    (pairs, triples, _, hand) = find_multiples(hand)
    if (len(pairs) == 1) and (len(triples) == 0):
        # print("one_pair", pairs[0])
        result += 100000000 * ranks.index(pairs[0])
        result += high_card(hand)
    return result

def high_card(hand):
    # print("high_card", hand)
    result = ""
    for card in hand:
        result += format(ranks.index(card[0]), "0>#2d")
    return int(result)

possible_hands = [
    ("Royal Flush", 90000000000, royal_flush),
    ("Straight Flush", 80000000000, straight_flush),
    ("Four of a Kind", 70000000000, four_of_a_kind),
    ("Full House", 60000000000, full_house),
    ("Flush", 50000000000, flush),
    ("Straight", 40000000000, straight),
    ("Three of a Kind", 30000000000, three_of_a_kind),
    ("Two Pairs", 20000000000, two_pairs),
    ("One Pair", 10000000000, one_pair),
    ("High Card", 0, high_card)
]

def split_deal(deal):
    # print("split_deal", deal)
    result = None
    cards = deal.split(" ")
    p1_hand = sorted(cards[:5], key=rank_order, reverse=True)
    p2_hand = sorted(cards[5:], key=rank_order, reverse=True)
    result = (p1_hand, p2_hand)
    return result

def score_hand(hand):
    # print("score_hand", hand)
    for (name, score, test) in possible_hands:
        hand_test = test(hand)
        if hand_test > 0:
            return (name, score+hand_test)
    return ("None", 0)

def play_deal(deal, scores):
    # print("play_deal ", deal)
    deal = deal.strip()
    (p1_hand, p2_hand) = split_deal(deal)
    print(p1_hand, p2_hand)
    (p1_score, p2_score) = (score_hand(p1_hand), score_hand(p2_hand))
    if p1_score[1] > p2_score[1]:
        scores[0] += 1
    else:
        scores[1] += 1
    print(p1_score, p2_score, scores)    
    return scores

def main():
    results = [0,0]

    with open("p054_poker.txt", "r") as datafile:
        deal = datafile.readline()
        while deal:
            results = play_deal(deal, results)
            deal = datafile.readline()
            print()
            time.sleep(5)

    # play_deal("AS AD AC AH KD 2H 3C 5D 7S JH", results)
    # play_deal("9S 8S 7S 6S 5S 2H 3C 5D 7C JH", results)
    # play_deal("AS KS QS JS TS 2H 3C 5D 7C JH", results)

    print(results)

main()