"""
Person class.

Person:
    id_ -> string
    name -> string
"""


class Person():
    """Person class."""

    def __init__(self, name, id_):
        """Define init."""
        self.name = name
        self._id = id_

    @property
    def id_(self) -> str:
        """Get customer _id."""
        return self._id

    @id_.setter
    def id_(self, id_):
        """Set customer _id."""
        if id_:
            self._id = id_
        else:
            raise ValueError("Id can't be empty")

    def to_dict(self):
        """Transform data to a dict for saving in json file."""
        return {"id": self.id_, "name": self.name}
