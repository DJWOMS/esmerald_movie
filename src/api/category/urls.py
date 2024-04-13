from esmerald import Include, Gateway

from .controllers import CategoryAPIView


route_patterns = [
    Gateway(handler=CategoryAPIView)
]
