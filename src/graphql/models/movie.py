import strawberry
import datetime

from typing import Optional, List


@strawberry.type
class Movie:
    id: strawberry.ID
    filmtv_id: int
    original_title: str
    release_year: int
    genre: str
    duration_min: int
    avg_vote: float
    critics_vote: float
    public_vote: float
    description: Optional[str]
    notes: Optional[str]
    directors: List[str]
    countries: List[str]
    actors: List[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime


@strawberry.input
class MovieCreateInput:
    filmtv_id: int
    original_title: str
    release_year: int
    genre: str
    duration_min: int
    avg_vote: float
    critics_vote: float
    public_vote: float
    description: Optional[str]
    notes: Optional[str]
    directors: List[str]
    countries: List[str]
    actors: List[str]


@strawberry.type
class MovieAdded:
    id: strawberry.ID
    original_title: str
    message: str = "Movie added successfully."


@strawberry.type
class MovieNotFound:
    message: str = "Couldn't find user with the supplied id."


@strawberry.type
class MovieDeleted:
    message: str = "Movie deleted successfully."



