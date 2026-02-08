# Manual de Usuario - RPS (Piedra-Papel-Tijeras-Lagarto-Spock)

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Inicio del Juego](#inicio-del-juego)
5. [Cómo Jugar](#cómo-jugar)
6. [Reglas del Juego](#reglas-del-juego)
7. [Estrategia del Agente Inteligente](#estrategia-del-agente-inteligente)
8. [Mensajes del Sistema](#mensajes-del-sistema)
9. [Consejos para el Jugador](#consejos-para-el-jugador)
10. [Solución de Problemas](#solución-de-problemas)

---

## Introducción

RPS es una implementación del juego **Piedra-Papel-Tijeras-Lagarto-Spock** con un agente inteligente que aprende de tus patrones de juego. El juego utiliza la variante extendida popularizada por la serie "The Big Bang Theory", que añade dos opciones adicionales al juego clásico.

**Características principales:**
- 5 opciones de juego: Piedra, Papel, Tijeras, Lagarto y Spock
- Agente inteligente con análisis de frecuencia de jugadas
- Sistema de predicción basado en historial
- Interfaz de línea de comandos simple

---

## Requisitos del Sistema

- **Python:** 3.7 o superior
- **Sistema Operativo:** Windows, macOS o Linux
- **Librerías estándar:** `random`, `enum`, `typing` (incluidas en Python)

---

## Instalación

### Opción 1: Clonar el repositorio
```bash
git clone https://github.com/cacelass/rps.git
cd rps
```

### Opción 2: Descargar el código

Descarga el repositorio como ZIP desde GitHub y descomprime.

### Instalación de dependencias
```bash
pip install -e .
```

---

## Inicio del Juego

Navega al directorio del proyecto y ejecuta:
```bash
python src/rps/main.py
```

O si el módulo está instalado:
```bash
python -m rps.main
```

---

## Cómo Jugar

### Selección de Jugada

Cuando el juego te solicite una elección, deberás ingresar un número del **0 al 4**:
```
Pick a choice (Rock[0], Paper[1], Scissors[2], Lizard[3], Spock[4]):
```

### Opciones Disponibles

| Número | Acción   |
|--------|----------|
| **0**  | Rock     |
| **1**  | Paper    |
| **2**  | Scissors |
| **3**  | Lizard   |
| **4**  | Spock    |


### Continuar o Salir

Después de cada ronda, el sistema preguntará:
```
Another round? (y/n):
```

- **Escribe `y`** para jugar otra ronda
- **Escribe `n`** para salir del juego

---

## Reglas del Juego

El juego sigue las reglas de **Piedra-Papel-Tijeras-Lagarto-Spock**:

### Tabla de Victorias

Cada acción vence a exactamente **2 otras acciones**:

| Acción   | Vence a              |
|----------|----------------------|
| **Rock (Piedra)**     | Scissors (Tijeras), Lizard (Lagarto) |
| **Paper (Papel)**     | Rock (Piedra), Spock |
| **Scissors (Tijeras)**| Paper (Papel), Lizard (Lagarto) |
| **Lizard (Lagarto)**  | Spock, Paper (Papel) |
| **Spock**             | Scissors (Tijeras), Rock (Piedra) |

### Resultados Posibles

- **Victoria:** Tu elección vence a la del computador
- **Derrota:** La elección del computador vence a la tuya
- **Empate:** Ambos eligen la misma acción

---

## Estrategia del Agente Inteligente

El agente utiliza un sistema de dos fases para tomar decisiones:

### Fase 1: Recopilación de Datos (Rondas 1-5)

- El agente juega de forma **completamente aleatoria**
- Todas las acciones tienen la misma probabilidad de ser elegidas
- El agente guarda tu historial de jugadas en memoria

**Código relevante:**
```python
if len(memoria) > 5:
    # Análisis de frecuencia
else:
    # Selección aleatoria
    computer_selection = random.randint(0, 4)
```

### Fase 2: Predicción Inteligente (Ronda 6 en adelante)

A partir de la **sexta ronda**, el agente activa el análisis de frecuencia:

#### Algoritmo de Predicción

1. **Cuenta tus jugadas:** Analiza cuántas veces has usado cada acción
2. **Calcula porcentajes:** Determina la frecuencia de cada acción
3. **Detecta patrones:** Identifica si hay una acción dominante (≥40%)
4. **Contraataca:** Si detecta patrón, elige aleatoriamente entre las acciones que vencen tu jugada favorita
5. **Mantiene aleatoriedad:** Si no hay patrón claro (<40%), juega al azar

#### Umbral de Predicción

El agente considera que existe un **patrón predecible** cuando:
```
frecuencia_de_acción_más_común ≥ 40%
```

#### Ejemplo Práctico

Si después de 10 rondas has jugado:
- Rock: 5 veces (50%)
- Paper: 2 veces (20%)
- Scissors: 2 veces (20%)
- Lizard: 1 vez (10%)
- Spock: 0 veces (0%)

El agente detectará que prefieres **Rock (50% ≥ 40%)** y elegirá aleatoriamente entre:
- **Paper** (vence a Rock)
- **Spock** (vence a Rock)

---

## Información Técnica

### Almacenamiento de Historial

El juego mantiene un historial de **todas tus jugadas** en memoria:
```python
memoria: List[int] = []  # Se reinicia al cerrar el programa
```

**Nota:** El historial se pierde al cerrar el programa. No hay persistencia de datos entre sesiones.

### Validación de Entrada

El sistema valida que:
- La entrada sea un número entero
- El número esté en el rango [0, 4]
- Si no cumple, repite la solicitud hasta recibir entrada válida

### Comportamiento Determinista vs Aleatorio

- **Rondas 1-5:** 100% aleatorio
- **Ronda 6+:** 
  - Si detecta patrón (≥40%): Contraataque inteligente
  - Si no detecta patrón (<40%): Aleatorio
