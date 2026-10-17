import io

import zxingcpp
from PIL import Image

from ecoharmony.codigos_qr import generar_qr_png


def test_qr_generado_es_una_imagen_png_legible_con_su_contenido():
    """Los QR son funcionales: un lector de QR recupera el contenido original."""
    contenido = "ORD-0001|12345678|Tirolesa|2026-10-20T10:00:00-03:00"

    imagen = generar_qr_png(contenido)

    assert imagen.startswith(b"\x89PNG")
    leidos = zxingcpp.read_barcodes(Image.open(io.BytesIO(imagen)))
    assert [codigo.text for codigo in leidos] == [contenido]