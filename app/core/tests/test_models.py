from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test226@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_user2(email='test227@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_user3(email='test228@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'pars@PARS.com'
        user = get_user_model().objects.create_user(email, 'Pars123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Pars123456')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'bakhshi.r@gmail.com',
            '6162'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

        def test_ingredient_str(self):
            """Test the ingredient string respresentation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user2(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

        def test_recipe_str(self):
            """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user3(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)

        # @patch('uuid.uuid4')
        # def test_recipe_file_name_uuid(self, mock_uuid):
        #     """Test that image is saved in the correct location"""
        # uuid = 'test-uuid'
        # mock_uuid.return_value = uuid
        # file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        # exp_path = f'uploads/recipe/{uuid}.jpg'
        # self.assertEqual(file_path, exp_path)
