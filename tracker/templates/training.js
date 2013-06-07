{
    "type": "FeatureCollection",
    "features": [
{% for p in points %}
        {
            "geometry": {
                "type": "Point",
                "coordinates": [
                    {{ p.lat }},
                    {{ p.lng }}
                ]
            },
            "type": "Feature",
            "properties": {
                "city": "{{ p.city }}", 
                "year": "{{ p.date.year }}", 
                "type": "{{ p.type }}", 
                "host": "{{ p.host }}",
                "stories": [
                        {% for article in p.article.all %}
                            {
                             "headline": "{{ article.headline }}", 
                             "slug": "{{ article.slug }}"
                            }{% if not forloop.last %},{% endif %}
                        {% endfor %}
                    ]
            }
        }{% if not forloop.last %},{% endif %}
{% endfor %}
    ]
}
