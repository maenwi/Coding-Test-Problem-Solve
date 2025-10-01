def solution(data, ext, val_ext, sort_by):
    columns = ["code", "date", "maximum", "remain"]
    filter_idx = columns.index(ext)
    sort_idx = columns.index(sort_by)

    answer = []

    for a_data in data:
        if a_data[filter_idx] < val_ext:
            answer.append(a_data)

    answer.sort(key = lambda a_data: a_data[sort_idx])

    return answer