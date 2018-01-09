from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class BaseModel(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
