from django.test import TestCase
from django.urls import reverse
from .models import Note

# Create your tests here.
class NoteModelTest(TestCase):
    """Tests for the Note model."""
    def setUp(self):
        """Create a test note."""
        Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

class NoteViewTest(TestCase):

    def setUp(self):
        """Create a test note for view tests."""
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'            )

    def test_note_list_view(self):
        """Test the note list view returns 200 and shows notes."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        """Test the note detail view shows correct note."""
        response = self.client.get(
            reverse('note_detail', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')



    def test_note_delete_view(self):
        """Test the delete shows confirmation."""
        response = self.client.get(
            reverse('note_delete', args=[self.note.id])
            )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete "Test Note"?')