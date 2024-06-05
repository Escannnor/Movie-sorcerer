from sqlmodel import Session, select
from engine import engine
from models.series import Series

def add_series(title, date, season, link, country, image, rating):
    try:
        with Session(engine) as session:
            series = Series(title=title, date=date, season=season, link=link, country=country, image=image, rating=rating)
            session.add(series)
            session.commit()
            return 'Series added to database'
    except Exception as e:
            return f'Error in adding series {e}'
        
def get_series():
    with Session(engine) as session:
        series = select(Series)
        results = session.exec(series)
        for result in results:
            print(result)
            return result
        return 'No results'
    

def update_series(id,title=None, date=None, season=None, link=None, country=None, image=None, rating=None ):
    try:
        with Session(engine) as session:
            series = session.get(Series, id)
            if Series:
                if title is not None:
                    series.title = title
                elif date is not None:
                    series.date = date
                elif season is not None:
                    series.season = season
                elif link is not None:
                    series.link = link
                elif country is not None:
                    series.country = country
                elif image is not None:
                    series.image = image
                elif rating is not None:
                    series.rating = rating
                else:
                    return 'Field is not found'
                session.commit()
                return f'Series with id {id} updated'
            else:
                return f'No series found with id {id}'
    except Exception as e:
        return f'Error in updating Series {e}'
def delete_series(id):
    with Session(engine) as session:
        series = session.get(Series, id)
        session.delete(series)
        session.commit()
        return f'{series} deleted'
        