import pandas as pd


def plurality(preferences):
    result = {}  # creating a dictionary of pairs "candidate-votes"
    for preference in preferences:
        vote = str(preference)[0]
        result[vote] = result[vote] + 1 if vote in result.keys() else 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)  # sorting a dictionary
    return (result, result[0][0]) if result[0][1] != result[1][1] else (None, None)


def plurality_runoff(preferences):
    first_result, first_winner = plurality(preferences)  # first round
    if first_result[1][1] != first_result[2][1]:  # if not draw
        first_candidate, second_candidate = first_result[0][0], first_result[1][0]
        second_result = {first_candidate: 0, second_candidate: 0}
        for preference in preferences:  # checking who is more preferable
            if str(preference).find(first_candidate) < str(preference).find(second_candidate):
                second_result[first_candidate] = second_result[first_candidate] + 1
            else: second_result[second_candidate] = second_result[second_candidate] + 1
        second_result = sorted(second_result.items(), key=lambda x: x[1], reverse=True)  # sorting a dictionary
        return first_result, second_result, second_result[0][0]
    else: return None, None, None  # if draw


def condorcet_voting(preferences):
    candidates, result = sorted(list(str(preferences[0]))), {}
    relation = pd.DataFrame(columns=candidates, index=candidates)  # creating matrix of relations
    for candidate in candidates:  # filling the matrix
        relation[candidate][candidate] = 0
        opponents = candidates.copy()[candidates.index(candidate)+1:]
        for opponent in opponents:
            candidate_score = opponent_score = 0
            for preference in preferences:  # checking who is more preferable
                if str(preference).find(candidate) < str(preference).find(opponent): candidate_score += 1
                else: opponent_score += 1
            if candidate_score > opponent_score: relation[candidate][opponent], relation[opponent][candidate] = 1, 0
            elif candidate_score < opponent_score: relation[candidate][opponent], relation[opponent][candidate] = 0, 1
            else: relation[candidate][opponent], relation[opponent][candidate] = 0, 0
    for candidate in candidates:  # checking if there is there is a condorcet winner
        if sum(relation[candidate]) == len(candidates) - 1: return relation.transpose(), candidate
    return relation, None  # if no winner


def borda_voting(preferences):
    result = {}  # creating a dictionary of pairs "candidate-score"
    for preference in preferences:
        preference = str(preference)
        for candidate in preference:  # calculating the score of a candidate for the preference
            score = len(preference) - preference.index(candidate)
            result[candidate] = result[candidate] + score if candidate in result.keys() else score  # summing
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)  # sorting a dictionary
    return (result, result[0][0]) if result[0][1] != result[1][1] else (None, None)  # if not draw / draw
