from flask import Flask, jsonify
import modelo
import datos

app = Flask(__name__)

@app.route('/predecir-motivo', methods=['GET'])
def predecir_motivo_api():
    datos_historicos = datos.obtener_datos_historicos()
    prediccion = modelo.predecir_motivo(datos_historicos)

    return jsonify({
        "mensaje": "Predicción para el próximo mes",
        "motivos": prediccion
    })

if __name__ == '__main__':
    app.run(debug=True)