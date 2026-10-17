import io

import qrcode


def generar_qr_png(contenido: str) -> bytes:
    buffer = io.BytesIO()
    qrcode.make(contenido).save(buffer, format="PNG")
    return buffer.getvalue()