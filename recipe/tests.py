from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Dessert")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            category=self.category,
            description="Delicious chocolate cake"
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
        self.assertTemplateUsed(response, 'recipe/main.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)
        self.assertTemplateUsed(response, 'recipe/category_list.html')
