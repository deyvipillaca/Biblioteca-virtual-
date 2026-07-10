from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    imagen = db.Column(db.String(300), nullable=True)
    archivo_pdf = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Libro {self.titulo}>'


@app.route('/')
def index():
    libros = Libro.query.all()
    return render_template('index.html', libros=libros)


@app.route('/login')
def login():
    return "Pagina de login (pendiente)"


def cargar_libros_iniciales():
    if Libro.query.count() == 0:
        libros_ejemplo = [
            Libro(titulo="El Patito Feo", autor="Hans C. Andersen", categoria="Educacion", imagen="https://picsum.photos/300/400?10", archivo_pdf="patitofeo.pdf"),
            Libro(titulo="Cuentos de Casa", autor="Varios Autores", categoria="Educacion", imagen="https://picsum.photos/300/400?11", archivo_pdf="CUENTOSCASA.pdf"),
            Libro(titulo="101 Cuentos Emocionantes", autor="Varios Autores", categoria="Educacion", imagen="https://picsum.photos/300/400?12", archivo_pdf="9788469885772-libros-regalo-101-cuentos-emocionantes.pdf"),
            Libro(titulo="Cuentos que Cuidan", autor="Varios Autores", categoria="Educacion", imagen="https://picsum.photos/300/400?13", archivo_pdf="Cuentos que cuidan.pdf"),
            Libro(titulo="Cuentos Cortos con Comprension Lectora", autor="Varios Autores", categoria="Educacion", imagen="https://picsum.photos/300/400?14", archivo_pdf="Cuadernillo-de-cuentos-cortos-y-lecturas-para-en-PDF-con-comprension-lectora.pdf"),
            Libro(titulo="Cuentos", autor="Varios Autores", categoria="Educacion", imagen="https://picsum.photos/300/400?15", archivo_pdf="Cuentos.pdf"),
        ]
        db.session.add_all(libros_ejemplo)
        db.session.commit()
        print("Libros agregados correctamente.")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_libros_iniciales()

    app.run(debug=True)