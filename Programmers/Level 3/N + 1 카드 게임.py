def solution(coin: int, cards: list[int]) -> int:
    def check_cards(cards_1: list[int], cards_2: list[int]) -> bool:
        for i in cards_1:
            for j in cards_2:
                if i + j == n + 1:
                    cards_1.remove(i)
                    cards_2.remove(j)

                    return True

        return False

    n = len(cards)
    round = 1
    hand_cards = [cards.pop(0) for _ in range(n // 3)]
    saved_cards = []

    while coin >= 0 and cards:
        saved_cards.extend(cards.pop(0) for _ in range(2))

        if check_cards(hand_cards, hand_cards):
            pass
        elif coin >= 1 and check_cards(hand_cards, saved_cards):
            coin -= 1
        elif coin >= 2 and check_cards(saved_cards, saved_cards):
            coin -= 2
        else:
            break

        round += 1

    answer = round

    return answer
