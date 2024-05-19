from esmerald import Include, Gateway

from src.middleware.jwt import JWTAuthMiddleware


route_patterns = [
    Include(
        path="/admin",
        routes=[
            Include(path="/categories", namespace="src.api.category.urls"),
            Include(path="/genres", namespace="src.api.genre.urls"),
            Include(path="/actors", namespace="src.api.actor.urls"),
        ],
        middleware=[JWTAuthMiddleware]
    ),

]
