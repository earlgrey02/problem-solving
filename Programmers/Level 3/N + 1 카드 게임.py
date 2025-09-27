def solution(coin, cards) -> int:
    def check_cards(*cards):
        for i in cards[0]:
            for j in cards[1]:
                if i + j == n + 1:
                    cards[0].remove(i)
                    cards[1].remove(j)

                    return True

        return False

    n = len(cards)
    hand_cards = [cards.pop(0) for _ in range(n // 3)]
    saved_cards = []
    answer = 1

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

        answer += 1

    return answer