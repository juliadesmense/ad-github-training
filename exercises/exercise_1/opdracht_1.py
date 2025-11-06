def likes(team: list) -> str:
    if not team:
        return "no one likes this"

    if len(team) == 1:
        return f"{team[0]} likes this"

    # Als er meer dan één naam is, maak een mooie string:
    names = ", ".join(team[:-1]) + f" and {team[-1]}"
    return f"{names} like this"
