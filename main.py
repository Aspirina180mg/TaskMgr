'''
Un proyecto escalable que podrían desarrollar para aprender y aplicar los conceptos mencionados podría ser un sistema de gestión de tareas o una lista de tareas. Aquí te dejo una propuesta de cómo podrían estructurar el proyecto y aplicar los conocimientos aprendidos:
1. Aprender los conceptos básicos de Python: Comenzar por aprender la sintaxis básica de Python, cómo funcionan las variables y los tipos de datos, las estructuras condicionales y los errores y excepciones.Además, familiarizarse con las funciones y las funciones integradas en Python, así como las estructuras de datos como listas, tuplas, conjuntos y diccionarios.
2. Implementar una aplicación de consola de lista de tareas: Comenzar creando una aplicación de consola simple que permita al usuario crear una lista de tareas, marcar tareas como completadas y eliminar tareas.Utilizar las estructuras de datos aprendidas para almacenar y manipular las tareas.
3. Aprender sobre estructuras de datos y algoritmos: Profundizar en los conceptos de arrays, listas enlazadas, montículos (heaps), pilas y colas, tablas hash, árboles de búsqueda binaria, recursión y algoritmos de ordenamiento. Implementar algunas de estas estructuras de datos y algoritmos en el proyecto de la lista de tareas para mejorar su eficiencia y funcionalidad.
4. Aprender sobre programación orientada a objetos (OOP): Aprender sobre las clases, la herencia, los métodos especiales (dunder methods) y la encapsulación. Refactorizar el proyecto de la lista de tareas para seguir los principios de la programación orientada a objetos y mejorar su mantenibilidad y modularidad.
5. Aprender un framework web: Seleccionar un framework web como Flask o Django y aprender cómo crear una aplicación web con él. Implementar una interfaz de usuario para la lista de tareas utilizando el framework elegido. Aprender sobre los conceptos de enrutamiento, controladores (views), plantillas y formularios. 
6. Aprender sobre bases de datos: Aprender sobre bases de datos relacionales como MySQL o PostgreSQL, y bases de datos NoSQL como MongoDB o Redis. Integrar una base de datos en el proyecto de la lista de tareas para almacenar las tareas de manera persistente.
7. Aprender sobre APIs: Aprender sobre autenticación, REST, JSON APIs y otros protocolos de comunicación como gRPC o GraphQL. Agregar una API a la aplicación de la lista de tareas para permitir la creación, lectura, actualización y eliminación de tareas desde otras aplicaciones o servicios.
8. Aprender sobre seguridad web: Aprender sobre algoritmos de hash, seguridad de API, HTTPS, riesgos de OWASP, CORS, SSL/TLS, CSP y seguridad del servidor. Implementar medidas de seguridad en la aplicación de la lista de tareas para proteger los datos y prevenir vulnerabilidades.
9. Aprender sobre pruebas y CI/CD: Aprender sobre diferentes tipos de pruebas, como pruebas unitarias, pruebas de integración y pruebas de aceptación. Configurar un sistema de integración continua y entrega continua (CI/CD) para automatizar las pruebas y la implementación del proyecto de la lista de tareas.
10. Aprender sobre diseño y arquitectura de software: Aprender sobre principios de diseño y desarrollo, patrones de diseño GOF, Domain-Driven Design, Test-Driven Development, CQRS, Event Sourcing y patrones arquitectónicos como microservicios, serverless, etc. Aplicar estos conceptos al proyecto de la lista de tareas para mejorar su estructura y mantenibilidad.
11. Escalar el proyecto: Aprender sobre técnicas de escalado de bases de datos, búsqueda con Elasticsearch, manejo de mensajes con RabbitMQ o Kafka, contenerización con Docker, orquestación con Kubernetes, entre otros. Implementar estas técnicas en el proyecto de la lista de tareas para hacerlo escalable y robusto.
12. Aprender sobre monitoreo y escalado: Aprender sobre técnicas de monitoreo, instrumentación, telemetría y mitigación de problemas en aplicaciones escalables. Aprender sobre estrategias de migración y los diferentes tipos de escalado. Implementar medidas de monitoreo y escalado en el proyecto de la lista de tareas.
Recuerda que este proyecto es solo una sugerencia y puedes adaptarlo y personalizarlo según tus intereses y necesidades. A medida que avances en tu aprendizaje, puedes agregar más funcionalidades y explorar otros conceptos y tecnologías relacionadas. Lo más importante es mantener un enfoque práctico y divertido mientras construyes tu proyecto y aprendes Python y otras tecnologías. ¡Buena suerte!
'''

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar():
    input("pulse enter para volver al menú...")

def menu_principal():
    while True:
        cls()
        print("\n----- MENÚ PRINCIPAL -----")
        print("(1) Opción 1")
        print("(2) Opción 2")
        print("(3) Opción 3")
        print("(S) Salir del sistema")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            print("Seleccionada la opción 1")
            esperar()
        elif opcion == '2':
            print("Seleccionada la opción 2")
            esperar()
        elif opcion == '3':
            print("Seleccionada la opción 3")
            esperar()
        elif opcion.upper() == 'S':
            print("Seleccionada la opción Salir")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")
            esperar()

menu_principal()