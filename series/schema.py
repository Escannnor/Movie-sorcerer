from pydantic import BaseModel

class Series(BaseModel):
    title : str
    date : str
    season : str
    link : str
    country : str
    image: str
    rating: str