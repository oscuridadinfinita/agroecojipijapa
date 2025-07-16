# Informe Técnico: Mantenimiento de Sistemas - Hostería del Parque

## Introducción

Este informe detalla el plan de mantenimiento para los sistemas de agua potable, calentamiento, piscina, PTAR y climatización de la Hostería del Parque, incluyendo equipos preexistentes y nuevas estructuras.

## Datos Generales

- **Ubicación**: Machalilla, Ecuador
- **Fecha**: 10 de Junio, 2025
- **Cliente**: Hostería del Parque
- **Gerente**: Gricel Rodríguez - Provitur S.A.
- **Responsable Técnico**: Juan Salazar Flores (juancarlosalazar.jcsf@gmail.com, +593 99 514 1304)

## Resumen Ejecutivo

Este documento presenta el plan completo de mantenimiento para los sistemas de bombeo, calentamiento, climatización, refrigeración y PTAR, con equipos existentes y propuestas de mejora.

### Sistemas Principales

- **Sistema de Agua Potable**
  - 3 Bombas Pedrollo: 5.5 HP cada una
  - Aljibes: 2 reservorios de 50 m³ cada uno
  - Fuente: Cisterna de agua potable
  - Destino: Suministro a todo el hotel
- **Sistema de Calentamiento**
  - Calentador de Agua: Modelo H0328500
  - Combustible: GLP (6 tanques de 15kg cada uno)
  - Conexión: Sentralina de GLP
  - Uso: Piscina y servicios del hotel
- **Sistema de Piscina y Jacuzzi**
  - Pentair XF-12: Piscina
  - Pentair WF-12: Jacuzzi
  - Leo XKP1604: Jacuzzi
  - Sistema de filtración: Filtrado y Retrolavado
- **Sistema de Climatización**
  - 34 equipos Split Consola, 3 congeladores, 1 máquina de hielo, 16 minibares (detalles en tabla abajo)

**ADVERTENCIA DE SEGURIDAD:** El calentador de agua debe ser instalado y reparado por personal técnico especializado. La instalación y/o funcionamiento inadecuados pueden generar gases de monóxido de carbono que pueden ocasionar lesiones graves, daños a la propiedad e incluso la muerte.

## Configuración del Sistema

### Diagrama de Sistemas

```mermaid
graph TD
subgraph "Sistema de Agua Potable"
    A[Cisterna] --> B[Bomba Pedrollo 1]
    A --> C[Bomba Pedrollo 2]
    A --> D[Bomba Pedrollo 3]
    B & C & D --> E[Aljibe 1 (50m³)]
    B & C & D --> F[Aljibe 2 (50m³)]
    E --> G[Red Hotel]
    F --> G[Red Hotel]
end
subgraph "Sistema de Piscina y Calentamiento"
    H[Piscina] --> I[Pentair XF-12]
    H --> J[Pentair WF-12]
    H --> K[Leo XKP1604]
    I & J & K --> L[Filtro Arena]
    L --> M[Calentador H0328500]
    M --> N[Retorno Piscina]
end
style A fill:#1a6bb2,stroke:#0d4a8a,color:#fff
style B fill:#4caf50,stroke:#2e7d32
style C fill:#4caf50,stroke:#2e7d32
style D fill:#4caf50,stroke:#2e7d32
style E fill:#1a6bb2,stroke:#0d4a8a,color:#fff
style F fill:#1a6bb2,stroke:#0d4a8a,color:#fff
style G fill:#0d4a8a,stroke:#1a6bb2,color:#fff
style H fill:#1a6bb2,stroke:#0d4a8a,color:#fff
style I fill:#ff9800,stroke:#f57c00
style J fill:#ff9800,stroke:#f57c00
style K fill:#ff9800,stroke:#f57c00
style L fill:#9c27b0,stroke:#7b1fa2
style M fill:#f44336,stroke:#d32f2f
style N fill:#4caf50,stroke:#2e7d32
```

### Parámetros Técnicos

| Equipo | Modelo | Potencia | Capacidad | Estado |
| --- | --- | --- | --- | --- |
| Bomba Pedrollo 1 | Modelo del Geggio Nero | 5.5 HP | 50-250 mm H | Óptimo |
| Bomba Pedrollo 2 | Modelo del Geggio Nero | 5.5 HP | 50-250 mm H | Óptimo |
| Bomba Pedrollo 3 | Modelo del Geggio Nero | 5.5 HP | 50-250 mm H | Vigilancia |
| Calentador | H0328500 (Legacy™ LRZ) | \- | Max 90°C | Óptimo |
| Aljibe 1 | Reservorio | \- | 50 m³ | Óptimo |
| Aljibe 2 | Reservorio | \- | 50 m³ | Óptimo |

## Sistema de Climatización

### Inventario de Equipos

| TIPO | BTU | MARCA | MODEL U/E | MODEL U/C | SERIE U/E | SERIE U/C | HABITACIÓN | FECHA INSTALACIÓN | OBSERVACION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPLIT CONSOLA | 24,000 | SMC | SMCAS242IV2 | SMCAS2421V2 | D2022640203149121 20450 | D20226402051490 5150132 | CABAÑA PRINCIPAL- HAB. SEBASTIAN | 01/12/2014 |  |
| SPLIT CONSOLA | 24,000 | SMC | SMCAS242IV2 | SMCAS2421V2 | \- | \- | CABAÑA PRINCIPAL- PLANTA ALTA | 12/03/2015 |  |
| SPLIT CONSOLA | 24,000 | SMC | \- | \- | \- | SN:34065876506890201194 | CABAÑA PRINCIPAL PB | 01/06/2019 |  |
| SPLIT CONSOLA | 24,000 | COMFORTSTA R | \- | \- | \- | \- | CABAÑA PRINCIPAL PB | \- |  |
| SPLIT CONSOLA | 24,000 | \- | \- | \- | \- | \- | SALA DE ENTRETENIMIENTO | \- |  |
| SPLIT CONSOLA | 12,000 | \- | \- | \- | \- | \- | 101 | \- |  |
| SPLIT CONSOLA | 12,000 | SMC | SMCEV122IV4 | SMCC0122IV4 | SMCAS122IV419010 0218 | SMCAS122IV41901 00435 | 102 | 08/08/2019 |  |
| SPLIT CONSOLA | 24,000 | SMC | SMCEV2421V2 | SMCEV2421V2 | SMCAS2421V216090 0218 | SMCAS242IV21608 00032 | 103 | 05/07/2017 |  |
| ... (continúa con el resto de la tabla) ... |  |  |  |  |  |  |  |  |  |

*Nota: Se recomienda completar los datos faltantes (marca, modelo, serie) para un mantenimiento más preciso.*

## Plan de Mantenimiento

### Cronograma 2025

```mermaid
gantt
title Cronograma Mantenimiento 2025
dateFormat YYYY-MM-DD
axisFormat %d/%m
section Bombas Piscina
Pentair XF-12 Mantenimiento :active, 2025-06-09, 2d
Pentair WF-12 Mantenimiento :2025-06-16, 2d
Leo XKP1604 Mantenimiento :2025-06-22, 2d
section Bombas Agua Potable
Pedrollo 1 Mantenimiento :2025-07-01, 2d
Pedrollo 2 Mantenimiento :2025-07-06, 2d
Pedrollo 3 Mantenimiento :2025-07-12, 2d
section Calentador y Reservorios
Calentador H0328500 Revisión :2025-07-20, 2d
Aljibe 1 Limpieza :2025-08-01, 2d
Aljibe 2 Limpieza :2025-08-05, 2d
section Climatización
Mantenimiento Preventivo Aire Acondicionado :2025-06-15, 5d
section Mejoras
Instalación sensores IoT :2025-08-10, 5d
```

### Actividades Prioritarias

| Sistema | Equipo | Tareas | Inicio | Duración |
| --- | --- | --- | --- | --- |
| Piscina | Pentair XF-12 | Revisión sello mecánico, balanceo dinámico | 09/06/2025 | 2 días |
| Piscina | Pentair WF-12 | Limpieza cámaras, test capacitor | 16/06/2025 | 2 días |
| Agua Potable | Pedrollo 3 | Revisión impulsores, verificación protección | 12/07/2025 | 2 días |
| Calentamiento | Calentador H0328500 | Revisión quemadores, verificación gases | 20/07/2025 | 2 días |
| Climatización | Split Consola (SMC) | Limpieza filtros, revisión de motor ventilador | 15/06/2025 | 5 días |

## Presupuesto Estimado

### Materiales y Servicios

| Concepto | Costo Unitario (USD) | Cantidad | Subtotal (USD) |
| --- | --- | --- | --- |
| Rodamientos SKF para Pentair | $42.50 | 6 | $255.00 |
| Sellos mecánicos para Pedrollo | $75.00 | 3 | $225.00 |
| Kit mantenimiento calentador | $180.00 | 1 | $180.00 |
| Materiales limpieza aljibes | $350.00 | 1 | $350.00 |
| Filtros aire acondicionado | $25.00 | 34 | $850.00 |
| Mano de obra especializada | $80/día | 32 días | $2,560.00 |
| Subtotal |  | $4,420.00 |  |
| Contingencias (10%) |  | $442.00 |  |
| IVA (15%) |  | $663.00 |  |
| TOTAL ESTIMADO |  | $5,525.00 |  |

*Nota: Este presupuesto incluye materiales originales, mano de obra especializada y garantía de 12 meses. El costo de desplazamiento y alojamiento técnico está incluido.*

## Recomendaciones Técnicas

- **Sistema de GLP**: Instalación de detección de monóxido de carbono en el cuarto del calentador.
- **Rotación de Bombas**: Implementar sistema de rotación automática para las bombas Pedrollo.
- **Monitoreo de Aljibes**: Instalar sensores de nivel en los reservorios.
- **Climatización**: Revisar y reparar el motor ventilador de la unidad de 60,000 BTU en la cocina.

## Conclusión

Este informe será actualizado con más detalles a medida que avancen las tareas de mantenimiento.

## Firmas

- **Elaborado por**: Ing. Juan Salazar Flores (CTM-EC-11245)
- **Aprobado por**: Gricel Rodríguez (Gerente Provitur S.A.)