from esmerald import Include, Gateway

from .controllers import ActorAPIView


route_patterns = [
    Gateway(handler=ActorAPIView)
]
