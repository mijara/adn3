def dayblock_to_adn2_format(day):
    """
    Transform the internal day-block representation to ADN2's representation:
    {block}{day}, both starting at 1.
    """
    day, block = day.split("-")
    return "{}{}".format(int(block) + 1, int(day) + 1)
