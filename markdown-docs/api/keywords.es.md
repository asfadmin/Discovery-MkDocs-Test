# Palabras Clave de la API de Búsqueda

Considere usar nuestro nuevo módulo de Python, asf_search. asf_search puede ser utilizado para realizar búsquedas en el catálogo de ASF, y ofrece funcionalidad básica y soporte de descarga. Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Actualmente, proporcionamos constantes para plataforma, instrumento, modo de haz, dirección de vuelo, polarización y nivel de procesamiento. Se puede encontrar más información [aquí](/asf_search/basics).

Las palabras clave se utilizan para encontrar los datos deseados. Utilice tantas o tan pocas palabras clave como necesite. A continuación se enumeran las palabras clave disponibles y sus descripciones para cada punto de acceso de la API de Búsqueda. Las palabras clave son sensibles a mayúsculas y minúsculas.

*Nota:* Cualquier error se devolverá en formato JSON.

## Punto de Acceso de Búsqueda
<https://api.daac.asf.alaska.edu/services/search/param>

### Parámetros del Conjunto de Datos
- <span style="color: #236192; font-size: 20px;">dataset</span>
	- Esta es la palabra clave alternativa preferida para búsquedas de 'plataforma'.
	- Plataforma de teledetección que adquirió los datos. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- dataset=SENTINEL-1
		- dataset=OPERA-S1
		- dataset=AIRSAR,UAVSAR
	- Valores:
		- [SENTINEL-1](/datasets/using_ASF_data/#sentinel-1), [SLC-BURST](/datasets/using_ASF_data/#sentinel-1-bursts), [OPERA-S1](/datasets/using_ASF_data/#opera-sentinel-1), [ALOS PALSAR](/datasets/using_ASF_data/#alos-palsar), [ALOS AVNIR-2](/datasets/using_ASF_data/#alos-avnir-2), [SIR-C](/datasets/using_ASF_data/#sir-c), [ARIA S1 GUNW](/datasets/using_ASF_data/#aria-s1-gunw), [SMAP](/datasets/using_ASF_data/#smap-soil-moisture-active-passive), [UAVSAR](/datasets/using_ASF_data/#uavsar), [RADARSAT-1](/datasets/using_ASF_data/#radarsat-1), [ERS](/datasets/using_ASF_data/#ers), [JERS-1](/datasets/using_ASF_data/#jers), [AIRSAR](/datasets/using_ASF_data/#airsar), [SEASAT](/datasets/using_ASF_data/#seasat)

- <span style="color: #236192; font-size: 20px;">platform</span>
	- Véase también 'dataset'. Dataset es la palabra clave preferida cuando sea posible.
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- Véase también 'instrument'
	- Plataforma de teledetección que adquirió los datos. Sentinel-1 y ERS tienen múltiples plataformas de teledetección, y puede elegir si especificar una plataforma específica. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- platform=ALOS
		- platform=SA,SB
		- platform=S1
	- Valores:
		- ALOS, A3, AIRSAR, AS, ERS, ERS-1, E1, ERS-2, E2, JERS-1, J1, RADARSAT-1, R1, SEASAT, SS, S1, Sentinel, Sentinel-1, Sentinel-1A, SA, Sentinel-1B, Sentinel-1 Interferogram (BETA), SB, SIR-C, SMAP, SP, UAVSAR, UA

- <span style="color: #236192; font-size: 20px;">instrument</span>
	- Véase también 'dataset'. 'Dataset' es la palabra clave preferida cuando sea posible.
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- Véase también 'platform'
	- Instrumento de teledetección que adquirió los datos. Para algunas plataformas, como ALOS, hay múltiples instrumentos para elegir.
	- Ejemplo:
		- ALOS: instrument=PALSAR
		- ALOS: instrument=AVNIR-2
	- Valores:
		- C-SAR, PALSAR, AVNIR-2

- <span style="color: #236192; font-size: 20px;">absoluteOrbit</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Para ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, Sentinel-1A y Sentinel-1B, este valor corresponde al conteo de órbitas dentro del ciclo de órbita. Para UAVSAR, es el [ID de Vuelo](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035). Puede especificar un solo valor, un rango de valores o una lista de valores.
	- Ejemplo:
		- RADARS absoluteOrbit=25436
		- PALSAR: absoluteOrbit=25436-25445,25450
		- UAVSAR: absoluteOrbit=12006

- <span style="color: #236192; font-size: 20px;">asfframe</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Véase también 'frame'
	- Esto es principalmente una referencia de marco de ASF / [JAXA](https://global.jaxa.jp/). Sin embargo, algunas plataformas utilizan otras convenciones. Puede especificar un solo valor, un rango de valores o una lista de valores.
	- Ejemplo:
		- asfframe=300 o asfframe=2845-2855 o asfframe=2800,2845-2855
	- Valores:
		- ERS, JERS, RADARSAT: marcos ASF de 0 a 900
		- ALOS PALSAR: marcos JAXA de 0 a 7200
		- SEASAT: marcos tipo ESA de 0208 a 3458 (debe usar un cero delante para marcos 208-999)
		- Sentinel-1: Valores internos de 0 a 1184
      
- <span style="color: #236192; font-size: 20px;">maxBaselinePerp</span>
	- Para el análisis SAR interferométrico (InSAR), la Baseline Perpendicular es la distancia espacial entre las primeras y segundas observaciones medidas perpendicularmente a la dirección de observación del satélite y proporciona una indicación de la sensibilidad a la altura topográfica.
	- Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
	- Ejemplo:
		- maxBaselinePerp=1500 o maxBaselinePerp=50.5

- <span style="color: #236192; font-size: 20px;">minBaselinePerp</span>
	- Para el análisis SAR interferométrico (InSAR), la Baseline Perpendicular es la distancia espacial entre las primeras y segundas observaciones medidas perpendicularmente a la dirección de observación del satélite y proporciona una indicación de la sensibilidad a la altura topográfica.
	- Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
	- Ejemplo:
		- minBaselinePerp=100 o minBaselinePerp=50.5

- <span style="color: #236192; font-size: 20px;">beamMode</span>
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- El modo de haz utilizado para adquirir los datos. Véase también beamSwath. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- beamMode=FBS o beamMode=EW,IW o beamMode=ScanSAR+Wide
	- Valores:
		- AIRSAR: 3FP, ATI, XTI
		- ALOS: FBD, FBS, PLR, WB1, WB2, DSN
		- ERS-1: Estándar, STD
		- ERS-2: Estándar, STD
		- JERS-1: Estándar, STD
		- RADARSAT-1: Estándar, STD, Fine, High, Low, Wide, Narrow, ScanSAR+Wide, ScanSAR+Narrow
		- SEASAT: Estándar, STD
		- SMAP: Estándar, STD
		- Sentinel-1A: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- Sentinel-1B: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- UAVSAR: POL, RPI
      
- <span style="color: #236192; font-size: 20px;">beamSwath</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- BeamSwath abarca un ángulo de observación y un modo de haz. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- beamSwath=0
		- beamSwath=FN1, FN2, FN3, FN4, FN5
	- Valores:
		- AIRSAR: 3FP, ATI, XTI
		- ALOS: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20
		- ERS-1: STD
		- ERS-2: STD
		- JERS-1: STD
		- RADARSAT-1: FN1, FN2, FN3, FN4, FN5, SNA, SNB, ST1, ST2, ST3, ST4, ST5, ST6, ST7, SWA, SWB, WD1, WD2, WD3, EH3, EH4, EH6, EL1
		- SEASAT: STD
		- Sentinel-1A: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- Sentinel-1B: EW, IW, S1, S2, S3, S4, S5, S6, WV
		- UAVSAR: POL, RPI

- <span style="color: #236192; font-size: 20px;">collectionName</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Solo para colecciones de datos de UAVSAR y AIRSAR. Busque por el nombre de la misión/campaña. Puede especificar un solo valor. Para una lista de colecciones disponibles, consulte el Punto de Acceso de Lista de Misiones a continuación.
	- Ejemplo:
		- UAVSAR: collectionName=ABoVE
		- AIRSAR: collectionName=collectionName=Akiyoshi,+Japan

- <span style="color: #236192; font-size: 20px;">maxDoppler</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Doppler proporciona una indicación de cuánto se desvía la dirección de observación de la adquisición ideal en dirección de vuelo perpendicular.
	- Ejemplo:
		- maxDoppler=1500 o maxDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">minDoppler</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Doppler proporciona una indicación de cuánto se desvía la dirección de observación de la adquisición ideal en dirección de vuelo perpendicular.
	- Ejemplo:
		- minDoppler=100 o minDoppler=1500.5

- <span style="color: #236192; font-size: 20px;">maxFaradayRotation</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- La rotación del plano de polarización de la señal de radar afecta la imagen. Las señales HH y HV se mezclan. Rotaciones unidireccionales que superen los 5° probablemente reducirán significativamente la precisión en la recuperación de parámetros geofísicos, como la biomasa forestal.
	- Ejemplo:
		- maxFaradayRotation=3.5

- <span style="color: #236192; font-size: 20px;">minFaradayRotation</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- La rotación del plano de polarización de la señal de radar afecta la imagen. Las señales HH y HV se mezclan. Rotaciones unidireccionales que superen los 5° probablemente reducirán significativamente la precisión en la recuperación de parámetros geofísicos, como la biomasa forestal.
	- Ejemplo:
		- minFaradayRotation=2

- <span style="color: #236192; font-size: 20px;">flightDirection</span>
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- Dirección de la órbita del satélite durante la adquisición de datos. Puede especificar un solo valor.
	- Ejemplo:
		- flightDirection=DESCENDING
	- Valores:
		- A, ASC, ASCENDING, D, DESC, DESCENDING

- <span style="color: #236192; font-size: 20px;">flightLine</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Especifique una línea de vuelo para UAVSAR o AIRSAR. Puede especificar un solo valor.
	- Ejemplo:
		- UAVSAR: flightLine=05901
		- AIRSAR: flightLine=gilmorecreek045-1.93044

- <span style="color: #236192; font-size: 20px;">frame</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Véase también 'asfframe'
	- Los marcos de referencia de la ESA se ofrecen para proporcionar a los usuarios una convención de enmarcado universal. Cada marco de la ESA tiene asignado un marco correspondiente de ASF. Puede especificar un solo valor, un rango de valores o una lista de valores.
	- Ejemplo:
		- frame=300
		- frame=300-400
		- frame=300,303,305
		- frame=300,303,305-315
	- Valores:
		- Cualquier número del 0 al 7200.

- <span style="color: #236192; font-size: 20px;">fullBurstID</span>
    - Utilizado para [productos de ráfaga](/datasets/using_ASF_data/#sentinel-1-bursts) de Sentinel-1. Cada valor representa todos los productos de ráfaga sobre una única sub-banda, correspondiendo a un apilado casi perfecto alineado con el marco. Este valor es útil para el apilado de líneas base. Puede especificar un solo valor o una lista de valores.
    - Ejemplo:
        - valor único: fullBurstID=017_034465_IW2
        - lista de valores: fullBurstID=017_034465_IW2,079_167884_IW1

- <span style="color: #236192; font-size: 20px;">granule_list</span>
	- Lista separada por comas de escenas específicas (gránulos). Las listas grandes necesitarán utilizar una [solicitud POST](https://es.wikipedia.org/wiki/POST_(HTTP)).
	- granule_list no puede ser utilizada en conjunción con otras palabras clave, sin embargo, puede ser utilizada con la palabra clave de salida.
	- Ejemplo:
		- granule_list=ALPSRP111041130,
		S1B_IW_GRDH_1SDV_20161124T032008_20161124T032033_003095_005430_9906

- <span style="color: #236192; font-size: 20px;">groupid</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Lista separada por comas de identificadores de grupo específicos. Para algunos conjuntos de datos, el identificador de grupo es el mismo que el nombre de la escena. Para otros, como Sentinel-1, el identificador de grupo es único para un grupo de escenas. El valor del identificador de grupo se incluye en las salidas GeoJSON, JSON y CSV.
	- Ejemplo:
		- groupid=S1A_IWDV_0112_0118_037147_150

- <span style="color: #236192; font-size: 20px;">lookDirection</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Dirección izquierda o derecha de la adquisición de datos. Puede especificar un solo valor.
	- Ejemplo:
		- lookDirection=L
	- Valores:
		- R, DERECHA, L, IZQUIERDA

- <span style="color: #236192; font-size: 20px;">maxInsarStackSize</span>
	- Un conjunto InSAR está compuesto por todos los granos SAR que cubren la misma región geográfica, son de la misma plataforma y fueron adquiridos con el mismo modo de haz, ángulo de visión y ancho de banda. Para obtener conjuntos InSAR que contengan un cierto número de granos SAR, especifique un mínimo, máximo o ambos.
	- Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
	- Ejemplo:
		- maxInsarStackSize=175

- <span style="color: #236192; font-size: 20px;">minInsarStackSize</span>
	- Un conjunto InSAR está compuesto por todos los granos SAR que cubren la misma región geográfica, son de la misma plataforma y fueron adquiridos con el mismo modo de haz, ángulo de visión y ancho de banda. Para obtener conjuntos InSAR que contengan un cierto número de granos SAR, especifique un mínimo, máximo o ambos.
	- Funciona para ERS-1, ERS-2, JERS, RADARSAT-1, ALOS PALSAR. (No para Sentinel-1)
	- Ejemplo:
		- minInsarStackSize=20

- <span style="color: #236192; font-size: 20px;">offNadirAngle</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Ángulos fuera de nadir para ALOS PALSAR. Puede especificar un solo valor, un rango de valores o una lista de valores.
	- Ejemplo:
		- offNadirAngle=21.5
		- offNadirAngle=9.7-14
		- offNadirAngle=21.5,23.1,20.5-24.2
	- Valores:
		- Más comunes: 21.5, 23.1, 27.1, 34.3
		- Otros: 9.7, 9.9, 13.8, 14, 16.2, 17.3, 17.9, 18, 19.2, 20.5, 21.5, 23.1, 24.2, 24.6, 25.2, 25.8, 25.9, 26.2, 27.1, 28.8, 30.8, 34.3, 36.9, 38.8, 41.5, 43.4, 45.2, 46.6, 47.8, 49, 50, 50.8

- <span style="color: #236192; font-size: 20px;">operaBurstID</span>
    - Utilizado para [productos Opera-S1](/datasets/using_ASF_data/#opera-sentinel-1). Cada valor identifica la ráfaga específica para el producto. Puede especificar un solo valor o una lista de valores.
    - Ejemplo:
        - valor único: operaBurstID=T078-165486-IW2
        - lista de valores: operaBurstID=T078_165486_IW2, T078_165485_IW2

- <span style="color: #236192; font-size: 20px;">polarization</span>
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- Una propiedad de las ondas electromagnéticas SAR que se puede utilizar para extraer información significativa sobre las propiedades de la superficie de la Tierra. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- polarization=VV
		- polarization=VV,HH
		- polarization=VV+VH
		- polarization=Dual+VV
	- Valores:
		- AIRSAR: FULL
		- ALOS: CUADRATURA, HH+5SCAN, HH, HH+4SCAN, VV, HH+3SCAN, FULL, HH+HV, VV+VH
		- ERS-1: VV
		- ERS-2: VV
		- JERS-1: HH
		- RADARSAT-1: HH
		- SEASAT: HH
		- Sentinel-1A: VV, VV+VH, Dual VV, VV+VH, Dual HV, HH, HH+HV, VV, Dual VH
		- Sentinel-1B: VV, VV+VH, Dual VV, VV+VH, Dual HV, HH, HH+HV, VV, Dual VH
		- UAVSAR: FULL, HH

- <span style="color: #236192; font-size: 20px;">processingLevel</span>
	- Esta palabra clave tiene constantes proporcionadas a través de asf_search. Se puede encontrar más información [aquí](/asf_search/searching/#keywords).
	- Nivel al que se han procesado los datos, también tipo de producto. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- processingLevel=L0,L1
	- Valores:
		- AIRSAR: 3FP, LTIF, PTIF, CTIF, PSTOKES, DEM, CSTOKES, JPG, LSTOKES
		- ALOS: L1.0, L1.1, L1.5, L2.2, RTC_LOW_RES, RTC_HI_RES, KMZ
		- ERS-1: L0, L1
		- ERS-2: L0, L1
		- JERS-1: L0, L1
		- RADARSAT-1: L0, L1
		- SEASAT: L1
		- Sentinel-1A: GRD_HS, GRD_HD, GRD_MS, GRD_MD, GRD_FD, SLC, RAW, OCN, METADATA_RAW, METADATA_SLC, METADATA_GRD_HD, METADATA_GRD_MD, METADATA_GRD_MS, METADATA_GRD_HS, METADATA_OCN
		- Sentinel-1B: GRD_HS, GRD_HD, GRD_MS, GRD_MD, GRD_FD, SLC, RAW, OCN, METADATA_RAW, METADATA_SLC, METADATA_GRD_HD, METADATA_GRD_MD, METADATA_GRD_MS, METADATA_GRD_HS, METADATA_OCN
		- Sentinel-1 InSAR: GUNW_STD, GUNW_AMP, GUNW_CON, GUN_COH, GUNW_UNW
		- SMAP: L1A_Radar_RO_QA, L1A_Radar_RO_HDF5, L1B_S0_LoRes_HDF5, L1B_S0_LoRes_QA, L1B_S0_LoRes_ISO_XML, L1A_Radar_QA, L1A_Radar_RO_ISO_XML, L1C_S0_HiRes_ISO_XML, L1C_S0_HiRes_QA, L1C_S0_HiRes_HDF5, L1A_Radar_HDF5
		- UAVSAR: KMZ, PROYECTADO, PAULI, PROYECTADO_ML5X5, STOKES, AMPLITUD, COMPLEJO, DEM_TIFF, PROYECTADO_ML3X3, METADATOS, AMPLITUD_GRD, INTERFEROMETRÍA, INTERFEROMETRÍA_GRD, INC, PENDIENTE

- <span style="color: #236192; font-size: 20px;">product_list</span>
	- Lista separada por comas de archivos específicos (productos). Las listas grandes necesitarán utilizar una [solicitud POST](https://en.wikipedia.org/wiki/POST_(HTTP)). Puede encontrar los valores de product_list para cualquier archivo en las salidas GeoJSON (fileID) o JSON (product_file_id). También está disponible desde CMR, en el campo granuleUR. Se garantiza que es un identificador único en CMR. También puede encontrar el valor de product_list en Vertex. Consulta la [página del Cookbook](/api/cookbook) para este consejo y más.
	- product_list no puede ser utilizada en conjunto con otras palabras clave, sin embargo, puede ser utilizada con la palabra clave output.
	- Ejemplo:
		- product_list=ALAV2A276512920,
		S1A_IW_SLC__1SDV_20210614T154839_20210614T154905_038338_048643_D7E4-SLC

- <span style="color: #236192; font-size: 20px;">relativeOrbit</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Camino o trayectoria del satélite durante la adquisición de datos. Para UAVSAR es el [ID de Línea](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.201268782.1252483948.1620685771-1930115146.1605056035). Puede especificar un solo valor, un rango de valores o una lista de valores.
	- Ejemplo:
		- relativeOrbit=500,550-580
		- UAVSAR: relativeOrbit=05905
	- Valores:
		- ALOS: 1-671
		- ERS-1: 0-2410
		- ERS-2: 0-500
		- JERS-1: 0-658
		- RADARSAT-1: 0-342
		- SEASAT: 1-243
		- UAVSAR: varios

### Parámetros Geoespaciales
- <span style="color: #236192; font-size: 20px;">bbox</span>
	- *Aviso de Descontinuación:* Esta palabra clave será descontinuada. Por favor, utiliza 'intersectsWith' en su lugar.
	- Las cajas delimitadoras definen un área utilizando dos puntos de longitud/latitud. Los parámetros de la caja delimitadora son 4 números separados por comas: longitud inferior izquierda, latitud, y longitud superior derecha, latitud. Esta es una excelente opción para áreas de búsqueda muy amplias.
	- Ejemplo:
		- bbox=-150.2,65.0,-150.1,65.5

- <span style="color: #236192; font-size: 20px;">intersectsWith</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Búsqueda por polígono, un segmento de línea ("linestring") o un punto definido en texto bien conocido en 2D (WKT). Cada polígono debe estar explícitamente cerrado, es decir, el primer vértice y el último vértice de cada polígono listado deben ser idénticos. Los pares de coordenadas para cada vértice están en grados decimales: la longitud es seguida por la latitud.
	- Notas:
		- No soporta polígono múltiple, línea múltiple o punto múltiple.
 		- Los agujeros en los polígonos son ignorados
 		- Esta palabra clave también acepta una [solicitud POST](https://en.wikipedia.org/wiki/POST_(HTTP))
 	- Ejemplo (*Nota: Los espacios y paréntesis a continuación deben ser codificados en URL primero*):
 		- intersectsWith=polygon((-119.543 37.925, -118.443 37.7421, -118.682 36.8525, -119.77 37.0352, -119.543 37.925))
		- intersectsWith=linestring(-119.543 37.925, -118.443 37.7421)
		- intersectsWith=point(-119.543, 37.925)
	- Codificado correctamente en URL:
		- intersectsWith=point%28-119.543+37.925%29

- <span style="color: #236192; font-size: 20px;">polygon</span>
	- *Aviso de Descontinuación:* Esta palabra clave será descontinuada. Por favor, utiliza 'intersectsWith' en su lugar.
	- Polígono delimitador en formato digital de longitud/latitud; ingresa las coordenadas en dirección antihoraria, repitiendo el primer punto al final para cerrar el polígono: en el formato ABCDA.
	- Ejemplo:
		- polygon=-155.08,65.82,-153.5,61.91,-149.50,63.07,-149.94,64.55,-153.28,64.47,-155.08,65.82

#### Validación de Formas
Si el Área de Interés (AOI) especificada es su propio Rectángulo Delimitador Mínimo (MBR) en una proyección de Mercator, los resultados de búsqueda devueltos intersectarán con el AOI en una proyección de Mercator, independientemente de su anchura. Esto sigue siendo así incluso si se cruza la línea internacional de cambio de fecha dentro del AOI.

Para que un AOI se considere su propio MBR, debe cumplir con los siguientes criterios:

  - Cada vértice comparte una latitud o longitud con sus vecinos.
  - Los puntos Este/Oeste comparten longitud.
  - Los puntos Norte/Sur comparten latitud.

Los AOIs que no cumplan con estos criterios tendrán sus puntos conectados a lo largo de [círculos máximos](https://es.wikipedia.org/wiki/C%C3%ADrculo_m%C3%A1ximo).

Además, todos los AOIs son validados y luego simplificados según sea necesario. El proceso para esto es:
 
  1. Validar el AOI de entrada. Si no es válido, se muestra un error.
  2. Fusionar formas superpuestas.
  3. Casco convexo.
  4. Cualquier valor de índice fuera de rango se maneja ajustándolo y envolviéndolo al rango válido de valores.
  5. Simplificar puntos basados en el umbral de proximidad. El objetivo es tener menos de 400 puntos.

Cada uno de estos pasos se realiza solo cuando es necesario para obtener el AOI en un único contorno con menos de 400 puntos. Cualquier paso innecesario se omite.

**Ejemplos de validación y simplificación:**

- Se proporciona un polígono que se auto-intersecta: 
	- Se muestra un error.
- Se proporciona un único contorno, consistente en 1000 puntos:
	- Se utiliza una versión simplificada del mismo contorno, consistente en menos de 400 puntos.
- Se proporcionan múltiples geometrías, todas ellas superpuestas al menos en parte:
	- Se devuelve un único contorno, representando el contorno de todas las formas combinadas.
- Se proporcionan múltiples geometrías, algunas de ellas completamente no superpuestas:
	- Se devuelve un único contorno, representando el casco convexo de todas las formas juntas.


### Parámetros Temporales
- <span style="color: #236192; font-size: 20px;">processingDate</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Limita los resultados a registros que han sido procesados en ASF desde una fecha y/o hora dada.
	- Ejemplo:
		- processingDate=2017-01-01T00:00:00UTC

- <span style="color: #236192; font-size: 20px;">start</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Fecha de adquisición de datos. Se puede usar en combinación con 'end'. Puede introducir fechas en lenguaje natural, o una fecha y/o sello de tiempo. Todos los horarios están en UTC. Para más información sobre los formatos de fecha aceptados, consulta el punto final del Analizador de Fechas a continuación.
	- Ejemplo:
		- start=May+30,+2018
		- start=ayer
		- start=2010-10-30T11:59:59Z
		- start=hace+1+semana&end=ahora

- <span style="color: #236192; font-size: 20px;">end</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Fecha de adquisición de datos. Se puede usar en combinación con 'start'. Puede introducir fechas en lenguaje natural, o una fecha y/o sello de tiempo. Todos los horarios están en UTC. Para más información sobre los formatos de fecha aceptados, consulta el punto final del Analizador de Fechas a continuación.
	- Ejemplo:
		- end=May+30,+2018
		- end=hoy
		- end=2021-04-30T11:59:59Z
		- start=hace+1+semana&end=ahora

- <span style="color: #236192; font-size: 20px;">season</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Día de inicio y fin del año para el rango estacional deseado. Esta palabra clave puede usarse en conjunto con start/end para especificar un rango estacional dentro de un rango de fechas general. Los valores se basan en el calendario juliano. Debe especificar tanto una fecha de inicio como de fin de la temporada.
	- Ejemplo:
		- season=1,31
		- season=45,67
		- season=360,10
	- Valores:
		- 1 a 365

### Parámetros de Resultados
- <span style="color: #236192; font-size: 20px;">output</span>
	- Formato deseado de los resultados de la API de Búsqueda. Si no se especifica, el formato predeterminado es metalink. El formato preferido es geoJSON.
	- Ejemplo:
		- output=geojson
	- Valores:
		- geojson, csv, json, kml, metalink, count, download
	- Descripción:
		- GeoJSON es el formato de salida preferido. Si un campo requerido no está incluido, por favor contacta a ASF usando la información a continuación o contacta al equipo directamente en <uaf-asf-discovery@alaska.edu>
		- KML se puede abrir en Google Earth, ArcGIS Earth, o un programa similar
		- Count devuelve el número de resultados obtenidos por su consulta. No incluye información adicional. Usar la salida count puede ser útil para determinar si su consulta ha devuelto el número correcto de resultados. Hay un límite de tiempo para ejecutar consultas de la API de Búsqueda. Consulta la [página de Solución de Problemas](/api/troubleshooting) para más detalles.
		- Metalink proporciona información de descarga para las escenas devueltas por su consulta. No incluye metadatos.
		- Download devuelve un script de descarga masiva que incluye los archivos devueltos por la búsqueda. Consulta la [documentación de Descarga Masiva](https://asf.alaska.edu/how-to/data-tools/asf-bulk-data-download-options/) para una guía completa sobre cómo usar el script de descarga masiva.
		- JSON incluye metadatos de la escena y URLs de productos. Si GeoJSON no satisface tus necesidades, JSON es el formato preferido para uso programático.
		- CSV también incluye metadatos de la escena y URLs de productos. CSV devuelve menos campos que JSON.

- <span style="color: #236192; font-size: 20px;">maxResults</span>
	- Esta palabra clave también está disponible a través de [asf_search](/asf_search/searching/#searching).
	- Número máximo de registros de datos a devolver de su consulta.
	- Ejemplo:
		- maxResults=10

## Punto Final de Baseline
<https://api.daac.asf.alaska.edu/services/search/baseline>

- <span style="color: #236192; font-size: 20px;">reference</span>
	- Esta es la única palabra clave obligatoria. Introduce el nombre de la escena de referencia para la cual deseas ver los resultados de la Baseline.
	- Ejemplo:
		- reference=S1B_IW_SLC__1SDV_20210704T135937_20210704T140004_027645_034CB0_4B2C

- <span style="color: #236192; font-size: 20px;">processingLevel</span>
	- Nivel al que los datos han sido procesados. Los datos de Baseline solo están disponibles para ciertos niveles de procesamiento.
	- Ejemplo:
		- processingLevel=L1.5
	- Valores de ProcessingLevel que Contienen Datos de Baseline:
		- ALOS: L1.1, L1.5; por defecto es L1.1
		- ERS-1 & ERS-2: L0, L1; por defecto es L0
		- JERS-1: L0, L1; por defecto es L0
		- RADARSAT-1: L0, L1; por defecto es L0
		- Sentinel-1A & Sentinel-1B: SLC

- <span style="color: #236192; font-size: 20px;">output</span>
	- Formato deseado de los resultados de la API de Búsqueda. Si no se especifica, el formato predeterminado es metalink. El formato preferido es geoJSON.
	- Ejemplo:
		- output=geojson
	- Valores:
		- geojson, csv, json, kml, metalink, count, download
	- Descripción:
		- GeoJSON es el formato de salida preferido. Si un campo requerido no está incluido, por favor contacta a ASF usando la información a continuación o contacta al equipo directamente en <uaf-asf-discovery@alaska.edu>
		- KML se puede abrir en Google Earth, ArcGIS Earth, o un programa similar
		- Count devuelve el número de resultados obtenidos por su consulta. No incluye información adicional. Usar la salida count puede ser útil para determinar si su consulta ha devuelto el número correcto de resultados. Hay un límite de tiempo para ejecutar consultas de la API de Búsqueda. Consulta la [página de Solución de Problemas](/api/troubleshooting) para más detalles.
		- Metalink proporciona información de descarga para las escenas devueltas por su consulta. No incluye metadatos.
		- Download devuelve un script de descarga masiva que incluye los archivos devueltos por la búsqueda. Consulta la [documentación de Descarga Masiva](https://asf.alaska.edu/how-to/data-tools/data-tools/#bulk_download) para una guía completa sobre cómo usar el script de descarga masiva.
		- JSON incluye metadatos de la escena y URLs de productos. Si GeoJSON no satisface tus necesidades, JSON es el formato preferido para uso programático.
		- CSV también incluye metadatos de la escena y URLs de productos. CSV devuelve menos campos que JSON.

- <span style="color: #236192; font-size: 20px;">maxResults</span>
	- Número máximo de registros de datos a devolver de su consulta.
	- Ejemplo:
		- maxResults=10

## Punto Final de Validación WKT
<https://api.daac.asf.alaska.edu/services/utils/wkt>

Este punto final validará y reparará una entrada WKT. La salida WKT reparada es cómo la API de Búsqueda interpretará la entrada WKT proporcionada. Si un WKT no puede ser reparado, devolverá un error indicando la razón. Todas las validaciones y errores se devuelven en formato JSON.

- <span style="color: #236192; font-size: 20px;">wkt</span>
	- Esta es la única palabra clave aceptada para este punto final.
	- Ejemplo:
		- wkt=GEOMETRYCOLLECTION(POLYGON((46 -19,30 26,-3 41,22 39,49 16,46 -19)), POLYGON((27 24,12 4,18 31,27 24)))
		- En este ejemplo, la devolución JSON enumerará los errores que fueron reparados, y el WKT final envuelto y sin envolver.

## Punto Final de Archivos GeoEspaciales a WKT

<https://api.daac.asf.alaska.edu/services/utils/files_to_wkt>

Este punto final aceptará una [solicitud POST](https://en.wikipedia.org/wiki/POST_(HTTP)) con archivos adjuntos. Devolverá el WKT analizado del archivo, así como el WKT envuelto y sin envolver reparado. Todas las salidas se devuelven en formato JSON. El formato de archivo preferido es geojson, pero la API de Búsqueda también admitirá otros formatos, como shapefile o kml.

Consulta la [página de Herramientas](/api/tools) para más detalles sobre las solicitudes POST.

- Ejemplo:
	- curl -X POST -F 'files=@/path/to/file' 'https://api.aac.asf.alaska.edu/services/utils/files_to_wkt'

## Punto Final del Analizador de Fechas
<https://api.daac.asf.alaska.edu/services/utils/date>

Este punto final se puede usar para verificar cómo se analizan las fechas por la API de Búsqueda. Todas las fechas analizadas se devuelven en formato JSON.

- <span style="color: #236192; font-size: 20px;">date</span>
	- Esta es la única palabra clave aceptada para este punto final. Puede usar lenguaje natural, como "ayer", fechas con o sin sello de tiempo, o días de la semana.

## Punto Final de Lista de Misiones
<https://api.daac.asf.alaska.edu/services/utils/mission_list>

Este punto final enumera todas las misiones (también conocidas como campañas o colecciones) para todos los conjuntos de datos. Cualquiera de las misiones devueltas en la lista puede usarse como valor para la palabra clave collectionName en el punto final de Búsqueda. La lista de misiones se devuelve en formato JSON.

- <span style="color: #236192; font-size: 20px;">platform</span>
	- Esta palabra clave es opcional. Si se usa, restringirá la lista de misiones a las plataformas especificadas.
	- Plataforma de teledetección que adquirió los datos. Sentinel-1 y ERS tienen múltiples plataformas de teledetección, y puede elegir si especificar una plataforma específica. Puede especificar un solo valor o una lista de valores.
	- Ejemplo:
		- platform=ALOS
		- platform=SA,SB
		- platform=S1
	- Valores:
		- ALOS, A3, AIRSAR, AS, ERS, ERS-1, E1, ERS-2, E2, JERS-1, J1, RADARSAT-1, R1, SEASAT, SS, S1, Sentinel, Sentinel-1, Sentinel-1A, SA, Sentinel-1B, Sentinel-1 Interferogram (BETA), SB, SMAP, SP, UAVSAR, UA

## Punto Final de Salud
<https://api.daac.asf.alaska.edu/health>

Este punto final se utiliza para verificar el estado de salud de la API de Búsqueda. Se devuelve en formato JSON. No hay palabras clave asociadas con el punto final de verificación de salud.

Además de la salud de la API de Búsqueda, también devuelve las configuraciones de la API de Búsqueda y el estado de salud de CMR.
