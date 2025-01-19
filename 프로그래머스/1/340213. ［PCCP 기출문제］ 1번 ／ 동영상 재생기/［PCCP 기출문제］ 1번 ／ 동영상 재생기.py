def solution(video_len, pos, op_start, op_end, commands):
    
    def convert_to_sec(t):
        temp = t.split(":")
        return int(temp[0]) * 60 + int(temp[1])
    
    def convert_to_time(sec):
        m = sec // 60
        m = f"{m}" if m >= 10 else f"0{m}"
        
        s = sec % 60
        s = f"{s}" if s >= 10 else f"0{s}"
        return f"{m}:{s}"
    
    v = convert_to_sec(video_len)
    current = convert_to_sec(pos)
    ops = convert_to_sec(op_start)
    ope = convert_to_sec(op_end)
    
    def i_am_in_op(ops, ope, t):
        if ops <= t <= ope:
            return True
        return False
        
    for c in commands:
        if i_am_in_op(ops, ope, current):
            current = ope
        # 내가 오프닝 사이에 있다면, 오프닝 끝으로 날 옮겨줘
        
        if c == "prev":
            current = max([current - 10, 0])
        
        else:
            current = min([current + 10, v])
    
    if i_am_in_op(ops, ope, current):
        current = ope
    # 내가 오프닝 사이에 있다면, 오프닝 끝으로 날 옮겨줘

    return convert_to_time(current)