class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.rating_times = 0
        self.rates = 0
    def __str__(self):
        self.genre_string = ", ".join(self.genres)
        if self.rating_times > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genre_string}\n{self.rating_times} ratings, average {self.rates_rounded} points"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genre_string}\nno ratings"
    def rate(self, rt: int):
        self.ratings.append(rt)
        self.rating_times += 1
        self.rates = sum(self.ratings) / self.rating_times
        self.rates_rounded = format(self.rates,'.1f')
        return self.rates

def minimum_grade(rating: float, series_list: list):
    qualified_series = []
    for item in series_list:
        if item.rates >= rating:
            qualified_series.append(item)
    return qualified_series

def includes_genre(genre: str, series_list: list):
    qualified_genres = []
    for item in series_list:
        if genre in item.genres:
            qualified_genres.append(item)
    return qualified_genres


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)
    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
