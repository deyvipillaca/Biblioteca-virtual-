import unittest
from app import app, db  # Importamos tu aplicación y base de datos

class TestBibliotecaIntegration(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        # Configuramos Flask en modo de pruebas
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos temporal en memoria
        self.client = app.test_client()
        
        # Inicializamos la base de datos de prueba
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Limpieza después de terminar cada prueba"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page_status_code(self):
        """Prueba de integración: Verifica que la página de inicio cargue correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_static_css_loading(self):
        """Prueba de integración: Verifica que los estilos CSS respondan correctamente"""
        response = self.client.get('/static/css/estilos.css')
        # Puede devolver 200 o 304 si ya está en caché
        self.assertIn(response.status_code, [200, 304])

if __name__ == '__main__':
    unittest.main()
