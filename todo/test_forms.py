from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # python3 manage.py tests todo.test_forms
    # python3 manage.py tests todo.test_forms.TestItemForm #class
    # python3 manage.py tests todo.test_forms.TestItemForm.test_item_name_is_required

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test ToDo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
