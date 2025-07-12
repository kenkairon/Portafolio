# cursoFinalDjango
Educativo y de Aprendizaje Personal


Proyecto Django

1. Partes del Proyecto


## 📌 Nombre del Proyecto


### 👤 Integrante

Carlos Vasquez

## 🎯 Objetivo General

Desarrollar una aplicación web que permita generar un currículum vitae en tiempo real, incorporando datos ingresados dinámicamente por el usuario y ofreciendo la opción de visualizar e imprimir el currículum finalizado.

Estructura del Proyecto:


## 📝 Descripción del Proyecto

El proyecto resuelve la dificultad que enfrentan muchas personas al crear, actualizar y presentar su currículum vitae. Al permitir ingresar datos en tiempo real y generar automáticamente un formato listo para impresión, facilitando la creación de un CV profesional de manera rápida y accesible.


## ⚙️ Funcionalidad Principal

Permitir al usuario ingresar sus datos personales, académicos y laborales de forma estructurada, para luego generar automáticamente un currículum vitae que puede ser visualizado, descargado e impreso desde la plataforma.


## 👥 Usuarios del Sistema

El sistema está diseñado para ser utilizado por personas que desean crear o actualizar su currículum vitae de forma rápida y profesional , Esto incluye estudiantes, profesionales, técnicos y cualquier usuario que requiera generar su portafolio laboral.

3. Repositorio en GitHub

https://github.com/kenkairon/Portafolio.git

4.URL del Proyecto en Producción

https://kenkairon.pythonanywhere.com/

5. Tecnologías a Utilizar

Django 5.1.5

SQLite

Frontend: Bootstrap 4.6

Librerías adicionales para iconos : font-awesome 6.5.1  y bootstrap-iconos 1.11


## 🔄 Flujo del Sistema

El flujo del sistema describe las etapas que sigue el usuario dentro de la aplicación, desde su ingreso hasta la generación y visualización del currículum profesional.

1. Ingreso a la plataforma
- El usuario puede registrarse o iniciar sesión mediante un formulario de autenticación.
- Una vez autenticado, es redirigido al dashboard principal, donde tiene acceso a todas las secciones de su portafolio profesional.

2. Panel de control (Dashboard)
Desde el dashboard, el usuario tiene acceso a diferentes módulos que representan componentes clave de su currículum:

- Encabezado Profesional (Header): Permite definir información introductoria como nombre, cargo, resumen profesional, entre otros.
- Habilidades: El usuario puede agregar habilidades técnicas o blandas, cada una asociada a un ícono personalizado para mejorar la visualización.
- Objetivos Profesionales: Sección destinada a ingresar las metas u objetivos del usuario.
- Proyectos: Permite documentar y listar los proyectos personales o profesionales más relevantes.
- Certificaciones: Sección para registrar certificados, cursos o capacitaciones completadas por el usuario.
- Iconos: Librería personalizada para representar gráficamente habilidades o secciones clave del CV.

3. Generación del Currículum
- Una vez que el usuario ha completado todas las secciones, el sistema genera automáticamente un currículum profesional estructurado.
- El currículum puede ser:
  - Visualizado en tiempo real desde la plataforma.
  - Descargado en formato listo para impresión.
  - Impreso directamente desde el navegador.

Se registra un usuario o se logea para empezar a entrar en la Plataforma

Dashboard

iconos

header

Habilidades

Objetivos

Proyectos

Certificaciones

6. Relación de los Modelos

Módulo:  headerProfesional

Módulo: Iconos

7. Funcionalidades CRUD

¿Qué modelos tienen CRUD completo (crear, leer, actualizar, eliminar)?

Modelo 1: iconos

Modelo 2: headerProfesional -> habilidades -> headerProfesional

Modelo 3: objetivos

Modelo 4: proyectos

Modelo 5: certificaciones

8. Servicio


## ✉️ Servicio de Contacto

Modulo de contacto y implementado en el settings.py

9. Middleware

El uso del middleware se encuentra en el  modulo Acounts

Función que desarolla

Protege tu aplicación (CSRF, clickjacking, HTTPS).

Maneja usuarios (autenticación, sesiones, mensajes).

Personaliza flujos (redirección de usuarios autenticados).

Implementado en el settings.py

10. Implementa template fragment caching en alguna sección de la interfaz.

En el modulo home

12. GitHub Actions

Se ejecutaron los test  en git hub action