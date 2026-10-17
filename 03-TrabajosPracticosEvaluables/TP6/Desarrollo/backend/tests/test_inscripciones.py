import pytest
from datetime import datetime, timedelta, timezone

from ecoharmony.models.visitante import Visitante
from ecoharmony.inscripciones import ServicioInscripciones


def test_cup_01_registra_una_persona_con_cupos_disponibles():
    """CUP-01: registra una inscripción válida cuando hay cupos."""

    zona_argentina = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona_argentina)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona_argentina)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert resultado.actividad == "Tirolesa"
    assert resultado.inicio == inicio
    assert resultado.visitantes == [visitante]

def test_cup_01_conserva_inscripcion_registrada():
    """CUP-01: la inscripción confirmada queda registrada."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert len(servicio.inscripciones) == 1
    assert servicio.inscripciones[0] == resultado

def test_cup_02_ocupa_el_ultimo_cupo_disponible():
    """CUP-02: permite ocupar el último cupo disponible."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    # Tirolesa tiene capacidad 10.
    # Simulamos que ya hay 9 lugares ocupados.
    servicio.ocupacion[("Tirolesa", inicio)] = 9

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert servicio.ocupacion[("Tirolesa", inicio)] == 10
    assert servicio.consultar_cupos("Tirolesa", inicio) == 0

def test_cup_03_inscribe_diez_personas_en_tirolesa():
    """CUP-03: una inscripción grupal ocupa los 10 cupos de Tirolesa."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitantes = [
        Visitante(
            nombre=f"Visitante {i}",
            dni=f"{10000000 + i}",
            edad=20,
            talle="M",
        )
        for i in range(10)
    ]

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=10,
        visitantes=visitantes,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert len(resultado.visitantes) == 10
    assert len(servicio.inscripciones) == 1
    assert servicio.ocupacion[("Tirolesa", inicio)] == 10
    assert servicio.consultar_cupos("Tirolesa", inicio) == 0

def test_cup_04_rechaza_inscripcion_sin_cupos():
    """CUP-04: no permite inscribir cuando el turno está lleno."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    # Los 10 cupos de Tirolesa están ocupados.
    servicio.ocupacion[("Tirolesa", inicio)] = 10

    ocupacion_anterior = dict(servicio.ocupacion)
    inscripciones_anteriores = len(servicio.inscripciones)

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is None
    assert servicio.ocupacion == ocupacion_anterior
    assert len(servicio.inscripciones) == inscripciones_anteriores
    assert servicio.consultar_cupos("Tirolesa", inicio) == 0

def test_cup_05_rechaza_grupo_que_supera_cupos_disponibles():
    """CUP-05: rechaza todo el grupo si los cupos son insuficientes."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitantes = [
        Visitante(
            nombre=f"Visitante {i}",
            dni=str(10000000 + i),
            edad=20,
            talle="M",
        )
        for i in range(3)
    ]

    servicio = ServicioInscripciones()

    # Tirolesa tiene 10 cupos, de los cuales 8 están ocupados.
    servicio.ocupacion[("Tirolesa", inicio)] = 8

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=3,
        visitantes=visitantes,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is None
    assert len(servicio.inscripciones) == 0
    assert servicio.ocupacion[("Tirolesa", inicio)] == 8
    assert servicio.consultar_cupos("Tirolesa", inicio) == 2

def test_cup_06_safari_ocupa_sus_ocho_cupos():
    """CUP-06: Safari permite ocupar sus 8 cupos."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitantes = [
        Visitante(
            nombre=f"Visitante {i}",
            dni=str(10000000 + i),
            edad=20,
            talle=None,
        )
        for i in range(8)
    ]

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Safari",
        inicio=inicio,
        ahora=ahora,
        cantidad=8,
        visitantes=visitantes,
        actividad_terminos="Safari",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert len(resultado.visitantes) == 8
    assert servicio.ocupacion[("Safari", inicio)] == 8
    assert servicio.consultar_cupos("Safari", inicio) == 0

@pytest.mark.parametrize("actividad", ["Palestra", "Jardinería"])
def test_cup_07_capacidad_de_doce_personas(actividad):
    """CUP-07: Palestra y Jardinería tienen 12 cupos."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitantes = [
        Visitante(
            nombre=f"Visitante {i}",
            dni=str(10000000 + i),
            edad=20,
            talle="M" if actividad == "Palestra" else None,
        )
        for i in range(12)
    ]

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad=actividad,
        inicio=inicio,
        ahora=ahora,
        cantidad=12,
        visitantes=visitantes,
        actividad_terminos=actividad,
        acepto_terminos=True,
    )

    assert resultado is not None
    assert len(resultado.visitantes) == 12
    assert servicio.ocupacion[(actividad, inicio)] == 12
    assert servicio.consultar_cupos(actividad, inicio) == 0

def test_cup_08_cupos_independientes_por_turno():
    """CUP-08: cada turno mantiene su propia ocupación."""

    zona = timezone(timedelta(hours=-3))
    inicio_10 = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    inicio_11 = datetime(2026, 10, 20, 11, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitantes = [
        Visitante(
            nombre=f"Visitante {i}",
            dni=str(10000000 + i),
            edad=20,
            talle="M",
        )
        for i in range(3)
    ]

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio_10,
        ahora=ahora,
        cantidad=3,
        visitantes=visitantes,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None

    # Se ocuparon 3 lugares a las 10:00.
    assert servicio.consultar_cupos("Tirolesa", inicio_10) == 7

    # El turno de las 11:00 mantiene sus 10 cupos.
    assert servicio.consultar_cupos("Tirolesa", inicio_11) == 10

    assert servicio.ocupacion[("Tirolesa", inicio_10)] == 3
    assert servicio.ocupacion.get(("Tirolesa", inicio_11), 0) == 0

def test_est_03_datos_invalidos_no_modifican_estado():
    """EST-03: una inscripción inválida no registra ni ocupa cupos."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni=None,
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is None
    assert len(servicio.inscripciones) == 0
    assert servicio.consultar_cupos("Tirolesa", inicio) == 10
    assert servicio.ocupacion.get(("Tirolesa", inicio), 0) == 0

def test_est_04_terminos_no_aceptados_no_modifican_estado():
    """EST-04: rechazar sin modificar estado si no acepta términos."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    inscripciones_anteriores = servicio.inscripciones
    ocupacion_anterior = dict(servicio.ocupacion)

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=False,
    )

    assert resultado is None
    assert servicio.inscripciones == inscripciones_anteriores
    assert servicio.ocupacion == ocupacion_anterior
    assert servicio.consultar_cupos("Tirolesa", inicio) == 10

def test_est_01_conserva_inscripcion_confirmada():
    """EST-01: una inscripción confirmada queda disponible para consulta."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    inscripciones_guardadas = servicio.inscripciones

    assert resultado is not None
    assert len(inscripciones_guardadas) == 1
    assert inscripciones_guardadas[0] == resultado
    assert inscripciones_guardadas[0].actividad == "Tirolesa"
    assert inscripciones_guardadas[0].inicio == inicio
    assert inscripciones_guardadas[0].visitantes == [visitante]

def test_est_02_ocupacion_refleja_inscripciones():
    """EST-02: la ocupación refleja los participantes registrados."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    servicio = ServicioInscripciones()

    primer_grupo = [
        Visitante(
            nombre="Ana García",
            dni="12345678",
            edad=20,
            talle="M",
        ),
        Visitante(
            nombre="Juan Pérez",
            dni="23456789",
            edad=25,
            talle="L",
        ),
    ]

    segundo_grupo = [
        Visitante(
            nombre="Lucía Gómez",
            dni="34567890",
            edad=30,
            talle="S",
        )
    ]

    resultado_1 = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=2,
        visitantes=primer_grupo,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado_1 is not None
    assert servicio.consultar_cupos("Tirolesa", inicio) == 8

    resultado_2 = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=segundo_grupo,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado_2 is not None
    assert len(servicio.inscripciones) == 2
    assert servicio.ocupacion[("Tirolesa", inicio)] == 3
    assert servicio.consultar_cupos("Tirolesa", inicio) == 7

    total_participantes = sum(
        len(inscripcion.visitantes)
        for inscripcion in servicio.inscripciones
    )

    assert total_participantes == 3
    assert total_participantes == servicio.ocupacion[
        ("Tirolesa", inicio)
    ]

def test_sup_05_rechaza_grupo_con_participante_superpuesto():
    """SUP-05 integral: rechaza todo el grupo si alguien tiene un conflicto."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    servicio = ServicioInscripciones()

    # Primera inscripción: Ana se anota en Safari a las 10:00.
    ana = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle=None,
    )

    primera = servicio.inscribir(
        actividad="Safari",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[ana],
        actividad_terminos="Safari",
        acepto_terminos=True,
    )

    assert primera is not None

    # Nuevo grupo: Ana intenta inscribirse también en Tirolesa.
    grupo = [
        Visitante("Juan Pérez", "23456789", 25, "M"),
        Visitante("Ana García", "12345678", 20, "M"),
        Visitante("Lucía Gómez", "34567890", 30, "S"),
    ]

    inscripciones_antes = servicio.inscripciones
    ocupacion_antes = dict(servicio.ocupacion)

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=3,
        visitantes=grupo,
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is None
    assert servicio.inscripciones == inscripciones_antes
    assert servicio.ocupacion == ocupacion_antes
    assert servicio.consultar_cupos("Tirolesa", inicio) == 10
