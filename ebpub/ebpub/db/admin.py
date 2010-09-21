from django.conf import settings
from django.contrib.gis import admin
from ebpub.db.models import Location
from ebpub.db.models import LocationType
from ebpub.db.models import NewsItem
from ebpub.db.models import Schema
from ebpub.db.models import SchemaField
from ebpub.db.models import SchemaInfo

"""
See http://docs.djangoproject.com/en/dev/ref/contrib/gis/admin/
"""


class OSMModelAdmin(admin.GeoModelAdmin):
    # Use GeoModelAdmin to get editable geometries.
    # But we'll override a few defaults.

    default_zoom = 11
    openlayers_url = getattr(settings, 'OPENLAYERS_URL', admin.GeoModelAdmin.openlayers_url)
    point_zoom = 14
    wms_layer = 'openstreetmap'
    wms_name = 'OpenStreetMap'
    wms_url = 'http://maps.opengeo.org/geowebcache/service/wms'

    # TODO: upstream patch for geodjango: add a wms_format option so
    # we can easily use png instead of jpeg.  Or maybe arbitrary other
    # params.

    @property
    def default_lat(self):
        return settings.DEFAULT_MAP_CENTER_LAT

    @property
    def default_lon(self):
        return settings.DEFAULT_MAP_CENTER_LON


class NewsItemAdmin(OSMModelAdmin):
    pass

class LocationAdmin(OSMModelAdmin):
    pass

admin.site.register(Schema)
admin.site.register(SchemaField)
admin.site.register(SchemaInfo)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(LocationType)
admin.site.register(Location, LocationAdmin)