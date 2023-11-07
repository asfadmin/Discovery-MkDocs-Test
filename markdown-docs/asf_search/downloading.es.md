#Descarga

## Autenticación de sesión

asf_search admite la descarga de datos, tanto de los resultados de búsqueda proporcionados por las funciones de búsqueda, como directamente en las URL de los productos. Por lo general, se requiere una sesión autenticada. asf_search utiliza ```Solicitudes```. El uso de credenciales .netrc es el método preferido para la autenticación. Puede encontrar más información sobre la autenticación .netrc [aquí](https://requests.readthedocs.io/en/latest/user/authentication/#netrc-authentication).

Ejemplo usando .netrc:

	results = ....
	results.download(path='....')

Si no utiliza credenciales .netrc, puede autenticarse mediante un objeto ```ASFSession``` y uno de los siguientes métodos de autenticación. ```ASFSession``` es una subclase de ```Session```. La sesión debe pasarse a cualquier método de descarga al que se llame, se puede reutilizar y es seguro para subprocesos. 

- ```auth_with_creds('user', 'pass)```
- ```auth_with_token('EDL token')```
- ```auth_with_cookiejar(http.cookiejar)```

Ejemplo con autenticación manual:

	results = asf_search.granule_search([...])
	session = asf_search.ASFSession().auth_with_creds('user', 'pass')
	results.download(path='/Users/SARGuru/data', session=session)

asf_search también admite la descarga de una lista arbitraria de URL. Se admiten todos los métodos de autenticación disponibles:

	urls = [...]
	asf_search.download_urls(urls=urls, path='/Users/SARGuru/data', session=ASFSession().auth_with_token('EDL token'))

Tenga en cuenta también que ```ASFSearchResults.download()``` y la función genérica ```download_urls()``` aceptan un parámetro ```procesos``` que permite descargas paralelas.

## Métodos
### <span style="color: #236192; tamaño de fuente: 20px;" >download_urls()</span>

Descarga todos los productos de las direcciones URL especificadas a la ubicación especificada.

**args**

- urls: Lista de URLs desde las que descargar
- path: ruta local en la que guardar el producto
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano
- processes: Número de procesos de descarga a utilizar. El valor predeterminado es 1 (es decir, descarga secuencial)

### <span style="color: #236192; tamaño de fuente: 20px;" >download_url()</span>

Descarga un producto desde la dirección URL especificada a la ubicación especificada y al nombre de archivo (opcional).

**args**

- url: URL desde la que descargar
- path: ruta local en la que guardar el producto
- filename: Nombre de archivo opcional a utilizar, extraído de la URL por defecto
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano

### <span style="color: #236192; tamaño de fuente: 20px;" >remotezip()</span>

Configura y devuelve un objeto ```remotezip.RemoteZip```, que permite descargar
Archivos específicos de un archivo zip determinado sin descargar todo el archivo.

**args**

- url: URL desde la que descargar un archivo zip
- sesión: ```ASFSession``` autenticado que RemoteZip usará para descargar desde el producto zip

**Devuelve:**

- `remotezip.RemoteZip` autenticado con el objeto _ASFSession_ pasado

## Formatos de exportación
asf_search proporciona varios formatos de exportación, además del formato de asf_search predeterminado. Los formatos disponibles son: geojson, csv, metalink, kml, jsonlite, jsonlite2.

Ejemplos:

	results = ....
	with open("search_results.csv", "w") as f:
		f.writelines(results.csv())

	results = ....
	with open("search_results_jsonlite.json", "w") as f:
		f.writelines(results.jsonlite())

# ResultadosdelabúsquedadeASF

## Descripción

Esta clase describe un conjunto de resultados de búsqueda del archivo ASF. La clase proporciona una forma conveniente de administrar y examinar los resultados de búsqueda, así como la funcionalidad de exportación y descarga.

***

## Atributos
- 'searchOptions' _(ASFSearchOptions)_: Las opciones de búsqueda utilizadas para generar este conjunto de resultados. Puede ser 'Ninguno' en algunos casos.
- 'searchComplete' _(bool)_: Bandera que significa 'asf_search.search()' completada con éxito recopilando resultados de CMR. 
***

## Métodos

### <span style="color: #236192; tamaño de fuente: 20px;" >download()</span>

Itera sobre cada ''ASFProduct''' y los descarga en la ruta especificada.

**args:**

- ruta: El directorio en el que se deben descargar los productos.
- sesión: La sesión a utilizar, en la mayoría de los casos debe ser autenticada de antemano.
- procesos: Número de procesos de descarga a utilizar. El valor predeterminado es 1 (es decir, descarga secuencial)
- fileType _(opcional)_: Se utiliza para descargar metadatos XML de Burst. Especifique '''fileType=asf. FileDownloadType.ADDITIONAL_FILES'''' para descargar los metadatos XML. Para descargar archivos .tiff y .xml para ráfagas, use '''asf. FileDownloadType.ALL_FILES''''
	- Ejemplo: ''''burst_results.download(session=session, path="./", fileType=asf. FileDownloadType.ADDITIONAL_FILES)''''
	- Nota: Los metadatos XML de ráfaga son un archivo generado virtualmente y, por lo tanto, no tienen su propio nombre de archivo único. Los metadatos XML solo se pueden encontrar a través del nombre de la escena de ráfaga.

**devoluciones:** Ninguna

***

### <span style="color: #236192; tamaño de fuente: 20px;" >geojson()</span>

'ASFSearchResults.__str__()' utiliza este método para la serialización a través de 'json.dumps()'

**args:** Ninguno

**Devuelve:**

- 'dict' que describe los resultados de la búsqueda como un objeto geojson.

### <span style="color: #236192; tamaño de fuente: 20px;" >csv()</span>

Crea un generador de cadenas con formato csv a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato csv

### <span style="color: #236192; tamaño de fuente: 20px;" >kml()</span>

Crea un generador de cadenas con formato KML a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato kml

### <span style="color: #236192; tamaño de fuente: 20px;" >metalink()</span>

Crea un generador de cadenas con formato de metavínculo a partir de los resultados

**args:** Ninguno

**Devuelve:**

- Un generador de cadenas con formato de metavínculo

### <span style="color: #236192; tamaño de fuente: 20px;" >raise_if_incomplete()</span>

Utilícelo para comprobar si los resultados devueltos por 'asf_search.search()' están incompletos (esto puede suceder
si se produce un error al consultar CMR)

**args:** Ninguno

**Plantea:**

- Genera un 'asf_search.exceptions.ASFSearchError' si los resultados están incompletos
