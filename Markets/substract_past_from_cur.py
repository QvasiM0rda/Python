def substract_past_from_cur(current: dict, past: dict) -> dict:
    result = dict()
    for key, value in current.items():
        total = current[key]
        if key in past.keys():
            total -= past[key]

        if total / 1000 >= 0.5:
            result[key] = int(round(total / 1000, 0))
            
    return result
