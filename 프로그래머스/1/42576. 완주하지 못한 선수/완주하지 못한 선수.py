def handle_dup(people):
    appear = {}
    dup_handled_people = set()
    for person in people:
        try:
            appear[person] += 1
        except:
            appear[person] = 1
        dup_handled_people.add(f"{person}_{appear[person]}")
    
    return dup_handled_people
        
def solution(participant, completion):
    d_p = handle_dup(participant)
    c_p = handle_dup(completion)
    
    still_running = list(d_p.difference(c_p))
    
    return still_running[0].split("_")[0]