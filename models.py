from sqlalchemy import Column, String, BigInteger

from db import db

# Model for allergies table
class Allergies(db.Model):
    __tablename__ = 'allergies'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    START = Column(String(10))
    STOP = Column(String(50))
    PATIENT = Column(String(50), nullable=False)
    ENCOUNTER = Column(String(50))
    CODE = Column(BigInteger)
    SYSTEM1 = Column(String(20))
    DESCRIPTION = Column(String(50))
    TYPE = Column(String(50))
    CATEGORY = Column(String(50))
    DESCRIPTION1 = Column(String(50))
    SEVERITY1 = Column(String(50))
    DESCRIPTION2 = Column(String(50))
    SEVERITY2 = Column(String(50))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for careplans table
class CarePlans(db.Model):
    __tablename__ = 'careplans'
    Id = Column(String(50), primary_key=True)
    START = Column(String(50))
    STOP = Column(String(50))
    PATIENT = Column(String(50))
    ENCOUNTER = Column(String(50))
    CODE = Column(BigInteger)
    DESCRIPTION = Column(String(250))
    REASONCODE = Column(String(50))
    REASONDESCRIPTION = Column(String(250))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for claims_transactions table
class ClaimsTransactions(db.Model):
    __tablename__ = 'claims_transactions'
    ID = Column(String(50), primary_key=True)
    CLAIMID = Column(String(50))
    CHARGEID = Column(String(50))
    PATIENTID = Column(String(50))
    TYPE = Column(String(50))
    AMOUNT = Column(String(50))
    METHOD = Column(String(50))
    FROMDATE = Column(String(50))
    TODATE = Column(String(50))
    PLACEOFSERVICE = Column(String(50))
    PROCEDURECODE = Column(String(50))
    DEPARTMENTID = Column(String(50))
    NOTES = Column(String(250))
    UNITAMOUNT = Column(String(50))
    TRANSFEROUTID = Column(String(50))
    TRANSFERTYPE = Column(String(50))
    PAYMENTS = Column(String(50))
    TRANSFERS = Column(String(50))
    OUTSTANDING = Column(String(50))
    APPOINTMENTID = Column(String(50))
    LINENOTE = Column(String(50))
    PATIENTINSURANCEID = Column(String(50))
    PROVIDERID = Column(String(50))
    SUPERVISINGPROVIDERID = Column(String(50))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}


# Model for conditions table
class Conditions(db.Model):
    __tablename__ = 'conditions'
    ENCOUNTER = Column(String(50), primary_key=True)
    START = Column(String(50))
    STOP = Column(String(50))
    PATIENT = Column(String(50))
    CODE = Column(String(50))
    DESCRIPTION = Column(String(150))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for encounters table
class Encounters(db.Model):
    __tablename__ = 'encounters'
    Id = Column(String(50), primary_key=True)
    START = Column(String(50))
    STOP = Column(String(50))
    PATIENT = Column(String(50))
    ORGANIZATION = Column(String(50))
    PROVIDER = Column(String(50))
    PAYER = Column(String(50))
    ENCOUNTERCLASS = Column(String(50))
    CODE = Column(String(10))
    DESCRIPTION = Column(String(150))
    db.Model_ENCOUNTER_COST = Column(String(50))
    TOTAL_CLAIM_COST = Column(String(50))
    PAYER_COVERAGE = Column(String(50))
    REASONCODE = Column(String(50))
    REASONDESCRIPTION = Column(String(150))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for immunizations table
class Immunizations(db.Model):
    __tablename__ = 'immunizations'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    DATE = Column(String(20))
    PATIENT = Column(String(50), nullable=False)
    ENCOUNTER = Column(String(50))
    CODE = Column(String(20))
    DESCRIPTION = Column(String(250))
    db.Model_COST = Column(String(20))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for medications table
class Medications(db.Model):
    __tablename__ = 'medications'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    START = Column(String(20))
    STOP = Column(String(20))
    PATIENT = Column(String(50))
    PAYER = Column(String(50))
    ENCOUNTER = Column(String(50))
    CODE = Column(String(20))
    DESCRIPTION = Column(String(250))
    db.Model_COST = Column(String(20))
    PAYER_COVERAGE = Column(String(20))
    DISPENSES = Column(String(20))
    TOTALCOST = Column(String(20))
    REASONCODE = Column(String(20))
    REASONDESCRIPTION = Column(String(150))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for observations table
class Observations(db.Model):
    __tablename__ = 'observations'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    DATE = Column(String(20))
    PATIENT = Column(String(50))
    ENCOUNTER = Column(String(50))
    CATEGORY = Column(String(20))
    CODE = Column(String(20))
    DESCRIPTION = Column(String(250))
    VALUE = Column(String(150))
    UNITS = Column(String(50))
    TYPE = Column(String(15))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for organizations table
class Organizations(db.Model):
    __tablename__ = 'organizations'
    Id = Column(String(50), primary_key=True)
    NAME = Column(String(100))
    ADDRESS = Column(String(50))
    CITY = Column(String(50))
    STATE = Column(String(10))
    ZIP = Column(String(20))
    LAT = Column(String(20))
    LON = Column(String(20))
    PHONE = Column(String(50))
    REVENUE = Column(String(20))
    UTILIZATION = Column(String(20))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for patients table
class Patients(db.Model):
    __tablename__ = 'patients'
    Id = Column(String(50), primary_key=True)
    BIRTHDATE = Column(String(50))
    DEATHDATE = Column(String(50))
    SSN = Column(String(20))
    DRIVERS = Column(String(20))
    PASSPORT = Column(String(20))
    PREFIX = Column(String(10))
    FIRST = Column(String(20))
    LAST = Column(String(20))
    SUFFIX = Column(String(10))
    MAIDEN = Column(String(20))
    MARITAL = Column(String(5))
    RACE = Column(String(10))
    ETHNICITY = Column(String(20))
    GENDER = Column(String(5))
    BIRTHPLACE = Column(String(100))
    ADDRESS = Column(String(50))
    CITY = Column(String(50))
    STATE = Column(String(50))
    COUNTY = Column(String(50))
    ZIP = Column(String(20))
    LAT = Column(String(20))
    LON = Column(String(20))
    HEALTHCARE_EXPENSES = Column(String(20))
    HEALTHCARE_COVERAGE = Column(String(20))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for procedures table
class Procedures(db.Model):
    __tablename__ = 'procedures'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    START = Column(String(20))
    STOP = Column(String(20))
    PATIENT = Column(String(50))
    ENCOUNTER = Column(String(50))
    CODE = Column(String(20))
    DESCRIPTION = Column(String(250))
    db.Model_COST = Column(String(20))
    REASONCODE = Column(String(20))
    REASONDESCRIPTION = Column(String(150))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for providers table
class Providers(db.Model):
    __tablename__ = 'providers'
    Id = Column(String(50), primary_key=True)
    ORGANIZATION = Column(String(50))
    NAME = Column(String(50))
    GENDER = Column(String(5))
    SPECIALITY = Column(String(50))
    ADDRESS = Column(String(50))
    CITY = Column(String(20))
    STATE = Column(String(5))
    ZIP = Column(String(20))
    LAT = Column(String(20))
    LON = Column(String(20))
    UTILIZATION = Column(String(20))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}

# Model for supplies table
class Supplies(db.Model):
    __tablename__ = 'supplies'
    ID = Column(BigInteger, primary_key=True, autoincrement=True)
    DATE = Column(String(20))
    PATIENT = Column(String(50))
    ENCOUNTER = Column(String(50))
    CODE = Column(String(20))
    DESCRIPTION = Column(String(250))
    QUANTITY = Column(String(20))

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key != '_sa_instance_state'}
