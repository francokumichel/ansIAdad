# ansIAdad 😰

### Introducción
Por el momento, nos encontramos definiendo objetivos y dando forma a la idea que tenemos, paciencia 🙏 

### Consideraciones para el desarrollo✍️

Se organiza el trabajo en dos ramas principales:

- **main**: Cualquier commit que se realice en esta rama debe estar preparado para subir a producción. 

- **development**: En esta rama estará el código que conformará la siguiente versión del proyecto.

La idea es que cada vez que se incorpore nuevo código a main, sea una nueva versión del proyecto.

Además utilizaremos diferentes ramas auxiliares, aunque por el momento nos limitaremos a utilizar **features** para agregar nuevas funcionalidades a la aplicación.

- **Feature**: Estas ramas la utilizaremos para agregar nuevas características a nuestra aplicación. Estas ramas se van a generar a partir de development y se van a agregar también a development y su nomenclatura será *feature/<nombre-funcionalidad>*

Veamos con un ejemplo como sería el flujo normal de trabajo. Supongamos que queremos empezar a trabajar en una nueva funcionalidad, entonces lo que debemos hacer es ir a la rama development y crear una nueva rama a partir de esta con la nomenclatura antes dicha.

```bash
    # En caso de que no estemos ubicados en la rama development, cambiamos hacia esta rama
    git checkout development 
    # Nunca debemos olvidarnos de consultar por nuevos cambios en la rama development :/
    git pull origin development
    # Ahora creamos la rama donde vamos a desarrollar la nueva funcionalidad estando ubicados en development
    git checkout -b feature/nueva-funcionalidad
```

Una vez realizado esto, ya estaremos ubicados en nuestra nueva rama y podremos comenzar con el desarrollo de la nueva catacterística.

Bien, ahora supongamos que paso un tiempo, desarrollamos nuestra nueva funcionalidad y ya esta finalizada. Ahora lo que queremos es subirla a development. ¿Como logramos esto sin caer en el problema de lidiar con mergeos interminables o peor aún, de sobrescribir trabajo de otro integrante del grupo?. La forma que más me ha funcionado en este sentido es siguiendo este flujo:

```bash
    # Antes que nada, hay que ir a development y asegurarse de que la rama este actualizada con los últimos cambios
    git pull origin development
    
    # Nos trasladamos a nuestra rama donde estuvimos desarrollando la nueva funcionalidad
    git checkout feature/nueva-funcionalidad

    # Hacemos el merge en nuestra rama local donde estuvimos haciendo el desarrollo. ¿Y esto por qué?, pues si hay problemas muy engorrosos de merge o nos equivocamos de alguna forma, lo solucionamos en nuestra rama local y no afectamos a la rama development que usa todo el equipo de desarrollo
    git merge development

    # Si hubo problemas de merge que solucionar, vamos a tener que agregarlos y commitear, sino pusheamos nomas
    git push origin feature/nueva-funcionalidad

    # Ahora vamos a la rama development, opcionalmente habría que fijarse si es que alguien no subio nuevos cambios a esta rama
    git checkout development
    git pull origin development

    # Ahora solo queda agregar la nueva funcionalidad fusionando la rama donde desarrollamos la nueva funcionalidad con development
    git merge feature/nueva-funcionalidad

    # No debería haber problemas de merge, por lo que pusheamos nomas
    git push origin development
```

Y tachan!, ya agregamos nuestra nueva funcionalidad a la aplicación. Cabe aclarar que este es el flujo que yo sigo normalmente en proyectos no super grandes y complejos. Para el ambito del presente proyecto creo que es la forma mas idónea de encararlo.