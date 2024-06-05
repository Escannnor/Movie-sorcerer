from fastapi import FastAPI
from schemas import Series 
from session import add_series, get_all_series

app = FastAPI()

@app.get("/all")
def all():
    movies = get_all_movies()
    if not movies:
        return {"message": "No results"}
    return movies


@app.post("/add-movie")
def add(movie: Series):
    return add_movie(movie.name, movie.image, movie.year, movie.url)
=======
@app.post("/add-movie")
def add(movie: International):
    return add_movie(movie.name, movie.image, movie.date, movie.download_link, movie.description)
>>>>>>> fee12de0364577e628246ca81e393e8958d265cf
    