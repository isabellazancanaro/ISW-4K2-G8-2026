"use strict";
const mail = document.getElementById("mail");
document.getElementById("ver-mail").addEventListener("click", () => mail.showModal());
document.getElementById("cerrar-mail").addEventListener("click", () => mail.close());
// un click en el fondo oscuro también cierra
mail.addEventListener("click", (e) => { if (e.target === mail) mail.close(); });

// Escribe una línea de texto y achica la fuente si no entra en el ancho disponible
function escribir(g, texto, peso, tam, x, y, maxAncho, color) {
    g.fillStyle = color;
    g.font = `${peso} ${tam}px Lato, sans-serif`;
    while (g.measureText(texto).width > maxAncho && tam > 14) {
    tam -= 1;
    g.font = `${peso} ${tam}px Lato, sans-serif`;
    }
    g.fillText(texto, x, y);
}

// Dibuja la misma card que se ve en el mail, más actividad, fecha y hora
async function dibujarTarjeta(indice) {
    await Promise.all([
    document.fonts.load("900 40px Lato"),
    document.fonts.load("700 30px Lato"),
    document.fonts.load("400 30px Lato"),
    ]);
    const tarjeta = document.querySelectorAll(".mail-visitante")[indice];
    const img = tarjeta.querySelector("img");
    await img.decode();
    const [nombre, detalle] = Array.from(tarjeta.querySelectorAll("p"), p => p.textContent.trim());

    const ancho = 1000, alto = 340, x = 330, maxAncho = ancho - x - 40;
    const canvas = document.createElement("canvas");
    canvas.width = ancho;
    canvas.height = alto;
    const g = canvas.getContext("2d");
    g.fillStyle = "#ffffff";
    g.fillRect(0, 0, ancho, alto);
    g.strokeStyle = "#a7c957";
    g.lineWidth = 6;
    g.beginPath();
    g.roundRect(3, 3, ancho - 6, alto - 6, 28);
    g.stroke();

    g.drawImage(img, 40, 40, 260, 260);
    g.textBaseline = "alphabetic";
    escribir(g, nombre, 900, 44, x, 105, maxAncho, "#243a29");
    escribir(g, detalle, 400, 30, x, 155, maxAncho, "#243a29");

    g.strokeStyle = "#e6dfc6";
    g.lineWidth = 2;
    g.beginPath();
    g.moveTo(x, 192);
    g.lineTo(ancho - 40, 192);
    g.stroke();

    escribir(g, mail.dataset.actividad, 900, 38, x, 244, maxAncho, "#386641");
    escribir(g, mail.dataset.turno, 400, 30, x, 292, maxAncho, "#243a29");
    return canvas;
}

document.querySelectorAll(".adjunto").forEach(enlace => {
    enlace.addEventListener("click", async (e) => {
    e.preventDefault();
    const canvas = await dibujarTarjeta(Number(enlace.dataset.indice));
    canvas.toBlob(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = enlace.dataset.archivo;
        a.click();
        setTimeout(() => URL.revokeObjectURL(url), 1000);
    }, "image/png");
    });
});