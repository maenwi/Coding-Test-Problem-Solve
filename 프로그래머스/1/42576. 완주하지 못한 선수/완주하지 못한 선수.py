from collections import Counter

def solution(participant, completion):
    participant_dict = Counter(participant)
    completion_dict = Counter(completion)

    for person, num in participant_dict.items():
        if completion_dict[person] < num:
            return person
