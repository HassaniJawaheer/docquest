from fastapi import Request, HTTPException

def get_session_id(request: Request) -> str:
    session_id = getattr(request.state, "session_id", None)
    if not session_id:
        raise HTTPException(status_code=401, detail="Session ID missing.")
    
    session_manager = request.app.state.session_manager
    if not session_manager.is_valid(session_id):
        raise HTTPException(status_code=401, detail="Session expired or invalid.")
    
    return session_id
