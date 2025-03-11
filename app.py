from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creditos.db'
db = SQLAlchemy(app)

class Credito(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(10), nullable=False)

@app.route('/creditos', methods=['POST'])
def agregar_credito():
    data = request.json
    nuevo_credito = Credito(**data)
    db.session.add(nuevo_credito)
    db.session.commit()
    return jsonify({'message': 'Crédito agregado'}), 201

@app.route('/creditos', methods=['GET'])
def listar_creditos():
    creditos = Credito.query.all()
    return jsonify([credito.as_dict() for credito in creditos])

@app.route('/creditos/<int:id>', methods=['PUT'])
def editar_credito(id):
    data = request.json
    credito = Credito.query.get(id)
    if credito:
        for key, value in data.items():
            setattr(credito, key, value)
        db.session.commit()
        return jsonify({'message': 'Crédito actualizado'})
    return jsonify({'message': 'Crédito no encontrado'}), 404

@app.route('/creditos/<int:id>', methods=['DELETE'])
def eliminar_credito(id):
    credito = Credito.query.get(id)
    if credito:
        db.session.delete(credito)
        db.session.commit()
        return jsonify({'message': 'Crédito eliminado'})
    return jsonify({'message': 'Crédito no encontrado'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)