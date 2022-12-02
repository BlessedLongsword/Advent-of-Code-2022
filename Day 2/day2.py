PLAY_SCORE = {'A': 1, 'B': 2, 'C': 3}
CORRESPONDING = {'X': 'A', 'Y': 'B', 'Z': 'C'}
WIN_SCENARIO = {'A': 'B', 'B': 'C', 'C': 'A'}

RESULT_SCORE = {'X': 0, 'Y': 3, 'Z': 6}


def get_guide(strategy_guide):
    return list(map(lambda x: tuple(x.split(' ')), [line.rstrip() for line in open(strategy_guide, 'r').readlines()]))


def evaluate_game(game):
    if CORRESPONDING[game[1]] is WIN_SCENARIO[game[0]]:
        return PLAY_SCORE[CORRESPONDING[game[1]]] + 6
    elif CORRESPONDING[game[1]] is game[0]:
        return PLAY_SCORE[CORRESPONDING[game[1]]] + 3
    return PLAY_SCORE[CORRESPONDING[game[1]]]


def exercise1(file):
    strategy_guide = get_guide(file)
    return sum(evaluate_game(game) for game in strategy_guide)


def exercise2(file):
    strategy_guide = get_guide(file)
    total_score = 0

    lose_scenario = dict((v, k) for k, v in WIN_SCENARIO.items())

    for play, result in strategy_guide:
        if result == 'X':
            total_score += PLAY_SCORE[lose_scenario[play]]
        elif result == 'Y':
            total_score += PLAY_SCORE[play]
        else:
            total_score += PLAY_SCORE[WIN_SCENARIO[play]]
        total_score += RESULT_SCORE[result]

    return total_score


print('The total score would be', exercise1('input.txt'), 'points.')
print('The total score would be', exercise2('input.txt'), 'points.')

