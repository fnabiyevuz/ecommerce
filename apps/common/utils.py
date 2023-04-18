def get_session_key(request) -> str:
    """
    Get session_key or create new one
    """
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    session_key = request.session.session_key
    return session_key
