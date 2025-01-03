try:
    from .log_logic import req
except:
    from log_logic import req

read2server = req.ReqToServer()
session_key = read2server.create_session()
read2server.add_to_session(session_code=session_key, data={"project_name": "import quick-doc-py"})