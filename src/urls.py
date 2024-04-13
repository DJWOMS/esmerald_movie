from esmerald import Include, Gateway

route_patterns = [
    Include(path="/admin", routes=[
        Include(path="/categories", namespace="src.api.category.urls"),
    ]),
]
