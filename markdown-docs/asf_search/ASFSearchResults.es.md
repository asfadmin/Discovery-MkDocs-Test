# ASFSearchResults

## Descripción

Esta clase describe un conjunto de resultados de búsqueda del archivo ASF. La clase proporciona una forma conveniente de administrar y examinar los resultados de búsqueda, así como la funcionalidad de exportación y descarga.

***

## Atributos
- `searchOptions` _(ASFSearchOptions)_: Las opciones de búsqueda utilizadas para generar este conjunto de resultados. Puede ser `None` en algunos casos.
- `searchComplete` _(bool)_: Bandera que indica que `asf_search.search()` completó con éxito la recopilación de resultados de CMR. 
***

## Métodos

### <span style="color: #236192; font-size: 20px;">download()</span>

Itera sobre cada ```ASFProduct``` y los descarga en la ruta especificada.

**args:**

- path: El directorio en el cual los productos deben ser descargados.
- session: La sesión a usar, en la mayoría de los casos debe estar autenticada de antemano.
- processes: Número de procesos de descarga a usar. Por defecto es 1 (es decir, descarga secuencial)
- fileType _(opcional)_: Usado para descargar metadatos XML de Burst. Especifica ````fileType=asf.FileDownloadType.ADDITIONAL_FILES```` para descargar los metadatos XML. Para descargar archivos .tiff y .xml para bursts, usa ````asf.FileDownloadType.ALL_FILES````
	- Ejemplo: ````burst_results.download(session=session, path="./", fileType=asf.FileDownloadType.ADDITIONAL_FILES)````
	- Nota: Los Metadatos XML de Burst son un archivo generados virtualmente, y por lo tanto no tienen su propio nombre de archivo único. Los Metadatos XML solo se pueden encontrar a través del nombre de la escena de burst.

**retorna:** None

***

### <span style="color: #236192; font-size: 20px;">geojson()</span>

`ASFSearchResults.__str__()` utiliza este método para la serialización a través de `json.dumps()`

**args:** None

**retorna:**

- `dict` describiendo los resultados de búsqueda como un objeto geojson.

### <span style="color: #236192; font-size: 20px;">csv()</span>

Crea un generador de cadenas en formato csv a partir de los resultados

**args:** None

**retorna:**

- Un generador de cadenas en formato csv

### <span style="color: #236192; font-size: 20px;">kml()</span>

Crea un generador de cadenas en formato kml a partir de los resultados

**args:** None

**retorna:**

- Un generador de cadenas en formato kml

### <span style="color: #236192; font-size: 20px;">metalink()</span>

Crea un generador de cadenas en formato metalink a partir de los resultados

**args:** None

**retorna:**

- Un generador de cadenas en formato metalink

### <span style="color: #236192; font-size: 20px;">raise_if_incomplete()</span>

Utilizado para verificar si los resultados devueltos por `asf_search.search()` están incompletos (esto puede suceder si 
ocurre un error al consultar CMR)

**args:** None

**lanza:**

- Lanza un `asf_search.exceptions.ASFSearchError` si los resultados están incompletos
