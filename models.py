from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the Restaurant, Customer, and Review models
# models.py

# ... (previous code for imports, base, and other classes)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define a relationship to connect Restaurant to Review
    reviews = relationship('Review', back_populates='restaurant')
    # Define a relationship to connect Restaurant to Customer through Review
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def all_reviews(self):
        if self.reviews:
            return [review.full_review() for review in self.reviews]
        else:
            return []

    @classmethod
    def fanciest(cls):
        # Find the restaurant with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define a relationship to connect Customer to Review
    reviews = relationship('Review', back_populates='customer')
    # Define a relationship to connect Customer to Restaurant through Review
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def favorite_restaurant(self):
        # Find the restaurant with the highest star rating for this customer
        highest_rating_review = max(self.reviews, key=lambda review: review.star_rating)
        return highest_rating_review.restaurant

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define relationships to connect Review to Restaurant and Customer
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.first_name} {self.customer.last_name}: {self.star_rating} stars."

# Create the database engine and create tables
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Testing the code
if __name__ == '__main__':
    # Create sample instances
    restaurant1 = Restaurant(name='Restaurant A', price=3)
    restaurant2 = Restaurant(name='Restaurant B', price=2)
    customer1 = Customer(first_name='John', last_name='Doe')
    customer2 = Customer(first_name='Jane', last_name='Smith')
    review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
    review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer1)
    review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)

    # Add instances to the session and commit
    session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
    session.commit()

    # Test the methods
    customer = session.query(Customer).first()
    print(f"{customer.first_name}'s favorite restaurant is: {customer.favorite_restaurant().name}")

    restaurant = session.query(Restaurant).first()
    print(f"Reviews for {restaurant.name}:")
    for review in restaurant.all_reviews():
        print(review)
