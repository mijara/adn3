def get_first_available(sessions):
    last = 1
    for s in sessions:
        if s.number > last + 1:
            return last + 1
        last = s.number

    return len(sessions) + 1
