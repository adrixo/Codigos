TEORÍA DE CÓDIGOS
========================

Interfaz básica para instanciación y manejo de códigos para python2. Requiere la instalación del módulo `numpy <https://docs.scipy.org/doc/numpy/user/install.html>`_.

.. code-block:: bash

      pip install numpy
      ó
      sudo apt-get install python-numpy

Programas de ejemplo
#######################

En la carpeta ``ejemplos`` podemos encontrar algunos programas básicos que utilizan la api.
A continuación se muestra la ejecución de ``ejemplos/Ejemplo_3CodigosBasicos.py`` que instancia y muestra la información de los codigos de triple repetición, triple control y paridad.

.. code-block:: bash

      ./ejemplo/Ejemplo_3CodigosBasicos.py

.. image:: |Imagen ejemplo| img/Ejemplo_CodigosBasicos.png

      :alt: Codigos de ejemplo
      :width: 100%
      :align: center

Estructura del proyecto
#######################

El proyecto se estructura en carpetas: En ``ejemplos`` encontramos distintas formas de utilizar la Interfaz, en ``Matrices`` distintos ejemplos que podran ser cargados en tiempo de ejecución y en ``src`` los distintos modulos que componen la api

.. code-block:: bash

    .
    ├── ejemplos
    │   └── Ejemplo.py
    |
    ├── Matrices
    │   ├── MatrizCodigo_Control.txt
    │   └── MatrizCodigo_Generadora.txt
    |
    └── src
        ├── AlgebraLineal.py
        ├── aritmeticaModular.py
        ├── Codigo.py
        ├── Cuerpos.py
        ├── FuncionesCodigos.py
        └── Parametricas.py

Módulos usados:

+-----------------------+-----------------------------------------------------+
| Módulo                | Descripción                                         |
+=======================+=====================================================+
| AlgebraLineal.py      | Funciones de algebra lineal que necesitaremos para  |
|                       | la obtención y manejo de códigos                    |
+-----------------------+-----------------------------------------------------+
| FuncionesCodigos.py   | Funciones usadas en la teoría de códigos            |
+-----------------------+-----------------------------------------------------+
| Codigo.py             | Clase Codigo capaz de instanciar un código y        |
|                       | realizar operaciones sobre el.                      |
|                       | Usa las funciones declaradas en FuncionesCodigos.py |
+-----------------------+-----------------------------------------------------+
| Parametricas.py       | Ecuaciones paramétricas para generar códigos        |
+-----------------------+-----------------------------------------------------+
| aritmeticaModular.py  | Vacío                                               |
+-----------------------+-----------------------------------------------------+
| Cuerpos.py            | Vacío                                               |
+-----------------------+-----------------------------------------------------+

Referencias
-----------

https://docs.scipy.org/doc/numpy/reference/
