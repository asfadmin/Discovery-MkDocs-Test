# Opciones de búsqueda de ASF

## Descripción

Esta clase describe un conjunto de parámetros de búsqueda. Si bien no es necesario utilizar esta clase al construir una búsqueda, puede ser útil, ya que proporciona cierto grado de validación inmediata de parámetros, así como una forma conveniente de manipular y manejar las opciones de búsqueda en general.

Los parámetros de búsqueda específicos se manejan como atributos de objeto. Al intentar agregar un atributo que no es compatible, se generará un KeyError. Si intenta eliminar un atributo, se establecerá en Ninguno. Los parámetros de búsqueda se pueden establecer a través de kwargs en la instancia del objeto, o directamente en un objeto existente utilizando los mecanismos normales.

La conversión a un `dict` solo incluirá opciones de búsqueda que realmente se hayan establecido en un valor utilizable. Es decir, se ignorarán todas las opciones establecidas en '`None`.



## Atributos
- maxResults
- absoluteBurstID
- absoluteOrbit
- asfFrame
- beamMode
- provider
- collectionName
- maxDoppler
- minDoppler
- maxFaradayRotation
- minFaradayRotation
- flightDirection
- flightLine
- fullBurstID
- frame
- granule_list
- product_list
- intersectsWith
- lookDirection
- offNadirAngle
- operaBurstID
- platform
- polarization
- processingLevel
- relativeBurstID
- relativeOrbit
- processingDate
- start
- end
- season
- groupID
- insarStackId
- instrument
- session

***

## Métodos

_ASFSearchOptions no proporciona ningún método destinado al uso directo, sino que depende de un puñado de dunders para el comportamiento deseado. Para mayor claridad, estos se incluyen below._

### <span style="color: #236192; tamaño de fuente: 20px;" >__init__()</span>

Establece los diversos atributos descritos anteriormente y procesa cualquier kwargs en ellos.

**args:**

- _**kwargs_, limitado a los nombres enumerados como atributos anteriores. Cualquier otra cosa generará un `KeyError`

**Retorna:**
None

***

### <span style="color: #236192; font-size: 20px;">__init__()</span>

Establece el atributo denominado por `key` en el `value` especificado después de pasarlo a través de una función de validación adecuada.

Los valores de `None` están permitidos como una forma de anular el atributo. Al intentar establecer una `key` que no aparece en la lista de atributos anterior, se generará un `KeyError`

**args:**

- key: el nombre del atributo a establecer
- value: el valor en el que se debe establecer el atributo nombrado

**Retorna:**
None

***

### <span style="color: #236192; font-size: 20px;">__delattr__()</span>

Borra los nombres de un atributo por `item` configurándolo en `None`

**args:**

- item: el nombre del atributo que se va a borrar

**Retorna:**
None

***

### <span style="color: #236192; font-size: 20px;">__iter__()</span>

Se utiliza al convertir el objeto ASFSearchOptions en objetos más fundamentales, como `dict`

Solo incluye atributos que no son `None`.

**args:**
None

**Rendimientos:**

- (key, value) pares para cada uno de los atributos anteriores que no son `None`

***

