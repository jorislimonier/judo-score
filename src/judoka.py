class Judoka:
    def __init__(self, family_name, given_name, country, profile_url):
        self.family_name = family_name
        self.given_name = given_name
        self.country = country
        self.profile_url = profile_url


class Fight:
    def __init__(self, white, blue, competition, date, round_cat):
        self.white = white
        self.blue = blue
        self.competition = competition
        self.date = date
        self.round_cat = round_cat
        
