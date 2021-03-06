from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class BaseModel(object):
    @property
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
