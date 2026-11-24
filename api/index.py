from flask import Flask, request

app = Flask(__name__)
pedidos = []
productos = [
    {"nombre": "Labial Matte", "precio": 120, "emoji": "💄"},
    {"nombre": "Base Liquida", "precio": 250, "emoji": "✨"},
    {"nombre": "Sombras Palette", "precio": 320, "emoji": "🎨"},
    {"nombre": "Rimel Volumen", "precio": 150, "emoji": "👁️"},
    {"nombre": "Rubor Rosado", "precio": 130, "emoji": "🌸"},
    {"nombre": "Kit Brochas", "precio": 280, "emoji": "🖌️"},
]

@app.route("/")
def home():
    cards = ""
    for p in productos:
        cards += f"""<div style="background:white;border-radius:20px;padding:20px;text-align:center;box-shadow:0 4px 15px #f8bbd0"><div style="font-size:50px">{p['emoji']}</div><h3>{p['nombre']}</h3><p style="color:#e91e63;font-weight:bold;font-size:20px">${p['precio']} MXN</p><form action="/pedir" method="post"><input type="hidden" name="producto" value="{p['nombre']}"><input name="cliente" placeholder="Tu nombre" required style="width:90%;padding:10px;border-radius:10px;border:1px solid #f8bbd0;margin:5px"><input name="telefono" placeholder="Tu WhatsApp" required style="width:90%;padding:10px;border-radius:10px;border:1px solid #f8bbd0;margin:5px"><button style="background:#e91e63;color:white;border:none;padding:12px 20px;border-radius:20px;width:95%;margin-top:5px;font-weight:bold">Pedir 💗</button></form></div>"""
    return f"""<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Selin Beauty</title></head><body style="font-family:Arial;background:#fff0f5;margin:0;padding:20px"><div style="text-align:center"><h1 style="color:#e91e63;font-size:35px">💗 Selin Beauty 💗</h1><p>Maquillaje bonito, barato y con amor</p><a href="/admin" style="background:#333;color:white;padding:10px 20px;border-radius:20px;text-decoration:none">Ver Pedidos Admin</a></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-top:20px">{cards}</div><p style="text-align:center;margin-top:30px">Pedidos: {len(pedidos)} | Torreon 💗</p></body></html>"""

@app.route("/pedir", methods=["POST"])
def pedir():
    pedidos.append({"producto": request.form.get("producto"), "cliente": request.form.get("cliente"), "telefono": request.form.get("telefono")})
    return f"""<html><body style="font-family:Arial;background:#fff0f5;text-align:center;padding:40px"><h1 style="color:#e91e63">Gracias {request.form.get('cliente')}! 💗</h1><p>Tu pedido de <b>{request.form.get('producto')}</b> fue recibido.</p><p>Te contactamos al {request.form.get('telefono')}</p><a href="/" style="background:#e91e63;color:white;padding:12px 25px;border-radius:20px;text-decoration:none">Volver a la tienda</a></body></html>"""

@app.route("/admin")
def admin():
    filas = "".join([f"<tr><td style='padding:10px;border:1px solid #ddd'>{p['cliente']}</td><td style='padding:10px;border:1px solid #ddd'>{p['telefono']}</td><td style='padding:10px;border:1px solid #ddd'>{p['producto']}</td></tr>" for p in pedidos])
    return f"""<html><body style="font-family:Arial;padding:20px;background:#fff0f5"><h1>Pedidos Selin Beauty 💗</h1><p>Total: {len(pedidos)}</p><table style="background:white;width:100%"><tr><th>Cliente</th><th>Telefono</th><th>Producto</th></tr>{filas}</table><br><a href="/">Volver</a></body></html>"""
