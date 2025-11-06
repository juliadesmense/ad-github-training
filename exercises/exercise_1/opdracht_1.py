def likes(team: list) -> str:
    if(len(team)==0):
        return "no one likes this"
    if(len(team)==1):
        return team[0] + " likes this"
    if(len(team)>1):
        return team[0]+" en "+team[1] +  " like this"