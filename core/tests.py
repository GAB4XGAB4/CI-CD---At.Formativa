from django.test import TestCase
from .models import Note
from django.urls import reverse

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Teste 1", content="Conteúdo do teste 1")

    # Teste 1: Verifica se a nota foi criada corretamente
    def test_note_creation(self):
        self.assertEqual(self.note.title, "Teste 1")
        self.assertEqual(self.note.content, "Conteúdo do teste 1")

    # Teste 2: Verifica a representação em string do modelo
    def test_note_str_representation(self):
        self.assertEqual(str(self.note), "Teste 1")

class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Teste View", content="Conteúdo view")
        self.url = reverse('home') # Vamos precisar criar essa rota

    # Teste 3: Verifica se a view retorna status 200 (OK)
    def test_home_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    # Teste 4: Verifica se a view usa o template correto
    def test_home_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/home.html')

    # Teste 5: Verifica se o contexto contém a nota criada
    def test_home_view_context(self):
        response = self.client.get(self.url)
        self.assertIn('notes', response.context)
        self.assertEqual(response.context['notes'][0].title, "Teste View")
