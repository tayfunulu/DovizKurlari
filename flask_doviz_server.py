from flask import Flask, make_response, jsonify, request
from DovizKurlari import DovizKurlari

kurlar = DovizKurlari()

app = Flask(__name__)

@app.route('/api/doviz', methods=['GET', 'POST'])
def api_doviz():
    if request.method == "GET":
        return make_response(jsonify(kurlar.DegerSor()), 200)
    elif request.method == 'POST':
        content = request.json
        tarih= content['tarih']
        if "tur" in content:
          tur= content['tur']
          return make_response(jsonify(kurlar.Arsiv_tarih(tarih).get(tur.upper())), 201)  # 201 = ARSIV
        else:
          return make_response(jsonify(kurlar.Arsiv_tarih(tarih)), 201)  # 201 = ARSIV


@app.route('/api/doviz/<tur>', methods=['GET', 'POST'])
def api_her_doviz(tur):
    if request.method == "GET":
        Doviz_Value = kurlar.DegerSor().get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)
    elif request.method == "POST":  # Arsiv
        content = request.json
        tarih= content['tarih']
        Doviz_Value = kurlar.Arsiv_tarih(tarih).get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 201)
        else:
            return make_response(jsonify(Doviz_Value), 404)

@app.route('/api/doviz/<yil>/<ay>/<gun>', methods=['GET'])
def gun_ay_yil_api(yil,ay,gun):
    if request.method == "GET":
        Doviz_Value = kurlar.Arsiv(gun,ay,yil)
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)

@app.route('/api/doviz/<yil>/<ay>/<gun>/<tur>', methods=['GET'])
def gun_ay_yil_tur_api(yil,ay,gun,tur):
    if request.method == "GET":
        Doviz_Value = kurlar.Arsiv(gun,ay,yil).get(tur.upper())
        if Doviz_Value:
            return make_response(jsonify(Doviz_Value), 200)
        else:
            return make_response(jsonify(Doviz_Value), 404)



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")

