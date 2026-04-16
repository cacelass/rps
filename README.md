# RPS Predictive Agent

**Autor:** Alejandro Cancelas Chapela  
**Asignatura:** Práctica Axentes Intelixentes  
**Especialidad:** Inteligencia Artificial y Big Data

Agente inteligente para los juegos **Piedra-Papel-Tijeras (RPS)** y **Piedra-Papel-Tijeras-Lagarto-Spock (RPSLG)**, implementado en Python. El agente analiza el historial de jugadas del usuario y adapta su estrategia de predicción a lo largo de la partida.

---

## Contorno de tareas

| Propiedad | Valor |
|-----------|-------|
| Observable | Parcialmente observable |
| Agentes | Multiagente (competitivo) |
| Determinista | Estocástico |
| Episódico | Secuencial |
| Estático | Estático |
| Discreto | Discreto |
| Conocido | Conocido |

**Justificación:**

- **Parcialmente observable:** el agente no puede ver la acción del rival antes de elegir la suya.
- **Multiagente competitivo:** juega contra un humano u otro agente con objetivos opuestos.
- **Estocástico:** el resultado depende de las decisiones del rival, no solo del agente.
- **Secuencial:** cada ronda afecta a las siguientes; el historial es parte del estado.
- **Estático:** el entorno no cambia mientras el agente delibera.
- **Discreto:** el espacio de acciones es finito (3 o 5 gestos).
- **Conocido:** las reglas del juego son conocidas de antemano.

---

## Arquitectura del agente

El agente sigue el modelo de **agente reactivo basado en modelos** (Russell & Norvig, cap. 2):

```
Percepciones → Estado interno → Lógica predictiva → Decisión → Acción
```

| Componente | Descripción |
|------------|-------------|
| Sensores | Capturan la acción del usuario y la transforman en un valor numérico |
| Estado interno | Historial de jugadas (`memoria`) que convierte el entorno en secuencial |
| Lógica predictiva | Análisis de frecuencia y bayesiano para estimar la próxima jugada |
| Reglas condición-acción | Selección de la acción que maximiza la victoria contra la predicción |
| Actuadores | Devuelven la acción elegida y actualizan el estado |

---

## Estrategia de predicción

El agente adapta su estrategia según el número de rondas jugadas:

| Rondas | Estrategia |
|--------|-----------|
| 1 – 5 | Selección aleatoria (exploración) |
| 6 – 15 | Análisis de frecuencia |
| 16+ | Análisis bayesiano por transiciones |

### Análisis de frecuencia (rondas 6-15)

Calcula el porcentaje de uso de cada acción. Si alguna supera el 40%, predice que el usuario la repetirá y elige la acción que la derrota. Si no hay patrón claro, mantiene aleatoriedad.

### Análisis bayesiano (rondas 16+)

Construye una **matriz de transiciones 5×5** donde cada celda `[i][j]` cuenta cuántas veces el usuario jugó `j` después de haber jugado `i`. Con esa matriz predice la jugada más probable dada la última acción del usuario, y selecciona la acción ganadora.

```
transiciones[jugada_anterior][jugada_siguiente] += 1
predicción = argmax(transiciones[última_jugada])
```

---

## Modos de juego

Al iniciar, el agente pregunta el modo:

- `0` — **RPS:** Piedra, Papel, Tijeras (3 acciones)
- `1` — **RPSLG:** Piedra, Papel, Tijeras, Lagarto, Spock (5 acciones)

Las tablas de victorias y la lógica de predicción se adaptan automáticamente al modo elegido.

### Tabla de victorias RPSLG

| Acción | Vence a |
|--------|---------|
| Rock | Scissors, Lizard |
| Paper | Rock, Spock |
| Scissors | Paper, Lizard |
| Lizard | Spock, Paper |
| Spock | Scissors, Rock |

---

## Estructura del proyecto

```
rps/
├── data/                       # Recursos externos (imágenes, diagramas)
├── docs/                       # Documentación generada con Sphinx
│   ├── build/                  # HTML generado
│   └── source/                 # Fuentes Sphinx (conf.py, .rst)
├── src/
│   ├── rps/
│   │   ├── __init__.py
│   │   └── main.py             # Lógica principal del agente
│   └── test/
│       ├── __init__.py
│       └── test_proba.py       # Tests de probabilidad
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/cacelass/rps-predictive-agent
cd rps-predictive-agent

# Instalar dependencias con uv
uv sync

# Ejecutar
python3 src/rps/main.py
```

---

## Documentación

Generada automáticamente con **Sphinx** usando `autodoc` y `napoleon` para integrar los docstrings de Python.

```bash
cd docs
make html
```

---

## Principios de diseño

El proyecto sigue los principios **SOLID**:

- **SRP:** cada función tiene una responsabilidad única (evaluación, predicción, interacción).
- **OCP:** añadir nuevos gestos solo requiere actualizar la tabla de victorias y el enum, sin tocar la lógica del agente.