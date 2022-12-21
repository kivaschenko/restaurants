from django.test import TestCase
from django.contrib.auth.models import User
from .models import Restaurant, Menu


class MenuTests(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()
        
        restaurant_1 = Restaurant.objects.create(
            admin=testuser1, 
            short_name='Barbar Restaurants', 
            full_name='Barbar Restaurants',
            description='''
            Offers
                There are vegetarian dishes
                Appetizer
                Healthy food
                You can have a quick snack
                Late dinners
                Halal food
            ''',
            lng=33.89480139, lat=35.48331668,
            address='Hamra - PIccadilly Street, Lebanon'
        )
        restaurant_1.save()
        
        menu_1 = Menu.objects.create(
            restaurant=restaurant_1,
            body='''
                Dish 1
                Dish 2
                Desert
                Juice
                Price: 10.00
            ''',
            actual_date='2022-12-21',
            votes=0,
        )
        menu_1.save()
        
    def test_menu_content(self):
        menu = Menu.objects.get(id=1)
        restaurant = f'{menu.restaurant}'
        body = f'{menu.body}'
        actual_date = f'{menu.actual_date}'
        votes = menu.votes
        self.assertEqual(restaurant, 'Barbar Restaurants')
        self.assertEqual(
            body, 
            '''
                Dish 1
                Dish 2
                Desert
                Juice
                Price: 10.00
            '''
        )
        self.assertEqual(actual_date, '2022-12-21')
        self.assertEqual(votes, 0)