from flask import Flask, request

app = Flask(__name__)
pedidos = []
productos = [
{"nombre":"Labial Matte","precio":120,"foto":"https://adn-static3.nykaa.com/media/catalog/product/6/9/6902395681427.jpg"},
{"nombre":"Base liquida","precio":250,"foto":"https://images.shop.frankfurt-airport.com/pim/defaults/862x,webp/catalog/4/4/7/d/447d26e8375ffafe9b014a3810ed0a9f_1132595.jpg"},
{"nombre":"Sombras Palette","precio":300,"foto":"https://images-static.nykaa.com/media/catalog/product/9/f/9f32d63MACXX00001232_1.jpg"},
{"nombre":"Rimel Volumen","precio":150,"foto":"https://i.pinimg.com/originals/df/ad/f2/dfadf2dd15c4f8a1663339890e006940.webp"},
{"nombre":"Rubor Rosado","precio":130,"foto:"https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600
{"nombre":"Kit Brochas","precio":280,"foto":"https://m.media-amazon.com/images/S/aplus-media-library-service-media/db148df3-2612-4dbd-9d23-f3d38d15f950.__CR0,0,970,600_PT0_SX970_V1___.jpg"},

]
@app.route("/")
def inicio():
    tarjetas = ""
    for p in productos:
        tarjetas += f"""<div style="background:white;padding:20px;border-radius:15px;text-align:center;box-shadow:0 2px 10px #f8bbd0;">
        <img src="{p.get('foto','')}" style="width:100%;border-radius:10px;"><h3 style="color:#d81b60;">{p['nombre']}</h3>
        <p style="font-size:20px;">${p['precio']} MXN</p>
        <form action="/pedir" method="POST">
        <input type="hidden" name="producto" value="{p['nombre']}">
        <input type="text" name="nombre" placeholder="Tu nombre" required style="padding:8px;border-radius:8px;border:1px solid pink;width:90%;"><br><br>
        <button style="background:#ec407a;color:white;border:none;padding:10px 20px;border-radius:20px;">Pedir</button>
        </form></div>"""
    return f"""<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Selin Beauty</title></head>
    <body style="font-family:Arial;background:#fce4ec;margin:0;padding:20px;">
    <h1 style="text-align:center;color:#c2185b;">💄 Selin Beauty 💄</h1>
    <p style="text-align:center;">Maquillaje bonito a buen precio</p>
    <div style="display:grid;gap:15px;max-width:500px;margin:auto;">{tarjetas}</div>
    </body></html>"""

@app.route("/pedir", methods=["POST"])
def pedir():
    pedidos.append({"producto": request.form.get("producto"), "nombre": request.form.get("nombre")})
    return f"""<html><body style="font-family:Arial;background:#fce4ec;text-align:center;padding:40px;">
    <h1 style="color:#c2185b;">¡Gracias {request.form.get("nombre")}!</h1>
    <p>Tu pedido de {request.form.get("producto")} fue recibido 💗</p>
    <a href="/">Volver a la tienda</a>
    </body></html>"""

@app.route("/admin")
def administrador():
    filas = "".join([f"<tr><td style='padding:10px;border:1px solid pink;'>{x['nombre']}</td><td style='padding:10px;border:1px solid pink;'>{x['producto']}</td></tr>" for x in pedidos])
    return f"""<html><body style="font-family:Arial;background:white;padding:20px;">
    <h1>Pedidos Selin Beauty</h1>
    <table><tr><th>Cliente</th><th>Producto</th></tr>{filas}</table>
    <br><a href="/">Volver</a>
    </body></html>"""
