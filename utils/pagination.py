def paginate(queryset, serializer, page, limit):
    current_page = int(page) or 1
    current_limit = int(limit) or 10

    items = queryset[(current_page - 1) * current_limit:][:current_limit]
    serializer.instance = items
    response_data = {
        "items": serializer.data,
        "count": queryset.count(),
        "current_page": current_page,
        "limit": current_limit
    }

    return response_data
