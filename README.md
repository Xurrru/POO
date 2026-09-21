# POO
Semestre 2-IEC-Programación orientada a objetos seguro

## Markdown

---

### Configuración Inicial de Git

Antes de trabajar con Git en tu equipo, es necesario identificar el usuario y correo electrónico que se asociarán a tus modificaciones.

*   `git config --global user.name "nombre_github"`  
    * **Explicación:** Configura tu nombre de usuario a nivel global en tu equipo. Este nombre aparecerá como el autor de las modificaciones o commits que realices.
*   `git config --global user.email "email_github"`  
    * **Explicación:** Define el correo electrónico asociado a tu cuenta de GitHub. Es indispensable para que la plataforma vincule tus commits locales con tu perfil de usuario.
*   `git config --global --list`  
    * **Explicación:** Lista todas las configuraciones globales que se han establecido previamente (incluyendo tu nombre, email y otras preferencias), permitiendo verificar que los datos ingresados sean correctos.

---

### Obtener un Repositorio

*   `git clone url_repo .`  
    * **Explicación:** Copia (descarga) un repositorio remoto alojado en GitHub hacia tu máquina local. Al agregar el punto (`.`) al final, el contenido se descarga directamente en la carpeta actual sin crear una subcarpeta adicional.

---

### Flujo de Trabajo y Control de Versiones

*   `git add .`  
    * **Explicación:** Prepara los archivos (área de *Staging*). El punto (`.`) le indica a Git que incluya **todos** los archivos modificados, creados o eliminados del directorio actual para que formen parte del próximo punto de guardado.
*   `git commit -m "comentario"`  
    * **Explicación:** Crea un punto de guardado (*commit*) en el historial local con los cambios preparados en el paso anterior. El parámetro `-m` permite adjuntar un mensaje descriptivo indicando qué se hizo en este cambio.
*   `git push origin main`  
    * **Explicación:** Sube (*push*) todos los commits o puntos de guardado locales al servidor remoto en GitHub (`origin`), enviando los cambios a la rama principal (`main`).