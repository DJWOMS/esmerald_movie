"""
Generated by 'esmerald createapp' using Esmerald 3.1.2.
"""
from esmerald import Include, Gateway

# Create your routes here.

from .controllers import GenreAPIView


route_patterns = [
    Gateway(handler=GenreAPIView)
]
