# ASFProduct

## Descripción

Esta clase describe un único producto del archivo ASF. La clase proporciona metadatos, así como varios métodos útiles para interactuar con el producto.

***

## Atributos
- `properties` _(dict)_: Proporciona metadatos del producto como Modo de Haz, Hora de Inicio, etc.
- `geometry` _(dict)_: Describe las extensiones físicas del producto como un fragmento de geojson.
- `baseline` _(dict)_: Los campos relacionados con la línea base del producto, si están disponibles en CMR.
- `umm` _(dict)_: la respuesta json umm cruda de CMR utilizada para poblar `properties`, `geometry`, `baseline` y `meta`.
- `meta` _(dict)_: el json de metadatos devuelto por CMR.
<!-- netrc
cómo construir archivo netrc, enlace
O autenticación con estas opciones en su lugar -->

***

## Métodos

### <span style="color: #236192; font-size: 20px;">geojson()</span>

`ASFProduct.__str__()` utiliza este método para la serialización a través de `json.dumps()`

**args:**
None

**retorna:**

- `dict` describiendo el producto como un fragmento de geojson.

***

### <span style="color: #236192; font-size: 20px;">download(path, _filename=None, session=None_)</span>

Descarga este producto en la ruta especificada y con el nombre de archivo opcional.

**args:**

- path: El directorio en el cual este producto debe ser descargado.
- filename _(opcional)_: Nombre de archivo a usar en lugar del nombre de archivo original de este producto.
- session _(opcional)_: La sesión a usar, en la mayoría de los casos debe estar autenticada de antemano. Si no se proporciona una sesión, se usará una sesión en blanco (no autenticada).
- fileType _(opcional)_: Usado para descargar metadatos XML de Burst. Especifica ````fileType=asf.FileDownloadType.ADDITIONAL_FILES```` para descargar los metadatos XML. Para descargar archivos .tiff y .xml para bursts, usa ````asf.FileDownloadType.ALL_FILES````
	- Ejemplo: ````burst_results.download(session=session, path="./", fileType=asf.FileDownloadType.ADDITIONAL_FILES)````
	- Nota: Los Metadatos XML de Burst son un archivo generados virtualmente, y por lo tanto no tienen su propio nombre de archivo único. Los Metadatos XML solo se pueden encontrar a través del nombre de la escena de burst.

**retorna:**
None

***

### <span style="color: #236192; font-size: 20px;">stack()</span>

Construye una pila de línea base utilizando este producto como referencia

**args:**

- cmr_provider _(opcional)_: Nombre de proveedor personalizado para restringir los resultados de CMR, para más información sobre cómo se utiliza esto, consulta la [documentación de CMR](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#c-provider)
- session _(opcional)_: Una Sesión a ser utilizada al realizar la búsqueda. Para la mayoría de los usos, se puede ignorar. Utilizado al buscar un conjunto de datos, proveedor, etc. que requiere autenticación. Consulta [ASFSession](/asf_search/ASFSession) para más detalles.
- host _(opcional)_: Host de SearchAPI, por defecto es el SearchAPI de Producción. Esta opción está destinada para propósitos de desarrollo/pruebas y generalmente se puede ignorar.

**retorna:**

- Representación ```ASFSearchResults``` de la pila, con la adición de valores de línea base (temporal, perpendicular) adjuntos a cada `ASFProduct`

***

### <span style="color: #236192; font-size: 20px;">get_stack_opts()</span>

Construye opciones de búsqueda que describen una pila InSAR basada en este producto. Similar a `stack()` pero no realiza la búsqueda, simplemente retorna ```ASFSearchOptions``` que pueden ser inspeccionadas o ajustadas y luego pasadas a varias funciones de búsqueda.

**args:**
None

**retorna:**

- Objeto ```ASFSearchOptions```

***

### <span style="color: #236192; font-size: 20px;">centroid()</span>

Determina el centroide de un producto.

**args:**
None

**retorna:**

- Objeto ```shapely.geometry.point.Point``` describiendo el centroide del producto

<!-- Tendrá más que exportación geojson; añadir esto cuando otras opciones de salida estén disponibles -->

### <span style="color: #236192; font-size: 20px;">remotezip()</span>

retorna un objeto RemoteZip configurado, que permite descargar partes seleccionadas del archivo zip de un producto.
Para más información sobre cómo usar remotezip con asf-search, consulta la sección `Descarga de Productos Individuales` del [cuaderno de ejemplos de jupyter](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/5-Download.ipynb). Para más información sobre el paquete open-source remotezip, consulta <a target="_blank" href="https://github.com/gtsystem/python-remotezip">el repositorio del proyecto remotezip</a>.

**args:**

- `session` _ASFSession_: Un objeto _ASFSession_ autenticado que se utilizará para descargar el producto

**retorna:**

- Objeto```remotezip.RemoteZip``` autenticado con el objeto _ASFSession_ pasado
