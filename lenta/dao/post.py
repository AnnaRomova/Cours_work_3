class Post:
    def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content= content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"{self.poster_name}, nummber is {self.pk}"