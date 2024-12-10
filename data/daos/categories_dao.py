from typing import Optional

from data.db_utilities.session import CafeSession
from data.datamodel.categories import Categories


class CategoriesDao:
    def __init__(self, session=CafeSession.get_session()):
        self.session = session

    def create_category(self, category_name: str, description: Optional[str] = None):
        new_category = Categories(category_name=category_name, description=description)
        self.session.add(new_category)
        self.session.commit()

    def read_categories(self):
        return self.session.query(Categories).all()

    def delete_category(self, category_id):
        category = self.session.query(Categories).filter_by(id=category_id).first()
        if category:
            self.session.delete(category)
            self.session.commit()

    def update_category(
            self,
            category_id: int,
            category_name: Optional[str] = None,
            description: Optional[str] = None
    ):
        category = self.session.query(Categories).filter_by(id=category_id).first()
        if category:
            updates = {
                'category_name': category_name,
                'description': description
            }

            for key, value in updates.items():
                if value is not None:
                    setattr(category, key, value)

            self.session.commit()
