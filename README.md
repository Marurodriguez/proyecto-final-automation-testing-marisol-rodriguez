# Proyecto Final – Framework de Automatización de Pruebas

## 📌 Descripción del Proyecto

Este proyecto corresponde a la **Entrega Final** del curso de QA Automation y consiste en el desarrollo de un **framework de automatización de pruebas** desde cero.

El objetivo principal es demostrar la aplicación práctica de los conocimientos adquiridos durante el curso, integrando pruebas automatizadas de **interfaz de usuario (UI)** y **API**, utilizando buenas prácticas de automatización, una estructura clara de proyecto y código mantenible.

El framework permite ejecutar pruebas de forma consistente, obtener reportes claros de resultados y facilitar la incorporación de nuevos casos de prueba.

---

## 🛠️ Tecnologías Utilizadas

* Python 3
* Pytest
* Selenium WebDriver
* Requests
* Pytest-HTML (reportes)
* Git / GitHub

---

## 📁 Estructura del Proyecto

```
proyecto-final-automation-testing-marisol-rodriguez/
│
├── data/
│   └── users.json              # Datos de prueba externos
│
├── pages/                      # Page Object Model (UI)
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── api/
│   │   └── test_users_api.py   # Tests de API
│   ├── test_login.py           # Tests de login UI
│   └── test_purchase_flow.py   # Flujo completo de compra
│
├── utils/
│   ├── driver_factory.py       # Configuración del WebDriver
│   ├── data_loader.py          # Lectura de datos externos
│   └── screenshot.py           # Capturas automáticas en fallos
│
├── reports/
│   └── report.html             # Reporte HTML generado por Pytest
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ Instalación y Configuración

1. Clonar el repositorio:

```bash
git clone https://github.com/Marurodriguez/proyecto-final-automation-testing-marisol-rodriguez.git
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de Pruebas

Para ejecutar todas las pruebas (UI + API):

```bash
pytest
```

---

## 📊 Reportes

Luego de la ejecución, se genera un reporte HTML automático en la carpeta:

```
reports/report.html
```

El reporte muestra:

* Tests ejecutados
* Estado (passed / failed)
* Tiempo de ejecución
* Capturas de pantalla en caso de fallos en pruebas UI

---

## ✅ Funcionalidades Cubiertas

### Pruebas UI

* Login válido e inválido
* Navegación y agregado de productos
* Flujo completo de compra
* Uso de Page Object Model
* Parametrización de datos externos
* Capturas automáticas ante fallos

### Pruebas de API

* Pruebas sobre API pública
* Métodos GET, POST y DELETE
* Validación de códigos de estado
* Validación de estructura y contenido JSON

---

## 📝 Notas Finales

El framework fue diseñado para ser fácilmente escalable, permitiendo la incorporación de nuevos casos de prueba y módulos sin afectar la estructura existente. Todas las pruebas son independientes entre sí y pueden ejecutarse de forma automatizada.
