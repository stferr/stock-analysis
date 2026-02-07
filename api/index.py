from api.app import app

# Vercel expects a handler function
def handler(request):
    return app(request.environ, lambda *args: None)

# Also export app directly for Vercel
application = app
