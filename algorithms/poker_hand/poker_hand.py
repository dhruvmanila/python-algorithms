from __future__ import annotations
from typing import Tuple, List
from operator import itemgetter


class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Attributes: (read-only)
        hand: string representating the hand consisting of five cards

    Methods:
        compare_with(opponent): takes in player's hand (self) and
            opponent's hand (opponent) and compares both hands according to
            the rules of Texas Hold'em.
            Returns one of 3 strings (Win, Loss, Tie) based on whether
            player's hand is better than opponent's hand.

        hand_name(): Returns a string made up of two parts: hand name
            and high card.

    Supported operators:
        Rich comparison operators: <, >, <=, >=, ==
    """

    _HAND_NAME = [
        "High card",
        "One pair",
        "Two pairs",
        "Three of a kind",
        "Straight",
        "Flush",
        "Full house",
        "Four of a kind",
        "Straight flush",
        "Royal flush",
    ]

    _CARD_NAME = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, hand: str):
        """
        Initialize hand.
        Hand should of type str and should contain only five cards each
        separated by a space.

        The cards should be of the following format:
        [card value][card suit]

        The first character is the value of the card:
        2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)

        The second character represents the suit:
        S(pades), H(earts), D(iamonds), C(lubs)
        """
        # TODO: Input checking
        if not isinstance(hand, str):
            raise TypeError("Hand should be of str type.")
        self._hand = hand
        self._first_pair = 0
        self._second_pair = 0
        self._cards = self._internal_state()
        self._hand_value = self._total_hand_value()
        self._hand_type = self._hand_type()
        self._high_card = self._high_card()

    @property
    def hand(self):
        """Returns the self hand"""
        return self._hand

    def compare_with(self, other: PokerHand) -> str:
        """
        Determines the outcome of comparing self hand with other hand.
        Returns the output as 'Win', 'Loss', 'Tie' according to the rules of
        Texas Hold'em.

        Here are some examples:
        >>> player = PokerHand("2H 3H 4H 5H 6H")  # Stright flush
        >>> opponent = PokerHand("KS AS TS QS JS")  # Royal flush
        >>> player.compare_with(opponent)
        'Loss'

        >>> player = PokerHand("2S AH 2H AS AC")  # Full house
        >>> opponent = PokerHand("2H 3H 5H 6H 7H")  # Flush
        >>> player.compare_with(opponent)
        'Win'

        >>> player = PokerHand("2S AH 4H 5S 6C")  # High card
        >>> opponent = PokerHand("AD 4C 5H 6H 2C")  # High card
        >>> player.compare_with(opponent)
        'Tie'
        """
        # Breaking the tie works on the following order of precedence:
        # 1. First pair (default 0)
        # 2. Second pair (default 0)
        # 3. Compare all cards in reverse order as they are sorted.

        # First pair and second pair will only be a non-zero value if the card
        # type is either from the following:
        # 21: Four of a kind
        # 20: Full house
        # 17: Three of a kind
        # 16: Two pairs
        # 15: One pair
        if self._hand_type > other._hand_type:
            return "Win"
        elif self._hand_type < other._hand_type:
            return "Loss"
        elif self._first_pair == other._first_pair:
            if self._second_pair == other._second_pair:
                return self._compare_cards(other)
            else:
                return "Win" if self._second_pair > other._second_pair else "Loss"
        return "Win" if self._first_pair > other._first_pair else "Loss"

    def hand_name(self) -> str:
        """
        Return the name of the hand in the following format:
        'hand name, high card'

        Here are some examples:
        >>> PokerHand("KS AS TS QS JS").hand_name()
        'Royal flush'

        >>> PokerHand("2D 6D 3D 4D 5D").hand_name()
        'Straight flush, Six-high'

        >>> PokerHand("JC 6H JS JD JH").hand_name()
        'Four of a kind, Jacks'

        >>> PokerHand("3D 2H 3H 2C 2D").hand_name()
        'Full house, Twos over Threes'

        >>> PokerHand("2H 4D 3C AS 5S").hand_name()  # Low ace
        'Straight, Five-high'
        """
        name = PokerHand._HAND_NAME[self._hand_type - 14]
        high = PokerHand._CARD_NAME[self._high_card]
        pair1 = PokerHand._CARD_NAME[self._first_pair]
        pair2 = PokerHand._CARD_NAME[self._second_pair]
        if self._hand_type in [22, 19, 18]:
            return name + f", {high}-high"
        elif self._hand_type in [21, 17, 15]:
            return name + f", {pair1}s"
        elif self._hand_type in [20, 16]:
            join = "over" if self._hand_type == 20 else "and"
            return name + f", {pair1}s {join} {pair2}s"
        elif self._hand_type == 23:
            return name
        else:
            return name + f", {high}"

    def _compare_cards(self, other: PokerHand) -> str:
        # Comparing in reverse order as they're sorted
        for i in range(4, -1, -1):
            if self._cards[i][0] != other._cards[i][0]:
                return "Win" if self._cards[i][0] > other._cards[i][0] else "Loss"
        return "Tie"

    def _hand_type(self) -> int:
        # Number representing the type of hand internally:
        # 23: Royal flush (Why do I need this?)
        # 22: Straight flush
        # 21: Four of a kind
        # 20: Full house
        # 19: Flush
        # 18: Straight
        # 17: Three of a kind
        # 16: Two pairs
        # 15: One pair
        # 14: High card
        if self._is_flush():
            if self._is_five_high_straight() or self._is_straight():
                if self._hand_value == 60:
                    return 23
                else:
                    return 22
            return 19
        elif self._is_five_high_straight() or self._is_straight():
            return 18
        return 14 + self._is_same_kind()

    def _high_card(self) -> int:
        return self._cards[-1][0]

    def _total_hand_value(self) -> int:
        return sum(map(itemgetter(0), self._cards))

    def _is_flush(self) -> bool:
        suit = self._cards[0][-1]
        return all(map(lambda card: suit in card, self._cards))

    def _is_five_high_straight(self) -> bool:
        # If a card is a five high straight (low ace) change the location of
        # ace from the end of the list to the start. Check whether the last
        # element is ace or not. (Don't want to change again)
        if self._hand_value == 28:
            if self._cards[-1][0] == 14:
                ace_card = self._cards.pop()
                self._cards.insert(0, ace_card)
            return True
        return False

    def _is_straight(self) -> bool:
        for i in range(4):
            if self._cards[i + 1][0] - self._cards[i][0] != 1:
                return False
        return True

    def _is_same_kind(self) -> int:
        # Kind Values for internal use:
        # 7: Four of a kind
        # 6: Full house
        # 3: Three of a kind
        # 2: Two pairs
        # 1: One pair
        # 0: False
        kind = val1 = val2 = 0
        for i in range(4):
            if self._cards[i][0] == self._cards[i + 1][0]:
                if not val1:
                    val1 = self._cards[i][0]
                    kind += 1
                elif val1 == self._cards[i][0]:
                    kind += 2
                elif not val2:
                    val2 = self._cards[i][0]
                    kind += 1
                elif val2 == self._cards[i][0]:
                    kind += 2
        kind = kind + 2 if kind in [4, 5] else kind
        first = max(val1, val2)
        second = min(val1, val2)
        # If it's full house, make sure first pair is three count and if not
        # then switch them both.
        if kind == 6:
            values = list(map(itemgetter(0), self._cards))
            if values.count(first) != 3:
                first, second = second, first
        self._first_pair = first
        self._second_pair = second
        return kind

    def _internal_state(self) -> List[Tuple[int, str]]:
        # Internal representation of hand as a two tuple consisting of
        # the value and suit of the card.
        trans = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
        new_hand = self._hand.translate(str.maketrans(trans)).split()
        final_hand = [(int(card[:-1]), card[-1]) for card in new_hand]
        return sorted(final_hand)

    def __repr__(self):
        return f'{self.__class__}("{self._hand}")'

    def __str__(self):
        return self._hand

    # Rich comparison operators
    def __eq__(self, other):
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Tie"
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Loss"
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, PokerHand):
            return self < other or self == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, PokerHand):
            return not self < other and self != other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, PokerHand):
            return not self < other
        return NotImplemented

    def __hash__(self):
        return object.__hash__(self)
