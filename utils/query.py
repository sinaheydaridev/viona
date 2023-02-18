from rest_framework import exceptions


def get_object(model, pk):
    try:
        return model.objects.get(id=pk)
    except ValueError as e:
        raise exceptions.NotFound({"detail": e})
    except model.DoesNotExist:
        raise exceptions.NotFound({"detail": "Not found."})


def get_queryset(model, lookups=None):
    queryset = model.objects.all()
    if lookups:
        try:
            queryset = queryset.filter(lookups)
        except ValueError as e:
            raise exceptions.ParseError({"detail": e})
    return queryset
