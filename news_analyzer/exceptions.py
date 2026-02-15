"""Definicion de excepciones personalizadas para la aplicacion - Definition of custom exceptions for the application."""


class NewsSystemError(Exception):
    """Excepción personalizada para errores del sistema de noticias."""

    pass


class APIKeyError(NewsSystemError):
    """Excepción personalizada para errores de API key."""

    pass
