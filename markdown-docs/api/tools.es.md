# Herramientas de API de búsqueda

Las búsquedas se pueden ejecutar de varias maneras, dependiendo de sus necesidades. En esta página, encontrará consejos de sintaxis y codificación de caracteres, y más información sobre algunas de las formas de ejecutar consultas de la API de búsqueda.

## Sintaxis y codificación de caracteres

**Sugerencias de sintaxis**

1. Un "?" separa la URL del punto final de las palabras clave.
2. Las palabras clave van unidas por una "&". Algunos sistemas operativos o programas pueden requerir un "\&"
3. Es posible que no haya espacios ni paréntesis en la cadena de URL. Vea a continuación cómo codificar estos caracteres.

**Codificación de caracteres:**

>espacio
>
> reemplazar por '%20'. Usar '+' en los valores de palabras clave
>
>(
>
>reemplazar con '%28'
>
>)
>
>reemplazar con '%29'
>

Para obtener una lista completa de los códigos URL, consulte [Referencia de codificación de URL](https://www.w3schools.com/tags/ref_urlencode.asp).

**Caracteres que escapan**

Si ejecuta consultas de la API de búsqueda a través de la línea de comandos, es posible que deba escapar caracteres. Escapar de un carácter le dice a la interfaz de línea de comandos que interprete el carácter literalmente. Algunos caracteres que deben escaparse incluyen espacios y ampersands (&).

Para obtener más información sobre los caracteres que escapan, consulte la [Guía de scripting de Bash](https://tldp.org/LDP/abs/html/escapingsection.html). Para los usuarios de Windows, se puede encontrar más información [aquí](https://ss64.com/nt/syntax-esc.html).

## Detalles del programa

Puede usar un programa para ayudarlo con las consultas de la API de búsqueda. Esta sección proporcionará algunos detalles sobre algunos de los programas que puede usar para escribir y ejecutar consultas de API de búsqueda y algunos comandos de ejemplo para cada uno.

- [aria2](https://wiki.archlinux.org/title/aria2)
- [Wget](https://www.gnu.org/software/wget/)
- [cURL](https://curl.se/docs/manpage.html)

Tanto [Wget](http://wget.addictivecode.org/FrequentlyAskedQuestions.html?action=show&redirect=Faq#download) como [cURL](https://curl.se/) se instalan a menudo en sistemas Linux. cURL es parte de Mac OS, y Wget se puede instalar. El sistema operativo Microsoft Windows no viene con ninguno de los dos instalado, pero ambos se pueden descargar. cURL es más fácil de configurar en una máquina con Windows. [aria2] (https://aria2.github.io/) se puede instalar en sistemas Windows, Mac o Linux.

### Ejemplos usando aria2

aria2c se puede utilizar para descargar resultados de la API de búsqueda con un solo comando. Deberá incluir su nombre de usuario y contraseña de Earthdata, todas las palabras clave y valores deseados, y asegurarse de que output = metalink.

**Aria2 — Ejemplo de Linux/Mac - Descargar escena conocida**

      aria2c --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd='CHANGE_ME' "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Aria2 — Ejemplo de Windows - Descargar escena conocida**

      aria2c --check-certificate=false --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd="CHANGE_ME" "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

**Aria2 — Descarga basada en la plataforma y la búsqueda de rango de tiempo**

      aria2c --http-auth-challenge=true --http-user=CHANGE_ME --http-passwd='CHANGE_ME' "https://api.daac.asf.alaska.edu/services/search/param?platform=Sentinel-1A&intersectsWith=point(-122.425 37.77)&start=2016-07-01T00:00:00&output=metalink"

Puede almacenar sus credenciales de inicio de sesión en un archivo de configuración, en lugar de incluirlas en cada comando de descarga.

**aria2 - Ejemplo de Linux/Mac — Crear y usar un archivo de configuración**

      echo 'http-user=CHANGE_ME' >> aria2.conf
      echo 'http-passwd=CHANGE_ME' >> aria2.conf
      chmod 600 aria2.conf

      aria2c --conf-path=aria2.conf --http-auth-challenge=true "https://api.daac.asf.alaska.edu/services/search/param?granule_list=S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4&output=metalink"

Las opciones adicionales de aria2 están disponibles en el [manual de aria2](http://aria2.sourceforge.net/manual/en/html/aria2c.html).

Consulte la documentación completa en [archivos de configuración para aria2](https://aria2.github.io/manual/en/html/aria2c.html#aria2-conf).

### Ejemplos usando Wget

Una vez que tenga la URL de descarga, puede descargar archivos individualmente usando Wget. Puede encontrar la URL de descarga de los resultados deseados utilizando primero las salidas csv, json, metalink o geojson.

**Wget - Ejemplo de Linux/Mac — Descargar un archivo**

      wget -c --http-user=CHANGE_ME --http-password='CHANGE_ME' "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

**Wget - Ejemplo de Windows — Descargar un archivo**

      wget --check-certificate=off -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

      wget -c --http-user=CHANGE_ME --http-password="CHANGE_ME" "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

Puede almacenar sus credenciales de inicio de sesión en un archivo de configuración, en lugar de incluirlas en cada comando de descarga.

**Wget - Ejemplo de Linux/Mac — Crear y usar un archivo de configuración**

      echo 'http_user=CHANGE_ME' >> wget.conf
      echo 'http_password=CHANGE_ME' >> wget.conf
      chmod 600 wget.conf

      export WGETRC="wget.conf"
      wget -c "https://datapool.asf.alaska.edu/GRD_MD/SA/S1A_EW_GRDM_1SDH_20151003T040339_20151003T040443_007983_00B2A6_DDE4.zip"

También puede enviar resultados a un archivo en su PC

**Ejemplo: resultados de consulta enviados a un archivo de metavínculo**

      wget -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?intersectsWith=point%28-119.543+37.925%29\&platform=ALOS\&output=metalink

**Ejemplo de visualización - Mac/Linux**

      wget -O myfilename.kml https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=KML

**Descargar ejemplo - Windows**

      wget -c -O myfilename.metalink https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550\&output=METALINK

Las opciones adicionales de Wget están disponibles en el [Manual de GNU Wget](https://www.gnu.org/software/wget/manual/wget.html).

Consulte la documentación completa en [archivos de configuración para Wget](https://www.gnu.org/software/wget/manual/html_node/Startup-File.html#Startup-File).

### Ejemplos usando cURL

**cURL - Ejemplo de Mac/Linux**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=R1\&absoluteOrbit=25234\&output=CSV

**cURL - Ejemplo de Windows**

Nota: Copiar/pegar comillas a veces causa errores. Elimine y vuelva a escribir las comillas después de pegarlas.

      rizo "https://api.daac.asf.alaska.edu/services/search/param?platform=R1&absoluteOrbit=25234&output=CSV" > minombre.csv

También puede enviar resultados a un archivo en su PC

**Ejemplo de Mac/Linux: resultados de consulta enviados a un archivo de metavínculo**

      curl https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750 >minombredearchivo.metalink

**Ejemplo de Windows: resultados de consulta enviados a un archivo de metavínculo**

      curl "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP021910740,ALPSRP085800750" > minombredearchivo.metalink

**Ejemplo de búsqueda - Mac/Linux**

      curl https://api.daac.asf.alaska.edu/services/search/param?platform=r1\&asfframe=300\&output=CSV > myfilename.csv

**Ejemplo de búsqueda - Windows**

      rizo "https://api.daac.asf.alaska.edu/services/search/param?platform=r1&asfframe=300&output=CSV" > minombre.csv

**Ejemplo de visualización - Windows**

      rizo "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=KML" >minombre.kml

**Descargar ejemplo - Windows**

      curl -L "https://api.daac.asf.alaska.edu/services/search/param?granule_list=ALPSRP074606580,ALPSRP077086550&output=METALINK" >minombredearchivo.metalink

## Solicitudes POST
Algunas palabras clave y puntos finales aceptarán una solicitud POST. Los ejemplos de POST a continuación usan cURL.

**Ejemplo POST - Salida WKT del archivo**

      curl -X POST -F 'files=@/path/to/file.geojson' 'https://api.daac.asf.alaska.edu/services/utils/files_to_wkt'

**Ejemplos POST - se cruzaCon palabra clave**

      curl -X POST -F 'intersectsWith=LINESTRING(-97.1191 26.4312,-95.5371 29.1522,-83.7598 29.993,-81.5625 25.4036)' 'https://api.daac.asf.alaska.edu/services/search/param'

Puede agregar parámetros adicionales a su solicitud POST con el argumento -F para cada parámetro deseado.

      curl -X POST -F 'platform=S1' -F 'output=geojson' -F 'maxresults=10' -F 'intersectsWith=POINT(-102.4805 38.7541)' 'https://api.daac.asf.alaska.edu/services/search/param'

Para obtener más información, consulte [Solicitudes POST](https://en.wikipedia.org/wiki/POST_(HTTP))

## Navegador web

Puede ejecutar las consultas de la API de búsqueda directamente en un navegador web de su elección. Simplemente copie y pegue la consulta en un navegador web. Cualquier error será devuelto en formato JSON.

Deberá utilizar la codificación de URL para espacios y paréntesis. Consulte la sección Codificación de caracteres o consulte [Referencia de codificación de URL](https://www.w3schools.com/tags/ref_urlencode.asp) para obtener más detalles.


