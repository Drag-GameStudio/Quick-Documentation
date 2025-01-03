
print("-" * 80)
print(f"""Support the Project
If you like this project, you can support it on https://ko-fi.com/draggamestudio. 
Your support helps improve the project and add new features. Thank you!""")
print("-" * 80)


try:
    from .log_logic import req
except:
    from log_logic import req



try:
    read2server = req.ReqToServer()
    session_key = read2server.create_session()
    read2server.add_to_session(session_code=session_key, data={"project_name": "import quick-doc-py"})
except:
    pass