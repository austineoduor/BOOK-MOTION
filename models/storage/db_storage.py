#!/usr/bin/python3
""" new class for sqlAlchemy """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from models.user import User
from models.book import Book
from models.book_recommended import Recommended
from models.bookmotion_base import BookMotionBase, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


classes = {"Book": Book,"Recommended": Recommended, "User": User}
class DBStorage:
    """ create tables in environmental"""
    def __init__(self):
        self.__session = None
        self._engine = create_engine('sqlite:///Storage.db', pool_pre_ping=True)
        #Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        
    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def all(self, cls: str = None):
        """
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self._session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [User, Book, Recommended]
            for clase in lista:
                query = self._session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    '''def new(self, obj):
        """add a new element in the table
        """
        self._session.add(obj)
    '''

    def save(self, obj=None) -> None:
        """save changes
        """
        if obj:
            self._session.add(obj)
            self._session.commit()
        else:
            self._session.commit()

    def delete(self, obj=None) ->None:
        """delete an element in the table
        """
        if obj:
            self._session.delete(obj)

    def reload(self) -> None:
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self._session = Session()

    def close(self) -> None:
        """ calls remove()
        """
        self._session.close()

    def get(self, cls: str, _id: str) -> User:
        """Retrievs one objet of a class"""
        if not cls and not _id:
            raise InvalidRequestError
        try:
            user = self._session.query(classes[cls]).all()
        except InvalidRequestError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        else:
            for i in user:
                if i.id ==_id:
                    return i

    def count(self, cls: str = None) -> dict:
        """
        Returns the number of objects in storage matching the given class name.
        If no name is passed, returns the count of all objects in storage.
        """
        nobjects = 0
        if cls in classes:
            nobjects += len(self._session.query(classes[cls]).all())
        else:
            return 'No class with the name {}'.format(cls)
        return nobjects
