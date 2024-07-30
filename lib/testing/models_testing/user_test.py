import unittest
from lib.models import User, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class TestUser(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(engine)

    def test_create_user(self):
        user = User(username="testuser")
        self.session.add(user)
        self.session.commit()

        users = self.session.query(User).all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "testuser")

if __name__ == '__main__':
    unittest.main()
