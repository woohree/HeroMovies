# movies
class Genre:
    name = models.CharField(max_length=50)

class Movie:
    genres = ManyToMany(Genre, rel_name="movies")
    
    # 그 외 데이터들

class Review:
    user = FK(User)
    llke_users = MTM(User, rel_name="like_reviews")
    movie = FK(Movie)
    # 그 외

class ReviewComment:
    user = FK(User)
    review = FK(Review)
    like_users = MTM(User, rel_name="like_review_comments")
    # 그 외


# accounts
class User:
    following = MTM(User, syme=True)

    # 추천 데이터
    choose_movies = MTM(Movie, rel_name="chosen_users")
    
    # 평점 수정
    update_movies = MTM(Movie, rel_name="update_users")


# community
class Article:
    user = FK(User)
    good = MTM(User, rel_name="good_articles")
    bad = MTM(User, rel_name="bad_articles")
    # 그 외

class AriticleComment:
    user = FK(User)
    article = FK(Article)
    # 그 외

class CommentComment:
    user = FK(User)
    comment = FK(Comment)
    # 그 외