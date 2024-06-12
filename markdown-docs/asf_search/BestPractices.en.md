# asf_search Best Practices

In addition to covering best practices, this page also contains advanced search techniques and serves as the "philosophy of asf_search".

Topics covered include:

- General recommendations, including
working with results, performance, common search filters and types, and count
- Dataset specifics for NISAR and Opera
- Granule and product searches and the preferred method for these
- Secondary searches such as stacking
- Download and recommended authentication method
- Advanced search techniques, including ranges, subclasses, large result sets, and more

## General Recommendations
This section contains information on result sets, general performance, the different search types available, and common filter examples.

### Result Sets
Search results are returned as an `ASFSearchResults` object, a sublass of `User List`, containing a list of `ASFProduct` objects. Each of these classes provides some additional functionality to aid in working with the results and individual products.
`ASFProduct` provides a number of metadata fields, such as:

- Geographic coordinates
- Latitude/Longitude
- Shape type
- Scene and product metadata
- Path, frame
- Platform, beam, polarization
- File name, size, URL

Geographic coordinates are stored in the geometry attribute:

`results[0].geometry`

Other metadata is available through the properties attribute:

`results[0].properties`

`ASFProduct` objects provides geojson-based serialization, in the form of a geojson feature snippet:

`print(results[0])`

`ASFSearchResults` also supports the following output formats:

- csv
- jsonlite
- jsonlite2
- metalink
- kml

### General performance
When searching for multiple products it's faster to search all products at once in a single search, rather than running a separate query for each product, which involves multiple https requests.

``` python
import asf_search as asf

granules = ['S1B_IW_GRDH_1SDV_20161124T032008_20161124T032033_003095_005430_9906', 'S1-GUNW-D-R-087-tops-20190301_20190223-161540-20645N_18637N-PP-7a85-v2_0_1', 'ALPSRP111041130']

# THIS IS SLOW AND MAKES MORE NETWORK REQUESTS THAN NECESSARY
batched_results = ASFSearchResults([])
for granule in granules:
    unbatched_response = asf.granule_search(granules_list=granule)
    batched_results.extend(batched_results)

# THIS WILL ALWAYS BE FASTER
fast_results = asf.granule_search(granules_list=granules)
```

If you need to perform intermediate operations on large results (such as writing metadata to a file or calling some external process on results), use the `search_generator()` method to operate on results as they're returned page-by-page (default page size is 250).

``` python
import asf_search as asf

opts = asf.ASFSearchOptions(platform=asf.DATASET.SENTINEL1, maxResults=1000)

for page in asf.search_generator(opts=opts):
    foo(page)
```


### Differences between search types
Placeholder

This is already in the docs [here](/asf_search/searching/). Do we want to repeat it? 

### Common Filters 
Search options can be specified using kwargs, which also allows them to be handled using a dictionary:

	opts = {
    	'platform': asf.PLATFORM.ALOS,
    	'start': '2010-01-01T00:00:00Z',
    	'end': '2010-02-01T23:59:59Z'
	}
 
Below are some common filter examples:

	results = asf.geo_search(
    	intersectsWith='POLYGON((-91.97 28.78,-88.85 28.78,-88.85 30.31,-91.97 30.31,-91.97 28.78))',
    	platform=asf.PLATFORM.UAVSAR,
    	processingLevel=asf.PRODUCT_TYPE.METADATA,
		maxResults=250)

### search_count()
You may use the `search_count()` method to return the count of total results matching the passed search options.

This example returns the current size of the SENTINEL1 catalog:
    
    opts = {
    'platform': asf.PLATFORM.SENTINEL1}
    count = asf.search_count(**opts)

## Dataset Specifics
Constants are provided for each dataset. The list of constants can be found [here](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/DATASET.py).

Basic dataset search example:
    
    sentinel_results = asf.search(dataset=asf.DATASET.SENTINEL1, maxResults=250)

You can view the metadata for your results via the properties dictionary:

    sentinel_results[0].properties

Or you can view the metadata as a geojson formatted dictionary:

    sentinel_results.geojson()

### NISAR
asf_search supports searching for lists of short names by the `shortName` keyword.
The currently available NISAR data that CMR provides lacks searchable additional attributes.
Therefore, the best way to search for NISAR results is via combinations of `shortName`, `dataset`, `platform`, and `granule_list`/`product_list` keywords.

NISAR example:

    nisar_gslc_gunw = asf.search(shortName=['NISAR_L2_GSLC_V1', 'NISAR_L2_GUNW_V1'], opts=search_opts, maxResults=250)
    print(nisar_gslc_gunw)

### Opera-S1
The Opera dataset has both standard products and CalVal (calibration/validation) products available.
Please note that the CalVal products are treated as their own dataset in asf_search.
Both can be found in the [constants list](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/DATASET.py).

### Others?
Placeholder

Do other datasets have specific-to-them search constraints, options, etc?

### Further Reading
For more information on the constants and keywords available, see [this page](/asf_search/searching/#keywords).

## Granule & Product Searches
`granule_search()` and `product_search()` are similar.
Granule (also called a scene) searches include all files types for the specified granule, whereas product searches specify one file type. 
Granule searches can be 1:many, whereas a product search will always be 1:1. 

Granule search example:

    granule_list = [
        'S1B_IW_GRDH_1SDV_20190822T151551_20190822T151616_017700_0214D2_6084',
        'S1B_IW_GRDH_1SDV_20190810T151550_20190810T151615_017525_020F5A_2F74',
        'S1B_IW_GRDH_1SDV_20190729T151549_20190729T151614_017350_020A0A_C3E2',
        'S1B_IW_GRDH_1SDV_20190717T151548_20190717T151613_017175_0204EA_4181',
        'S1B_IW_GRDH_1SDV_20190705T151548_20190705T151613_017000_01FFC4_24EC',
        'S1B_IW_GRDH_1SDV_20190623T151547_20190623T151612_016825_01FA95_14B9',
        'S1B_IW_GRDH_1SDV_20190611T151546_20190611T151611_016650_01F566_D7CE',
        'S1B_IW_GRDH_1SDV_20190530T151546_20190530T151611_016475_01F02E_BF97',
        'S1B_IW_GRDH_1SDV_20190518T151545_20190518T151610_016300_01EAD8_9308',
        'S1B_IW_GRDH_1SDV_20190506T151544_20190506T151609_016125_01E56C_1D67'
    ]
    results = asf.granule_search(granule_list)
    print(results)

Product search example: 

    product_list = [
        'S1A_IW_GRDH_1SDV_20190809T001336_20190809T001401_028485_033839_78A1-GRD_HD',
        'S1A_IW_GRDH_1SDV_20150322T000454_20150322T000524_005137_006794_56E3-GRD_HD',
        'S1A_IW_GRDH_1SDV_20160121T001256_20160121T001321_009585_00DF26_5B84-GRD_HD',
        'S1A_IW_GRDH_1SDV_20151117T000448_20151117T000513_008637_00C455_3DC2-GRD_HD'
    ]
    results = asf.product_search(product_list)
    print(results)

`granule_search()` & `product_search()` do not make use of any other search filters, but will accept kwargs for consistency with other search functions:

    results = asf.granule_search(granule_list=granule_list)
    print(f'{len(results)} results found')

### Note about incorrect methods
It is generally preferred to "collapse" many small queries into fewer large queries. That is, it may be easy and logically reasonable to run a number of small `granule_search()` queries via a `foreach` loop over each of the items in the original granule list. *Please do not do this.* It consumes a lot of resources at both ASF and at CMR.

Instead, combine your small queries into a single large query where possible, as shown above, and then post-process the results locally. `granule_search()` and `product_search()` can support very large lists, and will break them up internally when needed.

## Secondardy Searches
Placeholder

What secondary searches are there, other than baseline stacking?

### Stacking
Once you have identified a result set or a product id, you may wish to build a baseline stack based on those results.
You may use either the `stack()` or `stack_from_id()` methods to accomplish this. 

`stack_from_id()` is provided largely as a convenience: internally, it performs a `product_search()` using the provided ID, and then returns the results of that product's `stack()` method.
For this reason, it is recommended that if you have an `ASFProduct` object at hand, you use that to build your stack directly, as it removes the need for the additional search action.
For other cases where you have parameters describing your reference scene but not an `ASFProduct` object itself, it is appropriate to use one of the various search features available to obtain an `ASFProduct` first.

A basic example using `ASFProduct.stack()`:
    
    import asf_search as asf

    reference = asf.product_search('S1A_IW_SLC__1SDV_20220215T225119_20220215T225146_041930_04FE2E_9252-SLC')[0]

    print(reference.stack())

The results are a standard `ASFSearchResults` object containing a list of `ASFProduct` objects, each with all the usual functionality.
There are 2 additional fields in the `ASFProduct` objects: `temporalBaseline` and `perpendicularBaseline`.
`temporalBaseline` describes the temporal offset in days from the reference scene used to build the stack. 
`perpendicularBaseline` describes the perpendicular offset in meters from the reference scene used the build the stack.
The reference scene is included in the stack and will always have a temporal and perpendicular baseline of 0.

### etc?

## Platform vs Dataset
asf-search provides 2 major keywords with subtle differences
    - `platform`
    - `dataset`

`platform` maps to the `platform[]` cmr keyword, values like `Sentinel-1A`, `UAVSAR`, `ALOS`. A limitation of searching by 
platform is that for platforms like `Sentinel-1A` there are a lot of Sentinel 1 derived product types (`OPERA-S1`, `SLC-BURST`). Given for every `SLC` product theres 27 additional `OPERA-S1` and `SLC-BURST` products this can lead to homogynous results depending on your search filters.

The `dataset` keyword serves as a solution for this. Each "dataset" is a collection of concept-ids generally associated with commonly used datasets.

``` python
# At the time of writing will likely contain mostly `OPERA-S1` and/or `SLC-BURST` products
platform_results = asf.search(dataset=asf.PLATFORM.SENTINEL1, maxResults=250) 

# Will contain everything but `OPERA-S1` and/or `SLC-BURST` products
dataset_results = asf.search(dataset=asf.DATASET.SENTINEL1, maxResults=250)

# Will contain OPERA-S1 Products
opera_results = asf.search(dataset=asf.DATASET.OPERA_S1, maxResults=250)

# Will contain SLC-BURST products
slc_burst_results = asf.search(dataset=asf.DATASET.SLC_BURST, maxResults=250)
```

## CMR UAT Host
asf-search defaults to querying against the production cmr api, `cmr.earthdata.nasa.gov`.
In order to use another cmr host, set the `host` keyword with `ASFSearchOptions`.

``` python
uat_opts = asf.ASFSearchOptions(host='cmr.uat.earthdata.nasa.gov', maxResults=250)
uat_results = asf.search(opts=uat_opts)
```

## Campaign lists
asf-search provides a built in method for searching for campaigns

`asf.campaigns(platform=asf.PLATFORM.SENTINEL1A)`

## CMR Keyword Aliasing
asf-search aliases the following keywords behind the scenes with corresponding collection concept ids for improved search performance:
- `platform`
- `processingLevel`

The Alias lists are updated as needed with each release, but if you're not finding expected results then the alias list may be out of date. In order to skip the aliasing step set the `collectionAlias` keyword to false with `ASFSearchOptions`

``` python
opts = asf.ASFSearchOptions(collectionAlias=False, maxResults=250)
unaliased_results = asf.search(opts=opts)
```

**Please note, this will result in slower average search times.** If there are any results missing from new datasets please report it as an [issue in github](https://github.com/asfadmin/Discovery-asf_search/issues) with the concept id of the missing collection and the name.

## Download

This [Jupyter notebook](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/5-Download.ipynb) covers the available authentication methods.
Once authenticated, it provides a workflow for downloading search results.

### Recommended Authentication
Using .netrc credentials is the preferred method for authentication.
This [guide](https://www.labkey.org/Documentation/wiki-page.view?name=netrc) will show you how to set up a .netrc file.
Requests will attempt to get the authentication credentials for the URL’s hostname from your .netrc file.
The .netrc file overrides raw HTTP authentication headers set with `headers=`.
If credentials for the hostname are found, the request is sent with HTTP Basic Auth.

## Advanced Search Techniques
Below you will find recommendations for advanced search techniques, such as ranges, subclassing, authentication, and the preferred method for large searches.

### Cool range stuff
Placeholder

### Subclassing
`ASFProduct` is the base class for all search result objects.
There are several subclasses of `ASFProduct` that are used for specific platforms and product types with unique properties/functionality.

Key Methods:

- `geojson()`
- `download()`
- `stack()`
- `get_stack_opts()` (returns None in `ASFProduct`, implemented by `ASFStackableProduct` subclass and its subclasses)
- `centroid()`
- `remotezip()` (requires optional dependency to be installed)
- `get_property_paths()` (gets product's keywords and their paths in umm dictionary)
- `translate_product()` (reads properties from umm, populates `properties` with associated keyword)
- `get_sort_keys()`
- `umm_get()`

Key Properties:

- `properties`
- `_base_properties` (what `get_property_paths()` uses to find values in umm JSON `properties`)
- `umm` (the product's umm JSON from CMR)
- `metadata` (the product's metadata JSON from CMR)

`ASFStackableProduct` is an important `ASFProduct` subclass, from which stackable product types meant for time series analysis are derived.
`ASFStackableProduct` has a class enum, `BaselineCalcType`, that determines how perpendicular stack calculations are handled.
Each subclass keeps track of their baseline calculation type via the `baseline_type` property.

Inherits: `ASFProduct`

Inherited By: `ALOSProduct`; `ERSProduct`; `JERSProduct`; `RADARSATProduct`; `S1Product`;
`S1BurstProduct`; `OPERAS1Product`, `ARIAS1GUNWProduct`

Key Methods:

- `get_baseline_calc_properties()`
- `get_stack_opts()` (overrides `ASFproduct`)
- `is_valid_reference()`
- `get_default_baseline_product_type()`

Key Definitions for class enum `BaselineCalcType`:

- `PRE_CALCULATED`: has pre-calculated `insarBaseline` value that will be used for perpendicular calculations
- `CALCULATED`: uses position/velocity state vectors and ascending node time for perpendicular calculations

Key Fields:

- `baseline`
- `baseline_type` (`BaselineCalcType.PRE_CALCULATED` by default or `BaselineCalcType.CALCULATED`)

Because `ASFProduct` is built for subclassing, that means you can provide your own custom subclasses dervied directly from `ASFProduct` or even from a pre-existing subclass like `S1Product` or `OperaS1Product`.

For more information on subclassing, see the [Jupyter notebook](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/Advanced-Custom-ASFProduct-Subclassing.ipynb).

### Using authenticated searches
Downloading data, and accessing some data, requires an authenticated session with Earthdata Login.
To simplify this workflow, the `ASFSession` class is provided. 
    
    auth_with_creds()
    auth_with_token()
    auth_with_cookiejar()

Creating an authenticated session example:

    from getpass import getpass
    session = asf.ASFSession()
    session.auth_with_creds(input('EDL Username'), getpass('EDL Password'))

The `ASFSearchOptions` class is provided for storing and validating search parameters.
Creating an `ASFSearchOptions` object is required to pass our authenticated session to `search()`.

    search_opts = asf.ASFSearchOptions(
    dataset=asf.DATASET.NISAR,
    session=session)

    nisar_response = asf.search(opts=search_opts, maxResults=250)

### search_generator() for large result sets
The recommended way to perform large, long-running searches is to use `search_generator()` to yield CMR results page by page.
This allows you to stream results to a file in the event CMR times out.
Different output formats can be used.

Note that asf_search queries CMR with page sizes of 500, so setting maxResults=1000 means asf_search will have to query cmr twice, each time returning 500 products:

`large_results_generator = asf.search_generator(maxResults=1000, platform=asf.PLATFORM.SENTINEL1A)`

	with open("search_results.metalink", "w") as f:
		f.writelines(asf.export.results_to_metalink(large_results_generator))

Another usage example:

	import asf_search as asf
	opts = asf.ASFSearchOptions(shortName='ARIA_S1_GUNW')
	urs = []
	for page in asf.search_generator(opts=opts):
    	urs.extend(product.properties['fileID'] for product in page)
    	print(len(urs))

### Downloading additional files
Some product types, such as S1 Bursts or Opera RTC products, have several files that can be downloaded.
We can specify which files to download by setting the `fileType` and using the `FileDownloadType` enum class.

Additional files are stored in this array:

    product.properties['additionalUrls']

To download only the additional files:

    FileDownloadType.ADDITIONAL_FILES    # everything in 'additionalUrls'

To download the default file:

    FileDownloadType.DEFAULT_FILE        # The default data file, 'url'

To download both:

    FileDownloadType.ALL_FILES           # all of the above

This example will download all additional files under the `additionalUrls` attribute:

    cslc_results[0].download(session=session, path = './', fileType=asf.FileDownloadType.ADDITIONAL_FILES) 

To be more specific, we can use the `download_urls()` or `download_url()` methods

    print(f"Additional urls: {opera_results[0].properties['additionalUrls']}")
    
    url = opera_results[0].properties['additionalUrls'][0]
    fileName = url.split('/')[-1]
    
    asf.download_url(url, session=session, path ='./', filename=fileName)

### S3 URIs
Some product types (Sentinel-1, BURST, OPERA, and NISAR) have s3 direct access uris. When available, they are accessible under
`ASFProduct.properties['s3Urls']`.

### CMR Keywords Search Parameter
You can also search for granules using `readable_granule_name` via pattern matching.

To do this, you can pass the CMR search keyword config directly with the `cmr_keywords` search parameter.
This allows you to pass any valid CMR keyword-value pair that isn't covered by asf_search directly, as well as configure existing parameter behavior.

More info on pattern matching and parameter options can be found [here](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#Parameter-Options).

Example:

    gslc_results = asf.search(granule_list=['*046_009_A_095*'], cmr_keywords=('options[readable_granule_name][pattern]', 'true'), opts=search_opts)
    
    for product in gslc_results:
        print(product.properties['fileID'])
