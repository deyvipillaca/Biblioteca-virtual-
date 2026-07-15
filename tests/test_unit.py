import unittest
from app import app, db, Libro  # Importamos la app, la BD y tu clase de modelo Libro

class TestBibliotecaUnit(unittest.TestCase):

    def setUp(self):
        """Configuración de un entorno aislado e independiente antes de cada test"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # BD limpia en memoria
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Destrucción y limpieza del entorno al finalizar el test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_libro_modelo(self):
        """Prueba unitaria: Verifica que un objeto Libro instancie sus campos correctamente"""
        # 1. Instanciamos un libro de prueba con todos los campos obligatorios
        nuevo_libro = Libro(
            titulo="Cien años de soledad", 
            autor="Gabriel García Márquez", 
            categoria="Literatura",
            imagen="https://picsum.photos",  # Enlace de imagen ficticio con dimensiones corregidas
            archivo_pdf="cien_anos_soledad.pdf"       # Nombre de archivo ficticio requerido
        )

        # 2. Guardamos de forma aislada en la base de datos temporal
        db.session.add(nuevo_libro)
        db.session.commit()

        # 3. Lo buscamos para validar que sus atributos coincidan exactamente
        libro_guardado = Libro.query.filter_by(titulo="Cien años de soledad").first()
        self.assertIsNotNone(libro_guardado)
        self.assertEqual(libro_guardado.autor, "Gabriel García Márquez")
        self.assertEqual(libro_guardado.categoria, "Literatura")

if __name__ == '__main__':
    unittest.main()
