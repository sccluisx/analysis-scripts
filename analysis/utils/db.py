from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from analysis import DATABASE


base = declarative_base()
engine = sa.create_engine('mysql+pymysql://root:root@localhost:8889/' + DATABASE)
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class IndividualReportModel(base):
    __tablename__ = 'individual_report'
    document_id = sa.Column(sa.String(30), primary_key=True)
    diagnostic = sa.Column(sa.Integer,nullable=False)
    locator = sa.Column(sa.String(4),nullable=False)
    session_id = sa.Column(sa.String(50),nullable=False)
    timestamp = sa.Column(sa.BigInteger, nullable=False)
    symptoms = sa.Column(sa.String(255))
    analysis_done = sa.Column(sa.Boolean,nullable=False)

    def __repr__(self):
        return '<Indiv. report: NPA ' + self.locator + ' time ' + str(self.timestamp) + '>'


class DailyDiagnosticChangeModel(base):
    __tablename__ = 'daily_diagnostic_change' #<- must declare name for db table
    id = sa.Column(sa.Integer, primary_key=True,autoincrement=True)
    locator = sa.Column(sa.String(4))
    year = sa.Column(sa.Integer)
    month = sa.Column(sa.Integer)
    day = sa.Column(sa.Integer)
    diagnostic_0 = sa.Column(sa.Integer, default=0)
    diagnostic_1 = sa.Column(sa.Integer, default=0)
    diagnostic_2 = sa.Column(sa.Integer, default=0)
    diagnostic_3 = sa.Column(sa.Integer, default=0)
    diagnostic_4 = sa.Column(sa.Integer, default=0)
    diagnostic_5 = sa.Column(sa.Integer, default=0)

    def __repr__(self):
        d = str(self.year) + '-' + str(self.month) + '-' + str(self.day)
        change = [
            self.diagnostic_0,
            self.diagnostic_1,
            self.diagnostic_2,
            self.diagnostic_3,
            self.diagnostic_4,
        ]
        return '<DailyChang: NPA ' + self.locator + ' ' + d + ' ' + str(change) + '>'


class LocationModel(base):
    __tablename__ = 'location'
    npa = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    state = sa.Column(sa.String(2))  # canton
    town = sa.Column(sa.String(100))
    longitude = sa.Column(sa.Float)
    latitude = sa.Column(sa.Float)

    def __repr__(self):
        return '<Location: NPA ' + self.npa + ' state ' + str(self.state) + '>'


def init_db():
    base.metadata.create_all()


if __name__ == '__main__':
    init_db()
