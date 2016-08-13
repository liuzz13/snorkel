from .meta import SnorkelBase
from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref


class Feature(SnorkelBase):
    """A feature that Candidate."""
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidate.id'), nullable=False)
    candidate = relationship('Candidate', backref=backref('features', cascade='all, delete-orphan', cascade_backrefs=False))
    name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(candidate_id, name),
    )

    def __eq__(self, other):
        try:
            return self.candidate == other.candidate \
                   and self.candidate.set == other.candidate.set \
                   and self.name == other.name
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Feature (" + str(self.name) + " on " + str(self.candidate) + ")"
