movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_imdb_above_5_5():
    movie_name = str(input("Choose movie from dictionary: "))
    for movie in movies:
        if movie["name"].lower() == movie_name.lower():
            imdb_score = movie["imdb"]
    if imdb_score > 5.5:
        return True
    return False

def sublist_imdb():
    sublist = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            sublist.append(movie["name"])
    return sublist

def movie_by_category():
    category = str(input("Enter category: "))
    for movie in movies:
        if movie["category"].lower() == category.lower():
            print(movie["name"])

def avg_imdb():
    movie_list = list(map(str.strip, input("Enter movie names (comma-separated): ").split(",")))
    total_score = 0
    count = 0
    for x in movie_list:
        for movie in movies:
            if movie["name"].lower() == x.lower():
                total_score += movie["imdb"]
                count += 1
    print("Average IMDB score by movies name:", total_score/count)

def avg_by_category():
    category = str(input("Enter category: "))
    total_score = 0
    count = 0
    for movie in movies:
        if movie["category"].lower() == category.lower():
            total_score += movie["imdb"]
            count += 1
    print("Average IMDB score by category:", total_score/count)

if is_imdb_above_5_5():
    print("Yes, imdb of this movie is above 5.5 \n")
else:
    print("No, imdb of this movie is not above 5.5 \n")

print(sublist_imdb(), "\n")

movie_by_category()

avg_imdb()

avg_by_category()

