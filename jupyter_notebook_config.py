# Configuration file for jupyter-notebook.
c.ServerProxy.servers = {
    'uvicorn': {
        'command': [
            'uvicorn',
            'main:app',
            '--port',
            '{port}',
        ],
        'absolute_url': False,
    }
}
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.ServerApp.token = ''
c.ServerApp.password = ''