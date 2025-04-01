# Code Citations

## License: unknown
https://github.com/MassiBelaid/uncompilated_name/tree/d151c4849b8d81355ea0344c81c50a1155d87de9/uncompilated_name/urls.py

```
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls'))]
```

